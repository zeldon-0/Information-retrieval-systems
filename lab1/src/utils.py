from pathlib import Path
import string

def load_text(file_name):
    text = Path(file_name).read_text()
    return text

def retrieve_words(input):
    unformatted_text = input.translate(str.maketrans('', '', string.punctuation))
    return unformatted_text.lower().split()

def aggregate_documents(document_paths):
    documents = {}
    for document in document_paths:
        documents[document.split('/')[-1]] = retrieve_words(load_text(document))
    return documents


if __name__ == "__main__":
    print(aggregate_documents(["../data/text1.txt", "../data/text2.txt", "../data/text3.txt"]))