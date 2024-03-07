#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def read_lines_from_gzip(file_path, fraction=1.0):
    # Count the total number of lines in the file
    total_lines = 0
    with gzip.open(file_path, "rt", encoding="utf-8") as file:
        for line in file:
            total_lines += 1

    # Read lines from the gzip file, considering only a fraction of them
    lines = []
    with gzip.open(file_path, "rt", encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i >= fraction * total_lines:
                break
            lines.append(line.strip())  # Remove leading/trailing whitespace and newline characters
    return np.array(lines)

def spam_detection(random_state=0, fraction=1.0):
    # Read lines from the ham file
    ham_lines = read_lines_from_gzip("src/ham.txt.gz", fraction)
    
    # Read lines from the spam file
    spam_lines = read_lines_from_gzip("src/spam.txt.gz", fraction)

    # Combine ham and spam lines
    all_lines = np.concatenate((ham_lines, spam_lines))
    
    # Initialize CountVectorizer object to convert text data into a feature matrix
    vec = CountVectorizer()
    
    # Transform text data into a feature matrix
    X = vec.fit_transform(all_lines).toarray()  # Convert to array for better handling
    
    # Create labels: 0 for ham, 1 for spam
    y = np.zeros(len(all_lines))
    y[len(ham_lines):] = 1
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=random_state)
    
    # Initialize and train Multinomial Naive Bayes model
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    # Predict labels for test data
    y_predicted = model.predict(X_test)
    
    # Calculate accuracy of the model
    accuracy = accuracy_score(y_test, y_predicted)
    
    # Count the number of misclassified samples
    misclassified = np.sum(y_test != y_predicted)
    
    # Return accuracy, number of test samples, and number of misclassified samples
    return accuracy, len(X_test), misclassified

def main():
    accuracy, total, misclassified = spam_detection(0,0.1)  # test with fraction 0.1
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
