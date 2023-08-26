class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w)]

    def is_anagram(self, other_word):
        return sorted(self.word.lower()) == sorted(other_word.lower()) and self.word.lower() != other_word.lower()
