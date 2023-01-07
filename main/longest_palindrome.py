def is_palindrome(s):
    '''
    :param s: A string input to identify if the string is a palindrome or not
    :return: True if string is palindrome; False otherwise.
    :Algorithm complexity: O(N)
    '''

    for ii in range(len(s) // 2):
        if s[ii] != s[len(s) - 1 - ii]:
            return False

    return True


def get_longest_palindrome_substrings(s):
    '''
    :param s: A string input to identify longest substring palindrome
    :return: A string having one output of longest palindrome
    :Algorithm complexity: O(N^2)
    '''

    if not len(s):
        return ''

    sub_strings = [s[ii:jj] for ii in range(len(s)) for jj in range(ii+1, len(s) + 1)]
    palindrome_substrings = [elem for elem in sub_strings if is_palindrome(elem)]
    length_palindrome_substring = [len(elem) for elem in palindrome_substrings]
    return palindrome_substrings[length_palindrome_substring.index(max(length_palindrome_substring))]


if __name__ == '__main__':

    print(get_longest_palindrome_substrings(''))
    print(get_longest_palindrome_substrings('a'))
    print(get_longest_palindrome_substrings('abcba'))
    print(get_longest_palindrome_substrings('acba'))
    print(get_longest_palindrome_substrings('babad'))
    print(get_longest_palindrome_substrings('cbbd'))

