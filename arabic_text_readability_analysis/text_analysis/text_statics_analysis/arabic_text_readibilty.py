from os.path import isfile, join
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import re
import requests, time
import ast
import math
url = 'https://farasa-api.qcri.org'

scaler = MinMaxScaler()



############-----------------syllables--------------------##############


def arabic_syllables(word):
    #fatha, damma, kasra
    tashkeel = ['\u064E','\u064F','\u0650']
 
    count_long = 0
    count_short = 0
    count_stress = 0
 
    for x in range(0,len(tashkeel)):
        for i in range(0, len(word)):
            if word[i] == tashkeel[x]:
                if i+1 < len(word):
                    #to count long syllables we need to check if the character following is an alef, waw or yaaA.
                    if word[i+1]=='\u0627' or word[i+1]=='\u0648' or word[i+1]=='\u064a':
                        count_long += 1
                    else:
                        count_short += 1
                else:
                    count_short += 1
 
    #counts stress syllables, those tanween fatih, tanween damm, tanween kasr and shadda.
    count_stress = word.count("\u064B") + word.count("\u064C") + word.count("\u064D") + word.count("\u0651")
    #syllables_count = count_short + (2 * count_long) + (2 * count_stress)
    syllables_count = count_short +  count_long +  count_stress
    return syllables_count


def arabic_syllables_count(text):
  words = text.split(" ")
  count = 0
  for i in words:
    count = count+arabic_syllables(i)
  return count  

def arabic_singleSyllableWord(text):
    words=word_tokenize(text)
    result=0
    for i in words:
        count=0
        count=arabic_syllables(i)
        if(count==1):
            result=result+1
    return result

def arabic_count_complex_word(text):
    complex_words = 0
    for i in text.split(' '):        
        syllable_count = arabic_syllables(i)
        if (syllable_count >= 4):
            complex_words +=1
    #print("Complex Word Count is ",complex_words)
    return max(1, complex_words)



def arabic_removePunctuation(text):
    result = ""

    for char in text:
        if char in (".",",","!","?","؟","،","\",""/","\"","#","$","%","&","'","(",")","*","+",":",";","<",">","=","[","]","^","_","`","{","}","|","~"):
            continue
        if char in ("-","\n","\r","\t"):
            char=" "
        if(char.isdigit()):
            continue    
        result+=char
    #result = re.sub('[ًٌٍَُِّْـ]+', '', result)    
    return result



def arabic_characterCount(text):
    count=0
    text=arabic_removePunctuation(text)
    text = re.sub('[ًٌٍَُِّْـ]+', '', text)
    for char in text:
        if (char.isdigit() or char.isspace()):
            continue;
        count+=1
    #print("Character Count is ",count)
    return count

def arabic_uniqueWordCount(text):
    count=0
    text=arabic_removePunctuation(text)
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
    
# def arabic_wordCount(text):
#     count=0
#     words=word_tokenize(text)
#     #print(words)
#     for i in words:
#         #hamdy: if(i.isdigit()):
#         #Hamdy    continue;
#         count+=1
#     #print("Word Count is ",count)
    
#     #Hamdy
#     if count == 0:
#         count = 1 # if input = "4 " -> method gives division by zero!
#     return count

def arabic_wordCount(text):
    count=0
    text=arabic_removePunctuation(text)
    words=word_tokenize(text)
    #print(words)
    for i in words:
        if(i.isdigit()):
            continue;
        count+=1
    #print("Word Count is ",count)
    return count



def arabic_sentenceCount(text):
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

def arabic_paragraphCount(text):
    count=  [line.strip() for line in text.split('\n') if len(line.strip()) > 0]
    #print("Paragraph Count is",len(count))
    return len(count)





############-----------------Readability Grade Levels--------------------##############

def arabic_FKRA(text):
    word = arabic_wordCount(text)
    sentence =arabic_sentenceCount(text)
    syllable =arabic_syllables_count(text) 
    ASL = word/sentence
    ASW = syllable/word
    FKRA = (0.39 * ASL) + (11.8 * ASW) - 15.59
    return round(FKRA,2)

def arabic_GFI(text):
    word = arabic_wordCount(text)
    sentence = arabic_sentenceCount(text)
    c_word = arabic_count_complex_word(text)
 
    GFI = 0.4 * ((word / sentence) + 100 * (c_word / word))
    return round(GFI,2)


