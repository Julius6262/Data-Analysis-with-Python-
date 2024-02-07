#!/usr/bin/env python3

def reverse_dictionary(d: dict) -> dict:
    new_dict = {}
    
    for key, value in d.items():
        for word in value:
                if word in new_dict:
                     new_dict[word].append(key)
                else: new_dict[word] = [key]

    
    return new_dict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
