import polars as pl
import argparse
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import LabelEncoder
from typing import List, Dict
from torch import nn, optim
import os


class ClasseDataset(Dataset):
    def __init__(self, grouped_data: dict):
        """
        Args:
            grouped_data (dict): Dictionary of grouped sequences by classe.
        """
        self.data = grouped_data
        self.classes = list(grouped_data.keys())

    def __len__(self):
        return len(self.classes)

    def __getitem__(self, idx):
        classe = self.classes[idx]
        sequences = self.data[classe]
        # Replace NaN values with zeros
        sequences = [[0 if val != val else val for val in seq] for seq in sequences]
        return classe, torch.tensor(sequences, dtype=torch.float)


class LSTMSequencePredictor(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        """
        LSTM model for sequence prediction
        
        Args:
            input_size (int): Number of features in input sequence
            hidden_size (int): Number of LSTM hidden units
            num_layers (int): Number of LSTM layers
            output_size (int): Number of features to predict
        """
        super(LSTMSequencePredictor, self).__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # LSTM layers
        self.lstm = nn.LSTM(
            input_size=input_size, 
            hidden_size=hidden_size, 
            num_layers=num_layers, 
            batch_first=True
        )
        
        # Fully connected layer to map LSTM output to prediction
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        """
        Forward pass of the LSTM
        
        Args:
            x (torch.Tensor): Input sequence of shape (batch_size, seq_length, input_size)
        
        Returns:
            torch.Tensor: Predicted sequence
        """
        # Check sequence length
        if x.size(1) == 0:
            raise ValueError(f"Input sequence has zero length. Input shape: {x.shape}")

        # Initialize hidden state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # LSTM forward pass
        out, _ = self.lstm(x, (h0, c0))
        
        # Predict the next sequence values
        predictions = self.fc(out)
        
        return predictions


def train_lstm_model(dataloader, input_size, hidden_size=64, num_layers=2, 
                     learning_rate=0.01, epochs=100):
    """
    Train LSTM model on variable-length sequences
    
    Args:
        dataloader (DataLoader): DataLoader containing sequences
        input_size (int): Number of input features
        hidden_size (int): LSTM hidden layer size
        num_layers (int): Number of LSTM layers
        learning_rate (float): Optimizer learning rate
        epochs (int): Number of training epochs
    
    Returns:
        nn.Module: Trained LSTM model
    """
    # Instantiate the model
    model = LSTMSequencePredictor(
        input_size=input_size, 
        hidden_size=hidden_size, 
        num_layers=num_layers, 
        output_size=input_size  # Predict same number of features
    )
    
    # Loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    # Training loop
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        batch_count = 0
        
        for classe, sequences in dataloader:
            # Skip empty or too short sequences
            if sequences.size(1) <= 1:
                print(f"Skipping sequence for class {classe} due to insufficient length")
                continue
            
            # Prepare input and target
            # Use all but the last time step as input, last time step as target
            input_seq = sequences[:, :-1, :]
            target_seq = sequences[:, 1:, :]
            
            # Zero gradients
            optimizer.zero_grad()
            
            # Forward pass
            try:
                predictions = model(input_seq)
            except ValueError as e:
                print(f"Error processing sequence: {e}")
                continue
            
            # Compute loss
            loss = criterion(predictions, target_seq)
            
            # Backward pass and optimize
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            batch_count += 1
        
        # Print loss every 10 epochs
        if epoch % 10 == 0 and batch_count > 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {total_loss/batch_count:.4f}')
    
    return model


def generate_sequence(model, initial_sequence, num_steps_to_generate=4):
    """
    Generate a new sequence based on an initial sequence
    
    Args:
        model (nn.Module): Trained LSTM model
        initial_sequence (torch.Tensor): Starting sequence
        num_steps_to_generate (int): Number of additional steps to generate
    
    Returns:
        torch.Tensor: Generated sequence
    """
    model.eval()
    with torch.no_grad():
        # Ensure initial sequence has at least one step
        if initial_sequence.size(1) == 0:
            raise ValueError("Initial sequence cannot be empty")
        
        current_seq = initial_sequence
        generated_sequences = [current_seq]
        
        for _ in range(num_steps_to_generate):
            # Get prediction for the last step
            pred = model(current_seq)
            
            # Take the last predicted step
            last_pred = pred[:, -1:, :]
            
            # Concatenate the prediction to the sequence
            current_seq = torch.cat([current_seq, last_pred], dim=1)
            generated_sequences.append(last_pred)
        
        return torch.cat(generated_sequences, dim=1)

    
def collate_fn(batch):
    """
    Pads sequences to the maximum length in the batch.
    Args:
        batch (list): List of tuples (classe, sequences) from the dataset.
    Returns:
        tuple: (classes, padded_sequences)
    """
    classes, sequences = zip(*batch)  # Separate classes and sequences
    max_length = max(seq.size(0) for seq in sequences)  # Find the longest sequence
    padded_sequences = torch.zeros(len(sequences), max_length, sequences[0].size(1))  # Initialize padded tensor
    
    for i, seq in enumerate(sequences):
        padded_sequences[i, :seq.size(0), :] = seq  # Copy data into padded tensor

    return classes, padded_sequences

def create_sequences(df: pl.DataFrame) -> dict:
    """
    Group records by "classe", create sequences, and pad to max_length.
    Args:
        df (pl.DataFrame): Processed DataFrame with "classe" grouping and sorted "DATA".
    Returns:
        dict: Grouped sequences, padded to max_length.
    """
    grouped_data = {}

    # Get numerical columns only (excluding "classe")
    numeric_columns = [
        col for col, dtype in zip(df.columns, df.dtypes)
        if dtype in [pl.Int32, pl.Int64, pl.Float32, pl.Float64] and col != "classe"
    ]
    max_length = len(numeric_columns)  # Set max_length as the number of numeric features
    
    # Replace NaNs with zeros
    df = df.fill_nan(0)

    # Group by "classe" and process each group
    for classe, group in df.group_by("classe"):
        # Select numeric columns and convert to a list of records
        group_numeric = group.select(numeric_columns)
        sequences = group_numeric.to_numpy().tolist()

        grouped_data[classe] = sequences
    
    return grouped_data, max_length


def decode_labels(encoded_data: dict, label_encoders: dict, feature_names: list) -> dict:
    """
    Decode label-encoded features back to their original values.
    Args:
        encoded_data (dict): Dictionary of encoded data.
        label_encoders (dict): Dictionary of fitted LabelEncoders.
        feature_names (list): List of feature names corresponding to the feature indices.
    Returns:
        dict: Decoded data.
    """
    decoded_data = {}
    for classe, sequences in encoded_data.items():
        decoded_sequences = []
        for sequence in sequences:
            decoded_sequence = []
            for i, value in enumerate(sequence):
                feature_name = feature_names[i]
                if feature_name in label_encoders:  # Decode if label-encoded
                    decoded_value = label_encoders[feature_name].inverse_transform([int(value)])[0]
                    decoded_sequence.append(decoded_value)
                else:
                    decoded_sequence.append(value)  # Keep numerical values as-is
            decoded_sequences.append(decoded_sequence)
        decoded_data[classe] = decoded_sequences
    return decoded_data


def load_csv(data_path: str) -> pl.DataFrame:
    schema_overrides = {f"{i:02d}h": pl.Float64 for i in range(1, 25)}  # Add "01h" to "24h"
    
    try:
        df = pl.read_csv(data_path, encoding="utf-8", schema_overrides=schema_overrides)
    except UnicodeDecodeError:
        df = pl.read_csv(data_path, encoding='latin1', schema_overrides=schema_overrides)
    
    return df

def process_data(df: pl.DataFrame, use_last_14_columns: bool = False) -> pl.DataFrame:
    # Drop unnecessary columns
    df = df.drop(["CODI_EOI", "MAGNITUD", "CODI_ENS", "GEOREFERENCIA", "NOM_COMARCA"])

    # Convert columns like "01h", "02h", ..., "24h" to numeric types
    hour_columns = [col for col in df.columns if col.endswith("h")]
    for col in hour_columns:
        df = df.with_columns(pl.col(col).cast(pl.Float64))

    # Label encode categorical columns
    label_encoders = {}
    categorical_columns = ["UNITATS", "TIPUS_ESTACIO", "AREA_URBANA", "CONTAMINANT", "MUNICIPI", "NOM_ESTACIO", "CODI_COMARCA"]
    for col in categorical_columns:
        label_encoders[col] = LabelEncoder()
        df = df.with_columns(pl.Series(col, label_encoders[col].fit_transform(df[col].to_list())))

    # Save label encoders to trace back original labels
    global label_encoders_dict
    label_encoders_dict = label_encoders

    # Convert the "DATA" column to datetime format
    df = df.with_columns(
        pl.col("DATA").str.strptime(pl.Datetime, format="%d/%m/%Y").alias("DATA")
    )

    # Group by "classe" and sort each group by "DATA"
    df = df.sort(["classe", "DATA"])

    # Option to use only last 14 columns
    if use_last_14_columns:
        # Get the last 14 columns (assuming hour columns are the last ones)
        last_14_columns = [col for col in df.columns if col.endswith('h')][-14:]
        
        # Select only these columns along with 'classe' and 'DATA'
        selected_columns = ['classe', 'DATA'] + last_14_columns
        
        # Use only the selected columns, dropping any extras
        df = df.select(pl.col(selected_columns))

    print(df[1])
    print(df.shape)
    return df

def main():
    parser = argparse.ArgumentParser(description='LSTM Sequence Prediction')
    parser.add_argument('--data_path', type=str, help='Path to data')
    parser.add_argument('--use_all', action='store_true', help='Use all sequences for generation')
    parser.add_argument('--use_last_14_columns', action='store_true', help='Use only the last 14 columns')
    args = parser.parse_args()

    # Load and process data
    df = process_data(load_csv(args.data_path), use_last_14_columns=args.use_last_14_columns)
    grouped_sequences, max_length = create_sequences(df)

    # Filter out sequences that are too short
    filtered_sequences = {
        classe: sequences for classe, sequences in grouped_sequences.items() 
        if len(sequences) > 1
    }

    # Create PyTorch Dataset with filtered sequences
    dataset = ClasseDataset(filtered_sequences)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False, collate_fn=collate_fn)
    # split the dataset into training and validation sets
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

    # Create DataLoader with custom collate function
    train_dataloader = DataLoader(train_dataset, batch_size=1, shuffle=False, collate_fn=collate_fn)
    val_dataloader = DataLoader(val_dataset, batch_size=1, shuffle=False, collate_fn=collate_fn)

    # Get input size (number of features)
    input_size = dataset[0][1].shape[1]
    
    # if the model checkpoint exists, load the model
    if os.path.exists("lstm_model.pth") and not args.use_last_14_columns:
        trained_model = LSTMSequencePredictor(input_size=input_size, hidden_size=64, num_layers=2, output_size=input_size)
        trained_model.load_state_dict(torch.load("lstm_model.pth"))
    
    elif os.path.exists("cut_lstm_model.pth") and args.use_last_14_columns:
        trained_model = LSTMSequencePredictor(input_size=14, hidden_size=64, num_layers=2, output_size=14)
        trained_model.load_state_dict(torch.load("cut_lstm_model.pth"))
    else:
        # Train the LSTM model
        trained_model = train_lstm_model(
            train_dataloader, 
            input_size=input_size, 
            hidden_size=64, 
            num_layers=2, 
            epochs=2000
        )

        # save the model
        torch.save(trained_model.state_dict(), "lstm_model.pth")

    # Generate sequences for each class
    for classe, initial_sequence in val_dataloader if not args.use_all else dataloader:
        print(f"\nOriginal Sequence for Classe {classe}:")
        print(initial_sequence)
        
        # Skip very short sequences
        if initial_sequence.size(1) <= 1:
            print(f"Skipping generation for class {classe} due to insufficient sequence length")
            continue
        
        # Generate new sequence
        try:
            generated_sequence = generate_sequence(
                trained_model, 
                initial_sequence, 
                num_steps_to_generate=2
            )
            
            print(f"\nGenerated Sequence for Classe {classe}:")
            # round the generated sequence to integers and discard negative values by assigning 0
            print(generated_sequence.round().clip(min=0))
        except ValueError as e:
            print(f"Error generating sequence for class {classe}: {e}")
        
        break  # Just show one example

if __name__ == '__main__':
    main()