def arabic_CLI(text):
    char = arabic_characterCount(text)
    word = arabic_wordCount(text)
    sentence = arabic_sentenceCount(text)
    L = (char / word) * 100
    S = (sentence / word) * 100
    CLI = (0.0588 * L) - (0.296 * S) - 15.8
    return round(CLI,2)

def arabic_SMOGI(text):
    sentence = arabic_sentenceCount(text)
    plosyllable = arabic_count_complex_word(text)
    SMOGI = 1.0430 * (math.sqrt(plosyllable * (30 / sentence))) + 3.1291
    return round(SMOGI,2)


def arabic_ARI(text):
    char =arabic_characterCount(text)
    word = arabic_wordCount(text)
    sentence =arabic_sentenceCount(text)
    ARI = (4.71 * (char / word)) + (.5 * (word / sentence)- 21.43)
    return round(ARI , 2)




def arabic_FORCAST(text):
    syll=arabic_singleSyllableWord(text)
    c_word = arabic_count_complex_word(text)
    div=round( (arabic_wordCount(text)*10)/150,2)
    #print(div)
    GL = 20 - (syll/ div)
    return round(GL,2)


def arabic_PSKG(text):
    word = arabic_wordCount(text)
    sentence = arabic_sentenceCount(text)
    syllable = arabic_syllables_count(text)
    ASL = word / sentence
    NS = ((syllable/word) * 0.0455*100) 
    GL = (0.0778 * ASL) + NS - 2.2029
    return round(GL,2)

def arabic_RIX(text):
    count = 0
    sentence = arabic_sentenceCount(text)
    for x in text.split(" "):
        if arabic_characterCount(x) > 4:
            count+=1
    return round(count / sentence , 2) 

def arabic_FRE(text):
    sentence = arabic_sentenceCount(text)
    word = arabic_wordCount(text)
    syllable = arabic_syllables_count(text)
    ASL = word / sentence
    ASW = syllable / word
    RE = 206.835 - (1.015 * ASL) - (84.6 * ASW)
    return round(RE,1)

def arabic_NDC(text):
    c_word = arabic_count_complex_word(text)
    word = arabic_wordCount(text)
    sentence = arabic_sentenceCount(text)
    PDW = round(c_word / word,2)*100
    ASL = word / sentence
    if PDW > 5:
        RS = ((0.1579 * PDW) + (0.0496 * ASL)) + 3.6365
    else:
        RS = (0.1579 * PDW) + (0.0496 * ASL)
    return round(RS,1)

def arabic_SPACHE(text):
    c_word = arabic_count_complex_word(text)
    word = arabic_wordCount(text)
    sentence = arabic_sentenceCount(text)
    PDW = round(c_word / word,2)*100
    ASL = word / sentence
    SP = ((0.141 *ASL) + (0.086 * PDW)+0.839)
    return round(SP,1)  

def arabic_spellingIssues(text):
   res = arabic_SpCH(text)
   count = 0
   for i in res:
     if i == '/':
       count +=1
   return count




def arabic_ReadingTime(text):
    word = arabic_wordCount(text)
    div_wordCount=float(word)/110
    second,minute=math.modf(div_wordCount)
    if second >= 0.60:
      minute +=1
      second-=0.60
    #second=round((second*0.60),2)
    #print("Reading Time is",minute+second);
    return int(minute),int(round(second,2)*100)

def arabic_SpeakingTime(text):
    word = arabic_wordCount(text)
    speakingRate=84
    time=word/speakingRate
    second,minute=math.modf(time)
    if second >= 0.60:
      minute +=1
      second-=0.60
    #second=round((second*0.60),2)
    #print("Reading Time is",minute+second);
    return int(minute),int(round(second,2)*100)
#---------------------------Sentences >  Syllables--------------------------------

#Sentences > 30 Syllables
def arabic_s_g_30s(text):
    count =0
    sentence=sent_tokenize(text)
    for x in sentence:
        #print(syllableCount(x))
        if arabic_syllables_count(x) > 30:
            count+=1
    return count    

#Sentences > 20 Syllables
def arabic_s_g_20s(text):
    count =0
    sentence=sent_tokenize(text)
    for x in sentence:
        #print(syllableCount(x))
        if arabic_syllables_count(x) > 20:
            count+=1
    return count


