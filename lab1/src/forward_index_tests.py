import unittest
from forward_index import *

class ForwardIndexTests(unittest.TestCase):
    def test_create_forward_index_should_create_index_for_files(self):
        self.assertEqual(create_forward_index({
                             "text4.txt": ["that", "july", "and", "august", "were", "hot", "and", "nahum", "worked", "hard"],
                             "text5.txt": ["in", "february", "the", "mcgregor", "boys", "from", "meadow", "hill", "were", "out", "shooting"]
                         }),
                         {
                             "text4.txt": ["and", "august", "hard", "hot", "july", "nahum", "that", "were", "worked"],
                             "text5.txt": ["boys", "february", "from", "hill", "in", "mcgregor", "meadow", "out", "shooting", "the", "were"]
                         },
                        "Should build forward index")

    def test_forward_index_search_should_find_all_docs_with_word(self):
        self.assertEqual(forward_index_search({
                             "text4.txt": ["and", "august", "hard", "hot", "july", "nahum", "that", "were", "worked"],
                             "text5.txt": ["boys", "february", "from", "hill", "in", "mcgregor", "meadow", "out", "shooting", "the", "were"]
                         }, "boys"),
                        ["text5.txt"],
                        "Should return only the document that has the word")

    def test_forward_index_search_should_return_empty_for_not_found_word(self):
        self.assertEqual(forward_index_search({
                             "text4.txt": ["and", "august", "hard", "hot", "july", "nahum", "that", "were", "worked"],
                             "text5.txt": ["boys", "february", "from", "hill", "in", "mcgregor", "meadow", "out", "shooting", "the", "were"]
                         }, "someword"),
                        [],
                        "Should return empty for missing word")

if __name__ == "__main__":
    unittest.main()
