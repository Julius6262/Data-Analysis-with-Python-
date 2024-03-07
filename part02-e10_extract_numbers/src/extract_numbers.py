def extract_numbers(s):
    numbers = []
    words = s.split()
    for word in words:
        try:
            num = int(word)
        except ValueError:
            try:
                num = float(word)
            except ValueError:
                # If word is not a number, skip it
                continue
        numbers.append(num)
    return numbers


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
