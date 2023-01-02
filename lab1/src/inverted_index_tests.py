import unittest
from inverted_index import *

class InvertedIndexTests(unittest.TestCase):
    def test_create_inverted_index_should_create_index_for_files(self):
        self.assertEqual(create_inverted_index({
                             "text4.txt": ["that", "july", "and", "august", "were", "hot", "and", "nahum", "worked", "hard"],
                             "text5.txt": ["in", "february", "the", "mcgregor", "boys", "from", "meadow", "hill", "were", "out", "shooting"]
                         }),
                        {
                            "that": ["text4.txt"],
                            "july": ["text4.txt"],
                            "and": ["text4.txt"],
                            "august": ["text4.txt"],
                            "were": ["text4.txt", "text5.txt"],
                            "hot": ["text4.txt"],
                            "nahum": ["text4.txt"],
                            "worked": ["text4.txt"],
                            "hard": ["text4.txt"],
                            "in": ["text5.txt"],
                            "february": ["text5.txt"],
                            "the": ["text5.txt"],
                            "mcgregor": ["text5.txt"],
                            "boys": ["text5.txt"],
                            "from": ["text5.txt"],
                            "meadow": ["text5.txt"],
                            "hill": ["text5.txt"],
                            "out": ["text5.txt"],
                            "shooting": ["text5.txt"]
                        },
                        "Should build inverted index")

    def test_inverted_index_search_should_find_all_docs_with_word(self):
        self.assertEqual(inverted_index_search({
                            "that": ["text4.txt"],
                            "july": ["text4.txt"],
                            "and": ["text4.txt"],
                            "august": ["text4.txt"],
                            "were": ["text4.txt", "text5.txt"],
                            "hot": ["text4.txt"],
                            "nahum": ["text4.txt"],
                            "worked": ["text4.txt"],
                            "hard": ["text4.txt"],
                            "in": ["text5.txt"],
                            "february": ["text5.txt"],
                            "the": ["text5.txt"],
                            "mcgregor": ["text5.txt"],
                            "boys": ["text5.txt"],
                            "from": ["text5.txt"],
                            "meadow": ["text5.txt"],
                            "hill": ["text5.txt"],
                            "out": ["text5.txt"],
                            "shooting": ["text5.txt"]
                        }, "boys"),
                        ["text5.txt"],
                        "Should return only the document that has the word")

    def test_inverted_index_search_should_return_empty_for_not_found_word(self):
        self.assertEqual(inverted_index_search({
                            "that": ["text4.txt"],
                            "july": ["text4.txt"],
                            "and": ["text4.txt"],
                            "august": ["text4.txt"],
                            "were": ["text4.txt", "text5.txt"],
                            "hot": ["text4.txt"],
                            "nahum": ["text4.txt"],
                            "worked": ["text4.txt"],
                            "hard": ["text4.txt"],
                            "in": ["text5.txt"],
                            "february": ["text5.txt"],
                            "the": ["text5.txt"],
                            "mcgregor": ["text5.txt"],
                            "boys": ["text5.txt"],
                            "from": ["text5.txt"],
                            "meadow": ["text5.txt"],
                            "hill": ["text5.txt"],
                            "out": ["text5.txt"],
                            "shooting": ["text5.txt"]
                        }, "someword"),
                        [],
                        "Should return empty for missing word")

if __name__ == "__main__":
    unittest.main()