import unittest
from .numbers_to_words import ConvertNumbersToWords


class WhenConvertingNumbersToWords(unittest.TestCase):

    def test_when_splitting(self):
        converter = ConvertNumbersToWords()
        expected = [('one', 1), ('eighty', 80), [('one', 1), ('seven', 7)]]
        number = 87
        actual = converter.split_numbers(number)
        self.assertEqual(expected, actual)

    def test_when_filtering(self):
        converter = ConvertNumbersToWords()
        expected = ('eighty-seven', 87)
        number = 87
        actual = converter.filter(converter.split_numbers(number))
        self.assertEqual(expected, actual)

    def test_when_merging(self):
        converter = ConvertNumbersToWords()
        expected = 'hundred and eighty-seven'
        number = 187
        actual = converter.merge(('hundred', 100), ('eighty-seven', 87))[0]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
