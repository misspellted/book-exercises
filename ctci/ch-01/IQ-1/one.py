# 1.1
# "Is Unique"
# Implement an algorithm to determine if a string has all unique characters.

# Note: There are no other constraints placed upon the algorithm, except to
# determine uniqueness. Therefore, one might assume the incoming data would
# always contain at least one character, however, that assumption is dangerous
# and incorrect. Always test your input, as this code may be reused in the
# future, and the minimum length assumption may no longer hold true.

# Therefore, I will test two cases before even getting into the algorithm
# proper, in that I will test against a null object reference (None in Python)
# and the empty case string.

# For the null object reference, I will assume that without the ability to
# test the characters of the string, there is no uniqueness to be had, and
# therefore, will return a negative result (False).

# For the empty string scenario, I will follow the same assumption, ignoring
# what might be the implicit \0 character to signify an empty string, as I
# cannot be sure on what platform Python is running (CPython, IPython, ?). As
# such, this scenario will also return a negative result (False).

# I will be breaking my normal code style rule here, and utilize multiple
# return statements, as I think that will keep the code easier to read, versus
# a few .. actually, I could default to False, and prove the unique case...
# Yeah, that'll restore my code style. (-_-) -> d(^_^)b

def isUnique(string):
    unique = False

    # And since that is the default result, we can then select the situation
    # where the two scenarios are NOT in play:
    if not string is None and 0 < len(string):
        # Going to now assume uniqueness is present, and prove otherwise.
        unique = True

        # But how do I know which characters I've seen?
        # I guess I could keep a second string tracking all the characters...
        gnirts = ""

        # So, we obviously need to iterate over the characters in the string.
        for character in string:
            for retcarahc in gnirts:
                # Oh man, this just feels bad... O(N^2) from the get go.. :(

                # Toggle uniqueness if one of the characters is the same.
                unique = retcarahc != character

                # The smallest consolation: At least break out early.
                if not unique:
                    break

            if not unique:
                break

            # Don't forget to add the unqiue character to the tracker.
            gnirts += character

    return unique

import unittest

class TestIsUnique(unittest.TestCase):
    def testWithNullString(self):
        self.assertFalse(isUnique(None))

    def testWithEmptyString(self):
        self.assertFalse(isUnique(""))

    def testWithShortNotUniqueString(self):
        self.assertFalse(isUnique("abcba"))

    def testWithShortUniqueString(self):
        self.assertTrue(isUnique("abc"))

    def testWithShortDecoratedCharactersInString(self):
        self.assertFalse(isUnique("résumé"))

    def testWithSimplePanagramString(self):
        string = "abcdefghijklmnopqrstuvwxyz"

        self.assertTrue(isUnique(string))

    def testWithSpokenPanagramString(self):
        string = "thequickbrownfoxjumpsoverthelazydog"

        self.assertFalse(isUnique(string))

    def testWithMixedCapitalsInString(self):
        string = "THEDOGgothUSducks"

        self.assertTrue(isUnique(string))

    def testWithUniquePunctuationInString(self):
        string = "`~!@#$%^&*()|}{+_-=[]';:<,>.?/"

        self.assertTrue(isUnique(string))

    def testWithCommonPunctuationInString(self):
        string = "~!@#$%^&*()_+{}\\\\"

        self.assertFalse(isUnique(string))

if __name__ == "__main__":
    unittest.main()
