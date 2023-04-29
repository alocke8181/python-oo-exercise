
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Special Word Finder: Subclass of Word Finder that filters out '#' and blank lines"""
    
    def __init__(self, file_path):
        "Initializes the same way as WordFinder"
        super().__init__(file_path)
        self.filterwords()

    def filterwords(self):
        "Internal function to filter blank lines and hashtags from the wordlist"
        self.word_list = [word for word in self.word_list if word != "" or word.startswith("#")]
        self.num_words = len(self.word_list)-1