from text_analysis.text_statics_analysis.indicnlp.tokenize import sentence_tokenize
from text_analysis.text_statics_analysis.indicnlp.tokenize import indic_tokenize
import language_tool_python
import nltk
from nltk.corpus import words
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import cmudict
import math
import re
import string
import syllables
from pyphen import Pyphen
from indicnlp.tokenize import indic_tokenize
# d = cmudict.dict()

def removePunctuationHindi(text):
    result = ""
 
    for char in text:
        if char in (".",",","!","?","؟","،","\",""/","\"","#","$","%","&","'","(",")","*","+",":",";","<",">","=","[","]","^","_","`","{","}","|","~"):
            continue
        if char in ("-","\n","\r","\t"):
            char=" "
        result+=char
    return result

def characterCountHindi(text):
    #sentences=sentence_tokenize.sentence_split(text, lang='hi')
    count=0
    for t in indic_tokenize.trivial_tokenize(text):
        for i in t:
            count=count+1
    return count

def sentenceCountHindi(text):
    #text=removePunctuation(text)
    sentences=sentence_tokenize.sentence_split(text, lang='hi')
    return (len(sentences))

def wordCountHindi(text):
    text=removePunctuationHindi(text)
    text=text.split()
    return(len(text))

def uniqueWordCountHindi(text):
	count=0
	text=removePunctuationHindi(text)
	words=text.split()
	uniqueWords=[]
	for i in words:
	    if i not in uniqueWords:
	        #print(i)
	        uniqueWords.append(i)
	for word in uniqueWords:
	    if word.isdigit():
	        continue;
	    count+=1
	return count


def syllableCountHindi(text):
    count=0
    text=removePunctuationHindi(text)
    words=text.split()
    for i in words:
        count+=syllables.estimate(i)
    return count


def polysyllabicHindi(text):
    count=0
    num_syl=0
    text=removePunctuationHindi(text)
    words=text.split()
    for i in words:
        num_syl=syllables.estimate(i)
        if(num_syl>=2):
            count+=1
    return count

def longWordCountHindi(text):
    words=indic_tokenize.trivial_tokenize(text)
    count=0
    for i in words:
        if len(i)>6:
            count+=1
    return count

def singleSyllableWordHindi(text):
    count=0
    num_syl=0
    text=removePunctuationHindi(text)
    words=text.split()
    for i in words:
        num_syl=syllables.estimate(i)
        if(num_syl==1):
            count+=1
    return count


def paragraphCountHindi(text):
    count=  [line.strip() for line in text.split('\n') if len(line.strip()) > 0]
    #print("Paragraph Count is",len(count))
    return len(count)

def FKRAHindi(text):
    #text = text.lower()
    #text=removePunctuation(text)

    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    syllable =syllableCountHindi(text)
    ASL = word/sentence
    ASW = syllable/word
    FKRA = (0.39 * ASL) + (11.8 * ASW) - 15.59
    return round(FKRA,2)


def GFIHindi(text):
    word = wordCountHindi(text)
    PSW=polysyllabicHindi(text)
    sentence =sentenceCountHindi(text)
    ASL = word/sentence
    #syllable =syllableCount(text)
 
    GFI = 0.4 * ( (ASL) + (PSW))
    return round(GFI,2)

def CLIHindi(text):
    char = characterCountHindi(text)
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    L = (char / word) * 100
    S = (sentence / word) * 100
    CLI = (0.0588 * L) - (0.296 * S) - 15.8
    return round(CLI,2)

def SMOGIHindi(text):
    PSW=polysyllabicHindi(text)
    sentence =sentenceCountHindi(text)
    SMOGI = 1.0430 * (math.sqrt(PSW * (30 / sentence))) + 3.1291
    return round(SMOGI,2)

def ARIHindi(text):
    char = characterCountHindi(text)
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    ARI = (4.71 * (char / word)) + (.5 * (word / sentence)- 21.43)
    return round(ARI , 2)

def FORCASTHindi(text):
    syll=singleSyllableWordHindi(text)
    c_word = polysyllabicHindi(text)
    word = wordCountHindi(text)
    div=round( (word*10)/150,2)
    #print(div)
    GL = 20 - (syll/ div)
    return round(GL,2)

 
