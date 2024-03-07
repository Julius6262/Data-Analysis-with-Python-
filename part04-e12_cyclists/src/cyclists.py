import pandas as pd

def cyclists():
    # Load the dataset
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Remove empty rows at the end
    df = df.dropna(how='all')

    # Remove columns that contain only missing values
    df = df.dropna(axis=1, how='all')

    

    return df

def main():
    cleaned_data = cyclists()
    print(cleaned_data)

if __name__ == "__main__":
    main()
