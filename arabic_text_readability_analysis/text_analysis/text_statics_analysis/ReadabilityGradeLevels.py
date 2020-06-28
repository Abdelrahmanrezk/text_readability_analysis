import language_tool_python
import nltk
from nltk.corpus import words
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import cmudict
# from spellchecker import SpellChecker
# nltk.download('words')
# nltk.download('cmudict')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
import math
import re
import string
import syllables
from pyphen import Pyphen
d = cmudict.dict()
dic = Pyphen(lang="en")


# tool = language_tool_python.LanguageTool('en-US')

def removePunctuation(text):
    result = ""
 
    for char in text:
        if char in (".",",","!","?","؟","،","\",""/","\"","#","$","%","&","'","(",")","*","+",":",";","<",">","=","[","]","^","_","`","{","}","|","~"):
            continue
        if char in ("-","\n","\r","\t"):
            char=" "
        result+=char
    return result

def removeSpace(text):
    result=""
    for char in text:
        if char in ("-","\n","\r","\t"):
            char=" "
        result+=char
    return result


def removeDigits(text):
    result=""
    for i in text:
        if(i.isdigit()):
            continue
        result+=i
    return result


def characterCount(text):
    count=0
    text=removePunctuation(text)
    text = re.sub('[ًٌٍَُِّْـ]+', '', text)
    for char in text:
        if (char.isdigit() or char.isspace()):
            continue;
        count+=1
    #print("Character Count is ",count)
    return count

def wordCount(text):
    count=0
    text=removePunctuation(text)
    words=word_tokenize(text)
    #print(words)
    for i in words:
        if(i.isdigit()):
            continue;
        count+=1
    #print("Word Count is ",count)
    return count





def nsyl(word):
    try:
        #print(d[word.lower()])
        li=[]
        #print(word,"-",d[word.lower()])
        for x in d[word.lower()][0]:
            for y in x:
                #print(y)
                if(y[-1].isdigit()):
                    li.append(y)
        #print(word,":",len(li))
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
    #print("Count:",count)
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
    text=removePunctuation(text)
    text=removeDigits(text)
    words=word_tokenize(text)
    result=0
    for i in words:
        count=0
        count=nsyl(i)
        if(count==1):
            #print(i)
            result=result+1
    #print(result)
    #print("Single Syllable Words are: ",result)
    return result



def uniqueWordCount(text):
    count=0
    text=removePunctuation(text)
    text=text.lower()
    words=word_tokenize(text)
    uniqueWords=[]
    for i in words:
        if i not in uniqueWords:
            #print(i)
            uniqueWords.append(i)
    for word in uniqueWords:
        if word.isdigit():
            continue;
        count+=1
    #print("Unique Count is ",count)
    return count


def sentenceCount(text):
  count = 0
  text2 = text + "\n"
  text2 = text2.replace(".","\n")
  text2 = text2.replace("!","\n")
  text2 = text2.replace("?","\n")
  text2 = text2.replace("؟","\n")
  lines = text2.split("\n")
  for line in lines:
    line = line.strip()
    if len(line) == 0:
      continue
    count+=1   
    if count == 0:
      count = 1 
  return count


def paragraphCount(text):
    count=  [line.strip() for line in text.split('\n') if len(line.strip()) > 0]
    #print("Paragraph Count is",len(count))
    return len(count)



def count_complex_word(text):
    complex_words = 0
    text=removePunctuation(text)
    for i in text.split(' '):        
        syllable_word = dic.inserted(i)
        syllable_dash = re.findall('-', syllable_word)
        if (len(syllable_dash) >= 2):
            complex_words +=1
    return max(1, complex_words)


def ReadingTime(text):
    word = wordCount(text)
    div_wordCount=word/200
    second,minute=math.modf(div_wordCount)
    second=round((second*0.60),2)
    return (minute+second)





def ReadingTime(text):
    word = wordCount(text)
    div_wordCount = word / 225
    second,minute=math.modf(div_wordCount)
    if second >= 0.60:
      minute +=1
      second-=0.60
    #second=round((second*0.60),2)
    #print("Reading Time is",minute+second);
    return int(minute),int(round(second,2)*100)
 
def SpeakingTime(text):
    word = wordCount(text)
    speakingRate=125
    time=word/speakingRate
    second,minute=math.modf(time)
    if second >= 0.60:
      minute +=1
      second-=0.60
    #second=round((second*0.60),2)
    #print("Reading Time is",minute+second);
    return int(minute),int(round(second,2)*100)


