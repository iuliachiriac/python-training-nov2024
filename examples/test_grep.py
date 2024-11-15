import os
import unittest

from files import grep


class GrepTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lines = [
            "hello world\n",
            "hi there\n",
            "what a wonderful world\n",
            "bye",
        ]
        with open("testfile.txt", "w") as f:
            f.writelines(lines)

    @classmethod
    def tearDownClass(cls):
        os.remove("testfile.txt")

    def test_multiple_matching_lines(self):
        matching_lines = grep("world", "testfile.txt")

        self.assertIsInstance(matching_lines, list)
        self.assertEqual(len(matching_lines), 2)
        self.assertListEqual(matching_lines,
                             ["hello world\n", "what a wonderful world\n"])

    def test_no_matching_lines(self):
        matching_lines = grep("why", "testfile.txt")

        self.assertIsInstance(matching_lines, list)
        self.assertEqual(len(matching_lines), 0)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            grep("why", "nofile.txt")
