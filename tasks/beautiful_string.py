
VOWELS = ('a', 'e', 'i', 'o', 'u')
TEST_LINES = [
    'aaaaeeeeooooouuuuujjjaaaeeeiiii',
    'aeiou',  # +
    'aaaaaeeeeeeeiiiiiiooooooou'  # +
    'aaeeeeiiiiouuuuu',  # +
    'ooooouuuuaaaaaeeeeeiiiiiiiuuuuooouuu',
    'aeiohasdnksafgjdlsa',
    'dasjkldwunasjkd',
    'njih21793123bj',
    '3213kj21b3k213njkasbnqwi8aaeeeiioousadkpowq93'  # +,
    'aaaaaaaeeeeeeeeiiiiiiiooooooouuuuuudjadsaeiou'  # +
]


class Solution:
    def get_count_and_slice_until_next(self, word):

        vowel = word[0]
        count = 0

        for v in word:
            if vowel != v:
                break
            count += 1

        return count, word[count:]

    def longest_beautiful_substring(self, word: str) -> int:
        length_beautiful_substring = 0
        i = 0
        while True:
            vowel = VOWELS[i]
            count, word = self.get_count_and_slice_until_next(word)
            length_beautiful_substring += count