def arabic_w_g_12l(txt):
    count =0
    words=word_tokenize(txt)
    for x in words:
        if len(x) > 12:
            count+=1
    return count
 
#Words > 4 Syllables
def arabic_w_g_4s(text):
    count =0
    words=word_tokenize(text)
    for x in words:
        #print(syllableCount(x))
        if arabic_syllables(x) >= 4:
            count+=1
    return count  



#------------------------------- Words or other Per Sentence or other

 
#Syllables Per Word
def arabic_SPW(text):
  WordCount=arabic_wordCount(text)
  SyllableCount= arabic_syllables_count(text)
  SyllablesPerWord=round(SyllableCount/WordCount,1)
  return SyllablesPerWord



#Words Per Sentence
def arabic_WPS(text):
    WordCount=arabic_wordCount(text)
    SentenceCount=arabic_sentenceCount(text)
    WordsPerSentence=round(WordCount/SentenceCount,1)
    return WordsPerSentence

#Words Per Paragraph
def arabic_WPP(text):
    WordCount=arabic_wordCount(text)
    ParagraphCount=arabic_paragraphCount(text)
    WordsPerParagraph=round(WordCount/ParagraphCount,1)
    return WordsPerParagraph


#sentence per pragraph
def arabic_SPP(text):
    Sentence = arabic_sentenceCount(text)
    pragragh = arabic_paragraphCount(text)
    SentencePerPragragh = round(Sentence/pragragh,1)
    return SentencePerPragragh


# Characters Per Word
def arabic_CPW(text):
    WordCount=arabic_wordCount(text)
    CharacterCount=arabic_characterCount(text)
    CharactersPerWord=round(CharacterCount/WordCount,1)
    return CharactersPerWord




def arabic_ARI2(text):
  words = arabic_wordCount(text)
  chars = arabic_characterCount(text)
  sentences = arabic_sentenceCount(text)
  F3 = chars / words
  F5 = words / sentences
  ARI = (F3*4.71) + (F5 * 0.5) - 21.43
  return round(ARI,2)

def arabic_AARI(text):
  words = arabic_wordCount(text)
  chars = arabic_characterCount(text)
  sentences = arabic_sentenceCount(text)
  F3 = chars / words
  F5 = words / sentences
  AARI = ((chars*3.28)+(F3 * 1.43)+(F5 * 1.24)+472.42)/1046.3
  return round(AARI,2)

def arabic_Al_Heeti(text):
   words = arabic_wordCount(text)
   chars = arabic_characterCount(text)
   F3 = chars / words
   Al = (F3 * 4.414 ) - 13.468
   return round(Al,2)

#---------------------------APIS----------------------------------
    

def arabic_seg(text):
    apiURL = "/msa/webapi/segmenter"
    text = {'text': text}
    headers = { 'content-type': "application/json", 'cache-control': "no-cache" }
    response = requests.get(url + apiURL, params=text, headers=headers)
    result =  response.text
    res = ast.literal_eval(result)
    ret = ""
    for elem in res["segtext"]:
        ret += elem + " "
    return ret


def arabic_lemma(text):
    apiURL = "/msa/webapi/lemma"
    text = {'text': text}
    headers = { 'content-type': "application/json", 'cache-control': "no-cache" }
    response = requests.get(url + apiURL, params=text, headers=headers)
    result =  response.text
    res = ast.literal_eval(result)
    ret = ""
    for elem in res['result']:
        ret += elem + " "
    return ret



def arabic_SpCH(text):
  apiURL = "/msa/webapi/spellcheck"
  text = {'text': text}
  headers = { 'content-type': "application/json", 'cache-control': "no-cache" }
  response = requests.get(url + apiURL, params=text, headers=headers)
  result =  response.text
  res = ast.literal_eval(result)
  return res["result"]


def arabic_Diac(text):
  apiURL = "/msa/webapi/diacritize"
  text = {'text': text}
  headers = { 'content-type': "application/json", 'cache-control': "no-cache" }
  response = requests.get(url + apiURL, params=text, headers=headers)
  result =  response.text
  res = ast.literal_eval(result)
  return res["output"]

def arabic_Diac2(text):
  apiURL = "/msa/webapi/diacritizeV2"
  text = {'text': text}
  headers = { 'content-type': "application/json", 'cache-control': "no-cache" }
  response = requests.get(url + apiURL, params=text, headers=headers)
  result =  response.text
  res = ast.literal_eval(result)
  return res["output"]



