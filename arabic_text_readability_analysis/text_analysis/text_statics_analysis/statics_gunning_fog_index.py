


import pyphen
import re
import nltk
dic = pyphen.Pyphen(lang='en')




def get_number_of_sentence_paragraph(text):
    '''
    Argument:
    text: is a string that contain multiple sentences and paragraphs
    return:
    - number of . that the whole text contain
    - number of paragraph based on \n
    '''
    #  Linux uses \n for a new-line, Windows \r\n and old Macs \r
    num_paragraph = text.split('\n')
    num_paragraph = sum( [len(paragraph) > 0 for paragraph in num_paragraph])
    
    num_sentence = len(nltk.sent_tokenize(text))
    
    return max(num_sentence, 1), max(num_paragraph, 1)



def get_number_of_words_char_unique(text):
    '''
    Argument:
    text: is a string that contain multiple sentences and paragraphs
    return:
    different statics like:
        - numbers of words in the whole text
        - number of chars of all words in the text
        - number of unique words in the whole text
    '''
    text = text.lower()
    text = text.split()
    chars_number = 0
    words_number = 0
    word_unique_numbers = 0
    yahoo_sign_count = 0
    unique_words_count = []
    for word in text:
        word = re.sub('["<>%$&|\';+~*_^]', '', word)
        yahoo_sign_count = word.count('@')
        words_number += yahoo_sign_count

        words = re.split('[#-\[\]{}`/—@]', word)
        chars_number += sum([len(word) for word in words])
        unique_words_count.extend([word for word in words if word])
        words_number += len([word for word in words if word])
    unique_words_count = len(set(unique_words_count))
    return words_number, unique_words_count, chars_number





def get_num_syllables(text):
    '''
    Argument:
    text: is a string that contain multiple sentences and paragraphs
    return:
    complex_words: numebr of all of words that contain more than or equal to 3 syllables 
    like graduate ==> grad-u-ate counted as 1
    '''
    text_list = re.findall('(\w+)', text)
    complex_words = 0
    for i in text_list:
        
        syllable_word = dic.inserted(i)
        syllable_dash = re.findall('-', syllable_word)
        if len(syllable_dash) >= 2:
            complex_words +=1
    return max(1, complex_words)





# def gunning_fog_index(text):
#     '''
#     The function work as pipline and at the end return gunning fog index,
#     which realated to score of readability for writing text
#     Argument:
#     text: is a string that contain multiple sentences and paragraphs
#     return:
#     gun_fog_result the result of gunning fog index
#     '''
#     # num_of_sentence, num_paragraph = get_number_of_sentence_paragraph(text)
#     word_numbers, uniques_words_numbers, chars_number = get_number_of_words_char_unique(text)
#     num_of_syllable = get_num_syllables(text)
#     # print(num_paragraph)
#     # print(num_of_sentence)
#     # print(word_numbers)
#     # print(num_of_syllable)
#     # word_numbers +=1
#     gun_fog_result = .4 * ((word_numbers/num_of_sentence) + (100 * ((num_of_syllable)/word_numbers)))
#     return round(gun_fog_result, 1)




