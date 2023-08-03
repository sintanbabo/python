print('decorators')
print('='*60)

class WordSet:
    replacePuncs = ['!','.',',','\'']

    def __init__(self):
        self.words = set()

    # instance method
    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    @staticmethod
    def cleanText(text):
        # chaining functions
        for punc in WordSet.replacePuncs:
            text = text.replace(punc,'')
        return text.lower()

wordSet = WordSet()

wordSet.addText('Hi, I\'m gh.park! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
