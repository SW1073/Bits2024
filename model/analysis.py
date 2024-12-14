import argparse
import os
import polars as pl
import matplotlib.pyplot as plt

def analyse_data(data_path: str):
    try:
        df = pl.read_csv(data_path, encoding = "utf-8")
    except UnicodeDecodeError:
        df = pl.read_csv(data_path, encoding = 'latin1')

    print(df.describe())
    print(df.schema)
    print(df.head())
    print(df.shape)
    print(df.n_chunks())
    print(df.columns)
    print(df.dtypes)
    print(df.count())
    print(df.is_duplicated())
    print(df.is_unique())
    print(df.min())
    print(df.max())
    print(df.sum())
    print(df.mean())
    print(df.median())
    print(df.std())
    print(df.var())
    print(df.quantile(0.5))
    print(df.quantile(0.25))
    print(df.quantile(0.75))
    print(df.unique())
    print(df.n_unique())

def main():
    parser = argparse.ArgumentParser(description='Analyse data')
    parser.add_argument('--data_path', type=str, help='Path to data')
    args = parser.parse_args()
    analyse_data(args.data_path)

if __name__ == '__main__':
    main()


