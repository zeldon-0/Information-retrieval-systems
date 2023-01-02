from utils import *


def create_forward_index(documents):
    forward_index = {}

    for document in documents:
        document_words = []
        for word in documents[document]:
            if word not in document_words:
                document_words.append(word)

        document_words.sort()
        forward_index[document] = document_words

    return forward_index


def forward_index_search(index, word):
    documents = []
    for document in index:
        if word in index[document]:
            documents.append(document)

    documents.sort()
    return documents


if __name__ == "__main__":
    documents = aggregate_documents(["../data/text1.txt", "../data/text2.txt", "../data/text3.txt"])

    forward_index = create_forward_index(documents);

    print("Forward index:" + str(forward_index))

    print("Search result for `only`:" + str(forward_index_search(forward_index, "only")))