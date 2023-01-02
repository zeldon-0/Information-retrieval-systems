from utils import *


def create_inverted_index(documents):
    inverted_index = {}

    for document in documents:
        for word in documents[document]:
            if word not in inverted_index:
                inverted_index[word] = [ document ]
            elif document not in inverted_index[word]:
                inverted_index[word].append(document)

    for word in inverted_index:
        inverted_index[word].sort()

    return inverted_index


def inverted_index_search(index, word):
    if word in index:
        return index[word]

    return []

if __name__ == "__main__":
    documents = aggregate_documents(["../data/text1.txt", "../data/text2.txt", "../data/text3.txt"])

    inverted_index = create_inverted_index(documents)

    print("Inverted index:" + str(inverted_index))

    print("Search result for `only`:" + str(inverted_index_search(inverted_index, "only")))