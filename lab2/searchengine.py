from common_elements import *
from pathlib import Path
import string
import os

def load_text(file_name):
    file_path = "./data/" + file_name
    if os.path.exists(file_path ) and os.path.getsize(file_path ) > 0:
        text = Path(file_path).read_text()
        return text

    return ""


def retrieve_words(input):
    words_with_punctuation = input.lower().split()
    result = []
    for word in words_with_punctuation:
        word_without_punctuation = word.strip(string.punctuation)
        if len(word_without_punctuation) > 0:
            result.append(word_without_punctuation)

    return result


def create_index(file_names, index, file_titles):
    for file_name in file_names:
        file_text = load_text(file_name)
        if file_text != "":
            file_titles[file_name] = file_text.split('\n')[0]

            words = retrieve_words(file_text)
            for word in words:
                if word not in index:
                    index[word] = [file_name]
                elif file_name not in index[word]:
                    index[word].append(file_name)

def search(index, query):
    words = query.split()
    result = None

    for word in words:
        if result is None:
            result = search_single_word(index, word)
        else:
            result = common(result, search_single_word(index, word))

    return result

def search_single_word(index, word):
    if word in index:
        return index[word]
    return []

def format_response(search_result, file_titles):
    if len(search_result) == 0:
        return "Could not find any files that match the prompt"

    result_string = ""
    for i,file in enumerate(search_result):
        file_title = file_titles[file]
        result_string = f"{result_string}{i}. File title: {file_title}; File name:  {file} \n"

    return result_string

def main():
    file_names = ["text1.txt", "text2.txt", "text3.txt"]
    index = {}
    file_titles = {}

    create_index(file_names, index, file_titles)

    while True:
        prompt = input("Awaiting user prompt for the search...\n")

        if len(prompt) == 0:
            return

        search_result = search(index, prompt)
        print(format_response(search_result, file_titles))

if __name__ == "__main__":
    main()


