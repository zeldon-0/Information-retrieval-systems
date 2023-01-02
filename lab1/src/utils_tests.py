import unittest
from utils import *


class UtilsTests(unittest.TestCase):
    def test_retrieve_words_should_split_string_into_words_for_index(self):
        self.assertEqual(retrieve_words("It is not because of anything that can be seen or heard or handled, but because of something that is imagined."),
                        [ "it", "is", "not", "because", "of", "anything", "that", "can", "be", "seen", "or", "heard", "or", "handled", "but", "because", "of", "something", "that", "is", "imagined"],
                        "Should split the string into separate words")

    def test_aggregate_documents_should_create_documents_dictionary(self):
        self.assertEqual(aggregate_documents(["../data/text4.txt", "../data/text5.txt"]),
                         {
                             "text4.txt": ["that", "july", "and", "august", "were", "hot", "and", "nahum", "worked", "hard"],
                             "text5.txt": ["in", "february", "the", "mcgregor", "boys", "from", "meadow", "hill", "were", "out", "shooting"]
                         },
                        "Should collect the file contents and split the strings into separate words for each document")


if __name__ == "__main__":
    unittest.main()