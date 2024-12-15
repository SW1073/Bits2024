import polars as pl
import argparse
import os   


def load_csv(data_path: str) -> pl.DataFrame:
    df = pl.read_csv(data_path)
    print("head", df.head())
    print("schema", df.schema)
    print("Types:", df.dtypes)
    print("Shape, ", df.shape)
    print("Describe", df.describe())
    print("Cols", df.columns)
    print("N UNIQUE", df.n_unique())
    print(df["TIPUS_ESTACIO"].head())
    print(df["TIPUS_ESTACIO"].unique())
    for col in df.columns:
        print(f"Column {col} has {df[col].n_unique()} unique values")
        # scan null values in columns
        print(f"Column {col} has {df[col].null_count()} null values")
        # drop null values in columns
        df = df.drop_nulls(subset=[col])
    
    print("Shape after drop nulls", df.shape)
    print("N UNIQUE after drop nulls", df.n_unique())
    pl.Config.set_fmt_str_lengths(100)
    print(df[0:10])
    print(df["MUNICIPI"][0:10])
    for col in df.columns:
        print(f"Column {col} has {df[col].n_unique()} unique values")
    
    with pl.Config(tbl_cols=-1):
        print(df)
    
    # print the unique values of column "municipi"
    print(df["MUNICIPI"].unique())
    
    print(df[600000])

    return df

def match_with_timestamp(df: pl.DataFrame, dfv2: pl.DataFrame) -> pl.DataFrame:
    # Debugging prints before transformation
    print("DATA column before transformation:")
    print(df["DATA"].head(10))

    # Convert df 'DATA' column to desired format (DD/MM/YYYY)
    df = df.with_columns(
        pl.col("DATA")
        .str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False)  # Correct format for 'YYYY-MM-DD'
        .dt.strftime("%d/%m/%Y")  # Format to desired string representation
        .alias("DATA")
    )

    # Debugging prints after transformation
    print("DATA column after transformation:")
    print(df["DATA"].head(10))

    # Ensure unique rows for 'DATA' by taking the first occurrence of each unique value
    df = df.group_by("DATA").first()

    # Debugging prints after ensuring uniqueness
    print("DATA column after ensuring uniqueness:")
    print(df["DATA"].head(10))

    # Debugging prints for dfv2 timestamp column
    print("timestamp column of dfv2:")
    print(dfv2["timestamp"].head(10))

    # Join df and dfv2 on the 'DATA' column
    result = df.join(dfv2, left_on="DATA", right_on="timestamp", how="inner")

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default='../../qualitat_aire.csv')
    args = parser.parse_args()
    df = load_csv(args.data_path)
    try:
        dfv2 = pl.read_csv('../../dades.csv', encoding='utf-8')
    except UnicodeDecodeError:
        dfv2 = pl.read_csv('../../dades.csv', encoding='latin1')
        
    result = match_with_timestamp(df, dfv2)
    print(result)
    print(result.columns)
    print(result["classe"][0:15])
    print(result["DATA"][0:15])
    # save the result to a csv file
    result.write_csv("result.csv")
if __name__ == '__main__':
    main()

    """https://analisi.transparenciacatalunya.cat/resource/44sy-txnv.json"""