def FKRA(text):
    word = wordCount(text)
    sentence =sentenceCount(text)
    syllable =syllableCount(text) 
    ASL = float(word)/sentence
    ASW = float(syllable)/word
    FKRA = (0.39 * ASL) + (11.8 * ASW) - 15.59
    return round(FKRA,2)

def GFI(text):
    word = wordCount(text)
    sentence = sentenceCount(text)
    c_word = count_complex_word(text)
    GFI = 0.4 * ((float(word) / sentence) + 100 * (float(c_word) / word))
    return round(GFI,2)


def CLI(text):
    text = text.lower()
    char = characterCount(text)
    word = wordCount(text)
    sentence = sentenceCount(text)
    L = (float(char) / word) * 100
    S = (float(sentence) / word) * 100
    CLI = (0.0588 * L) - (0.296 * S) - 15.8
    return round(CLI,2)


def SMOGI(text):
    text = text.lower()
    sentence = sentenceCount(text)
    plosyllable = count_complex_word(text)
    SMOGI = 1.0430 * (math.sqrt(plosyllable * (30 / float(sentence)))) + 3.1291
    return round(SMOGI,2)


def ARI(text):
    text = text.lower()
    char =characterCount(text)
    word = wordCount(text)
    sentence =sentenceCount(text)
    ARI = (4.71 * (float(char) / word)) + (.5 * (float(word) / sentence)- 21.43)
    return round(ARI , 2)


def FORCAST(text):
    syll=singleSyllableWord(text)
    c_word = count_complex_word(text)
    div=round((float(wordCount(text))*10)/150,2)
    GL = 20 - (float(syll)/ div)
    return round(GL,2)

def PSKG(text):
    word = wordCount(text)
    sentence = sentenceCount(text)
    syllable = syllableCount(text)
    ASL = float(word) / sentence
    NS = ((float(syllable)/word) * 0.0455*100) 
    GL = (0.0778 * ASL) + NS - 2.2029
    return round(GL,2)

def RIX(text):
    count = 0
    sentence = sentenceCount(text)
    for x in text.split(" "):
        if characterCount(x) > 4:
            count+=1
    return round(float(count) / sentence,2)   


def FRE(text):
    sentence = sentenceCount(text)
    word = wordCount(text)
    syllable = syllableCount(text)
    ASL = float(word) / sentence
    ASW = float(syllable) / word
    RE = 206.835 - (1.015 * ASL) - (84.6 * ASW)
    return round(RE,1)


def NDC(text):
    c_word = count_complex_word(text)
    word = wordCount(text)
    sentence = sentenceCount(text)
    PDW = round(float(c_word) / word,2)*100
    ASL = float(word) / sentence
    if PDW > 5:
        RS = ((0.1579 * PDW) + (0.0496 * ASL)) + 3.6365
    else:
        RS = (0.1579 * PDW) + (0.0496 * ASL)
    return round(RS,1)


def SPACHE(text):
    c_word = count_complex_word(text)
    word = wordCount(text)
    sentence = sentenceCount(text)
    PDW = round(float(c_word) / word,2)*100
    ASL = float(word) / sentence
    SP = ((0.141 *ASL) + (0.086 * PDW)+0.839)
    return round(SP,1)



#Sentences > 30 Syllables
def s_g_30s(text):
    count =0
    sentence=sent_tokenize(text)
    for x in sentence:
        #print(syllableCount(x))
        if syllableCount(x) > 30:
            count+=1
    return count   


#Sentences > 20 Syllables
def s_g_20s(text):
    count =0
    sentence=sent_tokenize(text)
    for x in sentence:
        #print(syllableCount(x))
        if syllableCount(x) > 20:
            count+=1
    return count   

#Words > 4 Syllables
def w_g_4s(text):
    count =0
    words=word_tokenize(text)
    for x in words:
        #print(syllableCount(x))
        if syllableCount(x) >= 4:
            count+=1
    return count  

#Words > 12 Letters
def w_g_12l(text):
    count =0
    words=word_tokenize(text)
    for x in words:
        #print(len(x))
        if len(x) > 12:
            count+=1
    return count 


# Characters Per Word
def CPW(text):
  WordCount=wordCount(text)
  CharacterCount=characterCount(text)
  CharactersPerWord=round(float(CharacterCount)/WordCount,1)
  return CharactersPerWord


