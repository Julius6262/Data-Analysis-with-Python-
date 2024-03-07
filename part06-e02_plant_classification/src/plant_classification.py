#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score

def plant_classification():
    iris_data = load_iris()
    # Access the features and target
    x = iris_data.data  # Features (sepal length, sepal width, petal length, petal width)
    y = iris_data.target  # Target (species)
    # test size of 20% and train size of 80%, random_state is seed value.
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)
    
    # Train the Gaussian Naive Bayes model
    model = GaussianNB()
    model.fit(x_train, y_train) 
    # Predict the labels for the test data
    y_pred = model.predict(x_test)
    
    # Calculate the accuracy score
    acc = accuracy_score(y_test, y_pred)
    
    return acc

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
