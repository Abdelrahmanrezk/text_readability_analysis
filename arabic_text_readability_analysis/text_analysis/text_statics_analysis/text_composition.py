import re
import nltk
import os


def get_text_composition(text):
    dict_group={"Adjectives":["JJ","JJR","JJS"],"Adverbs":["RB","RBR","RBS"],
    "Conjuctions":["CC"],"Determiners":["DT","PDT","WDT"],"Interjections":["UH"],
    "Nouns":["NN","NNS"],"Proper_Nouns":["NNP","NNPS"],"Prepositions":["IN"],
    "Pronouns":["PRP","PRP$","WP","WP$"],"Verbs":["VB","VBD","VBG","VBN","VBP","VBZ"],}

    dict_count={"Adjectives":0,"Adverbs":0,"Conjuctions":0,"Determiners":0,
    "Interjections":0,"Nouns":0,"Proper_Nouns":0,"Prepositions":0,"Pronouns":0,"Verbs":0}

    tokenized=nltk.sent_tokenize(text)
    try:
        for tokens in tokenized:
            words = nltk.word_tokenize(tokens)
            tagged = nltk.pos_tag(words)
            for word in tagged:
                pos=word[1]
                if(pos=="RB" or pos=="RBS" or pos=="RBR"):
                	pass
                for listKey,listElem in dict_group.items():    
                    if pos in listElem:
                        dict_count[listKey]+=1
    except Exception as e:
# send exception to log folder
        file = open("text_analysis/text_statics_analysis/logs_files/text_composition.log","+a")
        file.write("This error related to function get_text_composition of text_statics_analysis folder\n" 
                   + str(e) + "\n" + "#" *99 + "\n") # "#" *99 as separated lines
   
    return dict_count


