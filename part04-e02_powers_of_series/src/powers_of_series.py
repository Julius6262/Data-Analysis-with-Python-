
import pandas as pd

def powers_of_series(s, k):
    data = {}

    for n in range(1, k + 1):
        data[n] = s ** n

    df = pd.DataFrame(data)
    return df

def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 3))

if __name__ == "__main__":
    main()