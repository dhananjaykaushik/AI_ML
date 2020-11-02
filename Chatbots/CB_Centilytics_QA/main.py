
import random

import numpy as np
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# from spacy.lang.en import English
nlp = spacy.load('en_core_web_lg')

output_file_path = './output.txt'

file_data = ''
with open(output_file_path) as outfile:
    lines = outfile.readlines()
    for line in lines:
        file_data += ('\n' + line)

nlp.add_pipe(nlp.create_pipe('sentencizer'))
doc = nlp(file_data)
sentences = []
for sent in doc.sents:
    sentence = sent.string.strip()
    if (len(sentence)):
        sentences.append(sent.string.strip())


sentence_list = sentences

# Greeting Function


def greeting_response(text):
    text = text.lower()

    # Bot greeting response
    bot_greetings = ['howdy', 'hello',
                     'hey there!', 'good to have you', 'hola']
    user_greetings = ['hi', 'hey', 'hello', 'hola']
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)
    return None


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                # Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index


# Creating Bot Response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            # Found Similarity
            bot_response = bot_response + ' ' + sentence_list[index[i]]
            response_flag = 1
            j += 1
        if (j > 2):
            break
    if response_flag == 0:
        # No matches found
        bot_response = bot_response + ' Sorry, I don\'t understand.'

    sentence_list.remove(user_input)
    return bot_response


def intiateChat():
    # Start the chat
    print('Centilytics Bot:')
    print('I will answer your queries about Centilytics console.')
    print('Type !q to quit anytime.')

    while(True):
        user_input = input('Query: ')
        if user_input == '!q':
            print(
                'Centilytics Bot: Have a good day. I\'m always here for you. Contact me anytime.')
            break
        greet = greeting_response(user_input)
        if greet is not None:
            print('Centilytics Bot: ' + greet)
        else:
            print('Centilytics Bot: ' + bot_response(user_input))


intiateChat()