def PSKGHindi(text):
    #text=removePunctuation(text)
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    syllable =syllableCountHindi(text)
    ASL = word / sentence
    #NS = (syllable * 0.0455) 
    #GL = (0.0778 * ASL) + NS + 2.7971
    NS = ((syllable/word) * 0.0455*100) 
    GL = (0.0778 * ASL) + NS - 2.2029
    return round(GL,2)
 
def RIXHindi(text):
    count = 0
    sentence =sentenceCountHindi(text)
    for x in text.split(" "):
        #print(characterCount(x))
        if characterCountHindi(text) > 4:
            count+=1
    return round(count / sentence , 2)  

def FREHindi(text):
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    syllable =syllableCountHindi(text)
    ASL = word / sentence
    ASW = syllable / word
    RE=(0.39*ASL)+(11.8*ASW)-15.59
    #RE = 206.835 - (1.015 * ASL) - (84.6 * ASW)
    return round(RE,1)

def NDCHindi(text):
    c_word = polysyllabicHindi(text)
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    PDW = round(c_word / word,2)*100
    ASL = word / sentence
    if PDW > 5:
        RS = ((0.1579 * PDW) + (0.0496 * ASL)) + 3.6365
    else:
        RS = (0.1579 * PDW) + (0.0496 * ASL)
    return round(RS,1)


def SPACHEHindi(text):
    c_word = polysyllabicHindi(text)
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    PDW = round(c_word / word,2)*100
    ASL = word / sentence
    SP = ((0.141 *ASL) + (0.086 * PDW)+0.839)
    return round(SP,1)


def LIXHindi(text):
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    LongWords=longWordCountHindi(text)
    percentageOfLongWords=(LongWords/word)*100
    avgLengthOfSentence=word/sentence
    result=round(percentageOfLongWords+avgLengthOfSentence,0)
    return result

def LensearWriteHindi(text):
    text=removePunctuationHindi(text)
    words=text.split()
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    #hardword=3
    #easyword=1
    ratio=100/word
    hardword=ratio*3
    easyword=ratio*1
    Score=0
    for w in words:
        if syllables.estimate(w) <= 2:
            Score+=easyword
        if syllables.estimate(w) >=3:
            Score+=hardword
    preResult=(Score/sentence)
    if preResult > 20:
        result=round((preResult/2),1)
    else:
        result=round((preResult-2)/2,1)

    return result


def s_g_30Hindi(text):
    count=0
    num_syl=0
    sentences=sentence_tokenize.sentence_split(text, lang='hi')
    for i in sentences:
        if(syllables.estimate(i)>30):
            count+=1
    return count


#Sentences > 20 Syllables
def s_g_20Hindi(text):
    count=0
    num_syl=0
    sentences=sentence_tokenize.sentence_split(text, lang='hi')
    for i in sentences:
        if(syllables.estimate(i)>20):
            count+=1
    return count  



#Words > 4 Syllables
def w_g_4Hindi(text):
    count =0
    words=text.split()
    for x in words:
        if(syllables.estimate(x)>4):
            count+=1
    return count 

#Words > 12 Letters
def w_g_12Hindi(text):
    count =0
    words=text.split()
    for x in words:
        #print(len(x))
        if len(x) > 12:
            count+=1
    return count 


# Characters Per Word
def CPWHindi(text):
    word = wordCountHindi(text)
    char=characterCountHindi(text)
    CharactersPerWord=round(char/word,1)
    return CharactersPerWord

#Syllables Per Word
def SPWHindi(text):
    word = wordCountHindi(text)
    syllable =syllableCountHindi(text)
    SyllablesPerWord=round(syllable/word,1)
    return SyllablesPerWord

 
#Words Per Sentence
def WPSHindi(text):
    word = wordCountHindi(text)
    sentence =sentenceCountHindi(text)
    WordsPerSentence=round(word/sentence,1)
    return WordsPerSentence

#Words Per Paragraph
def WPPHindi(text):
    word = wordCountHindi(text)
    paragraph= paragraphCountHindi(text)
    WordsPerParagraph=round(word/paragraph,1)
    return WordsPerParagraph

#Sentences Per Paragraph
def SPPHindi(text):
    sentence =sentenceCountHindi(text)
    paragraph= paragraphCountHindi(text)
    SentencePerParagraph=round(sentence/paragraph,1)
    return SentencePerParagraph
