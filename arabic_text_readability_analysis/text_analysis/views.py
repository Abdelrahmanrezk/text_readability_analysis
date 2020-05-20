from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
import sys
import os
import pandas as pd
import random
import numpy as np
import secrets

# NLTK and text analysis files
from text_analysis.text_statics_analysis.text_composition import *
from text_analysis.text_statics_analysis.ReadabilityGradeLevels import *


def text_static_readability_composition(data, text):
	'''
	Argument:
		data: as python dictionary
		text: That user input on our interphase
	return:
		data as dictionary with text analysis calculated
	'''

	# Counts Statics
	statics_calculations = {
		'character_count'   : characterCount(text),  # ReadabilityGradeLevels file
		'syllable_count'	: syllableCount(text), 	 # ReadabilityGradeLevels file
		'word_count'		: wordCount(text), 		 # ReadabilityGradeLevels file
		'unique_word_count'	: uniqueWordCount(text), # ReadabilityGradeLevels file
		'sentence_count'	: sentenceCount(text), 	 # ReadabilityGradeLevels file
		'paragraph_count' 	: paragraphCount(text),  # ReadabilityGradeLevels file
	}
	
	

	# Readability GradeLevels
	readability_gradeLevels = {
		'flesch_kincaid_grade_level'   	: FKRA(text),    # ReadabilityGradeLevels file
		'gunning_fog_index'				: GFI(text),     # ReadabilityGradeLevels file
		'coleman_liau_index'			: CLI(text),     # ReadabilityGradeLevels file
		'smog'							: SMOGI(text),   # ReadabilityGradeLevels file
		'automated_readability_index'	: ARI(text),     # ReadabilityGradeLevels file
		'flesch_reading_ease' 			: FORCAST(text), # ReadabilityGradeLevels file
		'powers_sumner_kearl_grade' 	: PSKG(text),    # ReadabilityGradeLevels file
	}

	# statics_calculations dictionary created above
	data['statics_calculations'] = statics_calculations

	# readability_gradeLevels dictionary created above
	data['readability_gradeLevels'] = readability_gradeLevels

	# Text Composition 
	data['text_composition'] 		= get_text_composition(text) # text_composition file

	return data


def home_page(request):
	'''
	Argument:
		request: page request
	return:
		either the page itself if get request
		or if post make some analysis and return json result to js and js add to page
	'''

	data = {}
	if request.method == 'POST':
		try:
			# if data has user_text else generate text int except
			data = json.loads(request.body) # get data hat user inout in text area
			text = data['user_text']

			data = text_static_readability_composition(data, text)
			return JsonResponse(data)
		except:
			# generate some text from the IWSLT-sample.en and display in the input
			secure_random = secrets.SystemRandom()     
			text_file = open('text_analysis/IWSLT-sample.en', "r")
			start, end = np.random.randint(1000), np.random.randint(1000)
			# random numbers can be any number in range 1000 so start should less end to take lines
			if start > end:
				start, end = end, start # swap

			# read the random lines from the file
			lines = text_file.readlines()[start:end+2]

			# take from these line some lines and max is 15 line to displau in input
			random_lines = secure_random.sample(lines, min(len(lines)+3,np.random.randint(12)+3))
			random_lines = "".join(random_lines)

			# after choose random lines start to get text analysis calculated
			data = text_static_readability_composition(data, random_lines)
			data['generated_text'] = random_lines
			return JsonResponse(data)
	return render(request, 'text_analysis/home_page.html', data)
	


