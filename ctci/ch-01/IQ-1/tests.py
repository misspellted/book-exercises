# This file provides the collection of tests to run agains the isUnique
# method defined, accepting a string argument to be used in a test.

# It is expected that these tests be inserted into the file containing the
# version of the algorithm being tested, after trying various attempts to
# mess around with importing this file instead.

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
