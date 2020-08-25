from langdetect import detect
from googletrans import Translator
import nltk
import re

nltk.download('names')
humanNames = [name.lower() for name in nltk.corpus.names.words()]

# Service class for English translation and cleaning
class SentenceNormalizeService:
    def normalize(self, sentence):
        normalizedSentence = self.prepareLinks(sentence)
        normalizedSentence = self.translateToEnglish(normalizedSentence)
        normalizedSentence = normalizedSentence.lower()
        normalizedSentence = self.prepareHumanNames(normalizedSentence)
        normalizedSentence = re.sub(r'[\:\.\!\?]', '', normalizedSentence)
        normalizedSentence = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", ' ', normalizedSentence)
        return normalizedSentence

    def translateToEnglish(self, sentence):
        if sentence == '':
            return ''
        sentenceLang = detect(sentence)
        if sentenceLang == 'en':
            return sentence
        translator = Translator()
        return translator.translate(sentence).text

    def prepareLinks(self, sentence):
        sentenceArr = sentence.split(' ')
        sentenceWithPreparedLinksArr = []
        for word in sentenceArr:
            findedLink = re.search(r'(https?:\/\/[^\s\/]+\/?)', word)
            if findedLink:
                findedLink = findedLink.group(0)
                if re.search('i.imgur.com', findedLink):
                    findedLink = re.search(r'(https?:\/\/[^\s\/]+\/?)', findedLink).group(0)
                sentenceWithPreparedLinksArr.append(re.sub(r'[\/\:\.]', '', findedLink))
            else:
                sentenceWithPreparedLinksArr.append(word)
        return ' '.join(sentenceWithPreparedLinksArr)

    def prepareHumanNames(self, sentence):
        sentenceArr = sentence.split(' ')
        sentenceWithPreparedNamesArr = []
        for word in sentenceArr:
            if word in humanNames:
                sentenceWithPreparedNamesArr.append('NNNAME')
            else:
                sentenceWithPreparedNamesArr.append(word)
        return ' '.join(sentenceWithPreparedNamesArr)
