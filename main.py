def main():
    text = read("books/frankenstein.txt")
    print(text)
    print(f"Total number of words is: {countWords(text)}.")


def read(path):
    with open(path) as f:
        return f.read()

def countWords(words):
    return len(words.split())

main()