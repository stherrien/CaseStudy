from collections import OrderedDict


class ConvertNumbersToWords(object):
    def __init__(self):
        self.high_words = [(1000000000, 'billion'), (1000000, "million"), (1000, "thousand"), (100, "hundred"),
                           (90, "ninety"), (80, "eighty"), (70, "seventy"),
                           (60, "sixty"), (50, "fifty"), (40, "forty"),
                           (30, "thirty")]
        self.low_words = ["twenty", "nineteen", "eighteen", "seventeen",
                          "sixteen", "fifteen", "fourteen", "thirteen",
                          "twelve", "eleven", "ten", "nine", "eight",
                          "seven", "six", "five", "four", "three", "two",
                          "one", "zero"]
        self.words = OrderedDict()
        self.num = 0
        self.max_size = 1999999999
        self.setup_number_words()
        self.prefix = ""

    def setup_number_words(self):
        for (key, val) in self.high_words:
            self.words[key] = val
        for word, n in zip(self.low_words, range(len(self.low_words) - 1, -1, -1)):
            self.words[n] = word

    def convert(self, number):
        try:
            if int(number) < 0:
                self.num = abs(int(number))
                self.prefix = "negative"
            else:
                self.num = int(number)
            if self.num + 1 > self.max_size:
                raise ValueError
        except (TypeError, ValueError) as e:
            return False, "Invalid Input, please try with a Positive or Negative Integer"
        out = self.to_number_word(self.num)
        return True, out if len(self.prefix) == 0 else "%s %s" % (self.prefix, out)

    def to_number_word(self, val):
        words, num = self.filter(self.split_numbers(val))
        return words

    def split_numbers(self, number):
        for item in self.words:
            if item > number:
                continue
            out = []
            div, mod = divmod(number, item) if number != 0 else (1, 0)
            if div == 1:
                out.append((self.words[1], 1))
            else:
                if div == number:
                    print("div == number", div, number)
                    return [(div * self.words[item], div * item)]
                out.append(self.split_numbers(div))
            out.append((self.words[item], item))
            if mod:
                out.append(self.split_numbers(mod))
            return out

    def filter(self, val):
        while len(val) != 1:
            out = []
            left, right = val[:2]
            if isinstance(left, tuple) and isinstance(right, tuple):
                out.append(self.merge(left, right))
                if val[2:]:
                    out.append(val[2:])
            else:
                for item in val:
                    if isinstance(item, list):
                        out.append(item[0]) if len(item) == 1 else out.append(self.filter(item))
                    else:
                        out.append(item)
            val = out
        return out[0]

    @staticmethod
    def merge(left_pair, right_pair):
        left_text, left_number = left_pair
        right_text, right_number = right_pair
        if left_number == 1 and right_number < 100:
            return right_text, right_number
        elif 100 > left_number > right_number:
            return "%s-%s" % (left_text, right_text), left_number + right_number
        elif left_number >= 100 > right_number:
            return "%s and %s" % (left_text, right_text), left_number + right_number
        elif right_number > left_number:
            return "%s %s" % (left_text, right_text), left_number * right_number
        return "%s, %s" % (left_text, right_text), left_number + right_number


if __name__ == '__main__':
    convert_numbers_to_words = ConvertNumbersToWords()
    print(convert_numbers_to_words.convert("876543021"))
    print(convert_numbers_to_words.convert("1000"))
    print(convert_numbers_to_words.convert("14632"))
    print(convert_numbers_to_words.convert("100"))
    print(convert_numbers_to_words.convert("99"))
    print(convert_numbers_to_words.convert("997751076"))
