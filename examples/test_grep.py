import unittest

from files import grep


class GrepTestCase(unittest.TestCase):
    def test_multiple_matching_lines(self):
        lines = [
            "hello world\n",
            "hi there\n",
            "what a wonderful world\n",
            "bye",
        ]
        with open("testfile.txt", "w") as f:
            f.writelines(lines)

        matching_lines = grep("world", "testfile.txt")

        self.assertIsInstance(matching_lines, list)
        self.assertEqual(len(matching_lines), 2)
        self.assertListEqual(matching_lines,
                             ["hello world\n", "what a wonderful world\n"])