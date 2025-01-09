def main():
    file = "books/frankenstein.txt"
    text = read(file)
    print(text)
    print(f"--- Begin report of {file} ---")
    print(f"Total number of words in the document is: {countWords(text)}.")
    countLetters(text)


def read(path):
    with open(path) as f:
        return f.read()

def countWords(words):
    return len(words.split())

def countLetters(text):
    file = "books/frankenstein.txt"
    textLower = text.lower()
    letterCount = {}
    for c in text:
        if c in letterCount:
            letterCount[c] += 1
        else:
            letterCount[c] = 1

    for letter in letterCount:
        print(f"The '{letter}' character was found {letterCount[letter]} times in the document.")
    print("--- End of Report ---")

main()