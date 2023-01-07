import unittest
from main.longest_palindrome import is_palindrome, get_longest_palindrome_substrings


class LongestPalindromeTest(unittest.TestCase):
    def test_is_palindrome(self):

        self.assertEqual(is_palindrome('a'), True)
        self.assertEqual(is_palindrome('ab'), False)
        self.assertEqual(is_palindrome('abc'), False)
        self.assertEqual(is_palindrome('abba'), True)
        self.assertEqual(is_palindrome('abcba'), True)


    def test_longest_palindrome(self):

        self.assertEqual(get_longest_palindrome_substrings('a'), 'a')
        self.assertIn(get_longest_palindrome_substrings('babad'), ['bab','aba'])
        self.assertEqual(get_longest_palindrome_substrings('cbbd'), 'bb')
        self.assertEqual(get_longest_palindrome_substrings('abcba'), 'abcba')
        self.assertEqual(get_longest_palindrome_substrings(''), '')


if __name__ == '__main__':
    unittest.main()