def arabic_POS(text):
    apiURL = "/msa/webapi/pos"
    text = {'text': text}
    headers = { 'content-type': "application/json", 'cache-control': "no-cache" }
    response = requests.get(url + apiURL, params=text, headers=headers)
    result = response.text
    res = ast.literal_eval(result)
    arr=[] 
    for x in range(1,len(res)-1):
      r=res[x]
      arr.append(r["POS"])

    my_dict = {i:arr.count(i) for i in arr}
    # print(my_di/ct)
    # print("&"*50)
    # print(my_dict)
    # dict_count={"Adjectives":0,"Adverbs":0,"Conjuctions":0,"Determiners":0,
    # "Interjections":0,"Nouns":0,"Proper_Nouns":0,"Prepositions":0,"Pronouns":0,"Verbs":0}
    print(my_dict)
    dict_count= {'Nouns': 0, 'DET+NOUN': 0, 'DET+ADJ': 0, 'PUNC': 0, 'Verbs': 0, 'Prepositions': 0,
     'NOUN+NSUFF': 0, "Interjections": 0, "Proper_Nouns":0,
    'DET+ADJ+NSUFF': 0, 'NUM': 0, 'Conjuctions': 0, 'NUM+NSUFF': 0, 'ABBREV': 0, 'Adjectives': 0, 'CASE': 0, 
    'V+PRON': 0, "Adverbs": 0,
    'Pronouns': 0, 'Determiners': 0, 'PART': 0, 'NOUN+PART': 0, 'ADJ+NSUFF': 0}

    # {'NOUN': 26, 'DET+NOUN': 15, 'DET+ADJ': 4, 'PUNC': 36, 'V': 19, 'PREP': 20,
    # 'NOUN+NSUFF': 15, 'DET+ADJ+NSUFF': 2, 'NUM': 8, 'CONJ': 25, 'NUM+NSUFF': 2, 
    # 'ABBREV': 3, 'ADJ': 3, 'CASE': 1, 'V+PRON': 2, 'PRON': 12, 'DET+NOUN+NSUFF': 6,
    #  'PART': 5, 'NOUN+PART': 1, 'ADJ+NSUFF': 3}


    try : dict_count['Nouns'] = my_dict["NOUN"]
    except: pass
    try : dict_count['DET+NOUN'] = my_dict["DET+NOUN"]
    except: pass
    try : dict_count['DET+ADJ'] = my_dict["DET+ADJ"]
    except: pass
    try : dict_count['PUNC'] = my_dict["PUNC"]
    except: pass
    try : dict_count['Verbs'] = my_dict["V"]
    except: pass
    try : dict_count['Prepositions'] = my_dict["PREP"]
    except: pass
    try : dict_count['DET+ADJ+NSUFF'] = my_dict["DET+ADJ+NSUFF"]
    except: pass
    try : dict_count['NUM'] = my_dict["NUM"]
    except: pass
    try : dict_count['Conjuctions'] = my_dict["CONJ"]
    except: pass
    try : dict_count['NUM+NSUFF'] = my_dict["NUM+NSUFF"]
    except: pass
    try : dict_count['ABBREV'] = my_dict["ABBREV"]
    except: pass
    try : dict_count['Adjectives'] = my_dict["ADJ"]
    except: pass
    try : dict_count['Adverbs'] = my_dict["ADV"]
    except: pass
    try : dict_count['CASE'] = my_dict["CASE"]
    except: pass
    try : dict_count['Pronouns'] = my_dict["PRON"]
    except: pass
    try : dict_count['V+PRON'] = my_dict["V+PRON"]
    except: pass
    try : dict_count['Determiners'] = my_dict["DET+NOUN+NSUFF"]
    except: pass
    try : dict_count['PART'] = my_dict["PART"]
    except: pass
    try : dict_count['ADJ+NSUFF'] = my_dict["ADJ+NSUFF"]
    except: pass
    try : dict_count['ADJ+NSUFF'] = my_dict["ADJ+NSUFF"]
    except: pass

    print(dict_count)
    return dict_count
  # for keys,values in my_dict.items():
  #     print(keys," :",values)


def arabic_spellingIssues(text):
   res = arabic_SpCH(text)
   count = 0
   for i in res:
     if i == '/':
       count +=1
   return count   