#Syllables Per Word
def SPW(text):
  WordCount=wordCount(text)
  SyllableCount= syllableCount(text)
  SyllablesPerWord=round(float(SyllableCount)/WordCount,1)
  return SyllablesPerWord

#Words Per Sentence
def WPS(text):
  WordCount=wordCount(text)
  SentenceCount=sentenceCount(text)
  WordsPerSentence=round(float(WordCount)/SentenceCount,1)
  return WordsPerSentence
 

#Words Per Paragraph
def WPP(text):
  WordCount=wordCount(text)
  ParagraphCount=paragraphCount(text)
  WordsPerParagraph=round(float(WordCount)/ParagraphCount,1)
  return WordsPerParagraph

#Sentences Per Paragraph
def SPP(text):
  SentenceCount=sentenceCount(text)
  ParagraphCount=paragraphCount(text)
  SentencePerParagraph=round(float(SentenceCount)/ParagraphCount,1)
  return SentencePerParagraph

def w_g_6l(text):
    count =0
    words=word_tokenize(text)
    for x in words:
        #print(len(x))
        if len(x) > 6:
            count+=1
    return count 

def LIX(text):
  WordCount=wordCount(text)
  SentenceCount=sentenceCount(text)
  LongWords=w_g_6l(text)
  percentageOfLongWords=(float(LongWords)/WordCount)*100
  avgLengthOfSentence=float(WordCount)/SentenceCount
  result=round(percentageOfLongWords+avgLengthOfSentence,0)
  return result

def nonWordCount(text):
    regex="[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"    #checks for email address
    #text=removePunctuation(text)
    emails = re.findall("([a-zA-Z0-9]+[\._]?@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
    print("Non word: ",emails)
    return(len(emails))


def LensearWrite(text):
  text=removePunctuation(text)
  words=word_tokenize(text)
  SentenceCount=sentenceCount(text)
  wordcount=wordCount(text)
  #hardword=3
  #easyword=1
  ratio=100/float(wordcount)
  hardword=ratio*3
  easyword=ratio*1
  Score=0
  for word in words:
    if nsyl(word) <= 2:
      Score+=easyword
    if nsyl(word) >=3:
      Score+=hardword
  preResult=(Score/float(SentenceCount))
  if preResult > 20:
    result=round((preResult/2),1)
  else:
    result=round((preResult-2)/2,1)
    
  return result

def take_data_to_shower(text):
    text=removeSpace(text)
    alphanumeric = ""
    for char in text:
        if char ==" ":
            alphanumeric += " "
            continue
        if char.isalnum():
            alphanumeric += char 
    #print(alphanumeric)
    return alphanumeric

def spellingIssues(t):
    text = take_data_to_shower(t)
    wrong =[]
    for w in (text.lower()).split():
        flag = str(w)in words.words()
        if flag == False and w not in wrong:
            wrong.append(w)
    return len(wrong)

def grammarIssues(t):
  matches = tool.check(t)
  return (len(matches))

def isPassive(sentence):
    beforms = ['am', 'is', 'are', 'been', 'was', 'were', 'be', 'being']              
    aux = ['do', 'did', 'does', 'have', 'has', 'had']                                 
    words = nltk.word_tokenize(sentence)
    tokens = nltk.pos_tag(words)
    tags = [i[1] for i in tokens]
    if tags.count('VBN') == 0:                                                           
        return False
    elif tags.count('VBN') == 1 and 'been' in words:                                   
        return False
    else:
        pos = [i for i in range(len(tags)) if tags[i] == 'VBN' and words[i] != 'been']  
        end=pos[0]
        chunk = tags[:end]
        start = 0
        for i in range(len(chunk), 0, -1):
            last = chunk.pop()
            if last == 'NN' or last == 'PRP':
                start = i                                                             
                break
        sentchunk = words[start:end]
        tagschunk = tags[start:end]
        verbspos = [i for i in range(len(tagschunk)) if tagschunk[i].startswith('V')] 
        if verbspos != []:                                                           
            for i in verbspos:
                if sentchunk[i].lower() not in beforms and sentchunk[i].lower() not in aux:  
                    break
            else:
                return True
    return False

def passiveCount(text):
    sentences= nltk.sent_tokenize(text)
    count=0
    for sent in sentences:
        val=isPassive(sent)
        if(val==True):
            count+=1
    return count
 