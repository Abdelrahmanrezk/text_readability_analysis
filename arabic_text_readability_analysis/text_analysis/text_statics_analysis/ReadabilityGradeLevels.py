import math
import re
import string
import syllables
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tokenize import sent_tokenize,word_tokenize
from pyphen import Pyphen
dic = Pyphen(lang="en")


def removePunctuation(text):
    result = ""

    for char in text:
        if char in (".",",","!","?","؟","\n","\r","\t","،","\",""/","\"","#","$","%","&","'","(",")","*","+","-",":",";","<",">","=","@","[","]","^","_","`","{","}","|","~"):
            continue
        result+=char
    return result


def characterCount(text):
    count=0
    text=removePunctuation(text)
    for char in text:
        if (char.isdigit() or char.isspace()):
            continue;
        count+=1
    return count




def wordCount(text):
    count=0
    text=removePunctuation(text)
    words=word_tokenize(text)
    for i in words:
        if(i.isdigit()):
            continue;
        count+=1
    return count


def count_complex_word(text):
    complex_words = 0
    for i in text.split(' '):        
        syllable_word = dic.inserted(i)
        syllable_dash = re.findall('-', syllable_word)
        if len(syllable_dash) >= 2:
            complex_words +=1
    return max(1, complex_words)


def nsyl(word):
    try:
        li=[]
        for x in d[word.lower()][0]:
            for y in x:
                #print(y)
                if(y[-1].isdigit()):
                    li.append(y)
        return(len(li))
    except:
    	#if word not found in cmudict
        return(syllables(word))


def syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels:
            if word[index-1] not in vowels:
                count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return count


def syllableCount(text):
    count=0
    num=0
    text=removePunctuation(text)
    words=word_tokenize(text)
    #print(words)
    for i in words:
        count=count+nsyl(i)
    return(count)


def singleSyllableWord(text):
    words=word_tokenize(text)
    result=0
    for i in words:
        count=0
        count=nsyl(i)
        if(count==1):
            result=result+1
    return result


def uniqueWordCount(text):
    count=0
    text=removePunctuation(text)
    text=text.lower()
    words=word_tokenize(text)
    uniqueWords=[]
    for i in words:
        if i not in uniqueWords:
            uniqueWords.append(i)
    for word in uniqueWords:
        if word.isdigit():
            continue;
        count+=1
    return count

def sentenceCount(text):
    sentence=sent_tokenize(text)
    count=len(sentence)
    return count



def paragraphCount(text):
    count=  [line.strip() for line in text.split('\n') if len(line.strip()) > 0]
    return len(count)

def ReadingTime(text):
    word = wordCount(text)
    div_wordCount=word/200
    second,minute=math.modf(div_wordCount)
    second=round((second*0.60),2)
    return (minute+second)


def SpeakingTime(text):
    word = wordCount(text)
    speakingRate=125
    time=word/speakingRate
    second,minute=math.modf(time)
    second=round(second*0.60,2)
    return (minute+second)

def FKRA(txt):
    word = wordCount(txt)
    sentence =sentenceCount(txt)
    syllable =syllableCount(txt) 
    ASL = word/sentence
    ASW = syllable/word
    FKRA = (0.39 * ASL) + (11.8 * ASW) - 15.59
    return round(FKRA,2)

def GFI(txt):
    txt = txt.lower()
    word = wordCount(txt)
    sentence = sentenceCount(txt)
    c_word = count_complex_word(txt)
    GFI = 0.4 * ((word / sentence) + 100 * (c_word / word))
    return round(GFI,2)


def CLI(txt):
    txt = txt.lower()
    char = characterCount(txt)
    word = wordCount(txt)
    sentence = sentenceCount(txt)
    L = (char / word) * 100
    S = (sentence / word) * 100
    CLI = (0.0588 * L) - (0.296 * S) - 15.8
    return round(CLI,2)

def SMOGI(txt):
    txt = txt.lower()
    sentence = sentenceCount(txt)
    plosyllable = count_complex_word(txt)
    SMOGI = 1.0430 * (math.sqrt(plosyllable * (30 / sentence))) + 3.1291
    return round(SMOGI,2)

def ARI(txt):
    txt = txt.lower()
    char =characterCount(txt)
    word = wordCount(txt)
    sentence =sentenceCount(txt)
    ARI = (4.71 * (char / word)) + (.5 * (word / sentence)- 21.43)
    return round(ARI , 2)


def FORCAST(txt):
    syllable =syllableCount(txt)
    syll=singleSyllableWord(txt)
    c_word = count_complex_word(txt)
    GL = 25 - (syll/ 10)
    return round(GL,2)

def PSKG(txt):
    #txt = txt.lower()
    word = wordCount(txt)
    sentence = sentenceCount(txt)
    syllable = syllableCount(txt)
    ASL = word / sentence
    NS = ((syllable /word) * 0.0455) * 100
    GL = (0.0778 * ASL) + NS - 2.2029
    return round(GL,2)



