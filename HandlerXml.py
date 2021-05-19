import xml.etree.ElementTree as ET

listOfWordsLevel = []

class wordObj:
    wordLang1 = ""
    wordLang2 = ""
    def __init__(self, wordLang1, wordLang2):
        self.wordLang1 = wordLang1
        self.wordLang2 = wordLang2

def loadLevel(lang1, lang2, level):
    listOfWordsLevel.clear()
    tree = ET.parse('ListOfWords.xml')
    root = tree.getroot()

    for word in root.findall('./' + lang1 + '-' + lang2 + '/' + level + '/word'):
        wordsObj = wordObj(word.find(lang1).text,
                           word.find(lang2).text)
        listOfWordsLevel.append(wordsObj)