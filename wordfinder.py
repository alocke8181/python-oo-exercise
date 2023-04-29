"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Class to pick a random word from a file

    >>> wf = WordFinder("words.txt")
    235887 words read

    >>> wf.random() in wf.word_list
    True

    >>> wf.random() in wf.word_list
    True

    >>> wf.random() in wf.word_list
    True

    """
    def __init__(self, file_path):
        "Initalizes a WordFinder based on a filepath"
        self.file_path = file_path
        self.word_list = self.loadwords()
        self.num_words = len(self.word_list)-1

    def loadwords(self):
        "Private function to load the words from the given file"
        file = open(self.file_path, "r")
        word_lines = file.readlines()
        word_list = [line.split("\n")[0] for line in word_lines]
        print(f"{len(word_list)} words read")
        return word_list

    def random(self):
        "Retrieves a random word from the given list"
        rand_num = random.randint(0,self.num_words)
        return self.word_list[rand_num]

