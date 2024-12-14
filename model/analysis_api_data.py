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
    print(df["tipus_estacio"].head())
    print(df["tipus_estacio"].unique())
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
    print(df["municipi"][0:10])
    for col in df.columns:
        print(f"Column {col} has {df[col].n_unique()} unique values")
    
    with pl.Config(tbl_cols=-1):
        print(df)
    
    # print the unique values of column "municipi"
    print(df["municipi"].unique())
    
    print(df[600000])

    return df

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default='data.csv')
    args = parser.parse_args()
    load_csv(args.data_path)

if __name__ == '__main__':
    main()

    """https://analisi.transparenciacatalunya.cat/resource/44sy-txnv.json"""