import polars as pl
import argparse
import re
import numpy as np
from gensim.models import Word2Vec
from scipy.spatial.distance import cosine
from tqdm import tqdm


def tokenize_string(input_string):
    """
    Tokenize a string, removing digits at the end and cleaning tokens.
    
    Args:
        input_string (str): Input string to tokenize
    
    Returns:
        list: List of cleaned tokens
    """
    # Remove any digits from the end
    cleaned = re.sub(r'\d+$', '', input_string)
    
    # Split by spaces and remove empty strings
    tokens = [token.strip() for token in cleaned.split() if token.strip()]
    
    return tokens

def compute_embedding(tokens, model):
    """
    Compute average embedding for a list of tokens.
    
    Args:
        tokens (list): List of tokens
        model (Word2Vec): Trained Word2Vec model
    
    Returns:
        numpy.ndarray or None: Average embedding vector
    """
    # Filter tokens present in the model's vocabulary
    valid_embeddings = [model.wv[token] for token in tokens if token in model.wv]
    
    # Return mean embedding if any valid embeddings exist
    return np.mean(valid_embeddings, axis=0) if valid_embeddings else None

def advanced_matching(df, dfv2):
    """
    Perform advanced matching between df and dfv2 based on multi-token matching.
    
    Args:
        df (pl.DataFrame): First dataframe with 'MUNICIPI' and 'DATA'
        dfv2 (pl.DataFrame): Second dataframe with 'classes' and 'timestamp'
    
    Returns:
        pl.DataFrame: Matched result
    """
    # Prepare municipalities from df
    municipalities = set(df['MUNICIPI'].unique())
    
    # Collect all tokens from both dataframes for Word2Vec training
    all_tokens = []
    
    # Tokenize classes from dfv2
    dfv2_classes_tokens = dfv2['classe'].to_list()
    dfv2_classes_tokens = [tokenize_string(classe) for classe in dfv2_classes_tokens]
    
    # Add municipalities as tokens
    all_tokens.extend([tokenize_string(muni) for muni in municipalities])
    
    # Train Word2Vec model
    model = Word2Vec(
        sentences=all_tokens, 
        vector_size=50, 
        window=5, 
        min_count=1, 
        workers=4
    )
    
    # Prepare results list
    matched_results = []
    
    # Iterate through dfv2 records
    for dfv2_row in tqdm(dfv2.iter_rows(named=True)):
        classes_tokens = tokenize_string(dfv2_row['classe'])
        classes_embedding = compute_embedding(classes_tokens, model)
        
        if classes_embedding is None:
            continue
        
        # Check for municipality match and timestamp match
        for df_row in tqdm(df.iter_rows(named=True)):
            # Check timestamp match
            if df_row['DATA'] != dfv2_row['timestamp']:
                continue
            
            # Check municipality embedding match
            muni_tokens = tokenize_string(df_row['MUNICIPI'])
            muni_embedding = compute_embedding(muni_tokens, model)
            
            if muni_embedding is not None:
                # Compute cosine similarity
                similarity = 1 - cosine(classes_embedding, muni_embedding)
                
                # You can adjust this threshold as needed
                if similarity > 0.7:
                    # Combine row data from both dataframes
                    combined_row = {**df_row, **dfv2_row, 'embedding_similarity': similarity}
                    matched_results.append(combined_row)
    
    # Convert matched results to Polars DataFrame
    if matched_results:
        result_df = pl.DataFrame(matched_results)
        return result_df
    
    return None

def load_csv(data_path: str) -> pl.DataFrame:
    """
    Load CSV file and perform basic preprocessing
    
    Args:
        data_path (str): Path to the CSV file
    
    Returns:
        pl.DataFrame: Processed dataframe
    """
    df = pl.read_csv(data_path)
    
    # Basic preprocessing
    df = df.drop_nulls()
    
    return df

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default='../../qualitat_aire.csv')
    args = parser.parse_args()
    
    # Load primary dataset
    df = load_csv(args.data_path)
    
    # Load second dataset
    try:
        dfv2 = pl.read_csv('../../dades.csv', encoding='utf-8')
    except UnicodeDecodeError:
        dfv2 = pl.read_csv('../../dades.csv', encoding='latin1')
    
    # Perform advanced matching
    matched_result = advanced_matching(df, dfv2)
    
    if matched_result is not None and matched_result.height > 0:
        print(f"Found {matched_result.height} matches.")
        print("\nFirst few matched rows:")
        print(matched_result)
        return matched_result
    else:
        print("No matches found.")
        return None

if __name__ == '__main__':
    main()