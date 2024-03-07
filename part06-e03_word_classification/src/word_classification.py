#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.model_selection import KFold

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):  # one dimensional np.array
    # Initialize an empty list to store feature vectors for each word
    feature_matrix = []

    # Iterate over each word in the input array
    for word in a:
        # Initialize a feature vector for the current word
        word_features = [0] * len(alphabet)

        # Iterate over each character in the word
        for letter in word:
            # Check if the character is in the alphabet
            if letter in alphabet_set:
                # Increment the count for the corresponding letter in the feature vector
                index = alphabet.index(letter)
                word_features[index] += 1

        # Append the feature vector to the feature matrix
        feature_matrix.append(word_features)

    # Convert the feature matrix to a NumPy array and return it
    return np.array(feature_matrix)


def contains_valid_chars(s):  # string
    for letter in s:
        if not letter in alphabet_set:
            return False
    return True

def get_features_and_labels():
    # Load Finnish words
    finnish = load_finnish()
    # Convert all Finnish words to lowercase
    finnish = [word.lower() for word in finnish]

    # Filter out Finnish words containing invalid characters
    finnish = [word for word in finnish if contains_valid_chars(word)]

    # Load English words
    english = load_english()
    # Filter out English words starting with an uppercase letter
    english = [word for word in english if word[0].islower()]

    # Convert all English words to lowercase
    english = [word.lower() for word in english]

    # Filter out English words containing invalid characters
    english = [word for word in english if contains_valid_chars(word)]

    # Generate feature matrices for Finnish and English words
    finnish_features = get_features(finnish)
    english_features = get_features(english)

    # Concatenate feature matrices
    X = np.concatenate((finnish_features, english_features))

    # Generate target labels (0 for Finnish, 1 for English)
    y = np.zeros(len(finnish) + len(english))
    y[len(finnish):] = 1

    return X, y



def word_classification():
    # Obtain feature matrix X and target labels y
    X, y = get_features_and_labels()

    # Initialize Multinomial Naive Bayes classifier
    clf = MultinomialNB()

    # Perform 5-fold cross-validation and get accuracy scores
    kf = KFold(n_splits=5, shuffle=True, random_state=0)
    cv_scores = cross_val_score(clf, X, y, cv=kf)

    return cv_scores

def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()