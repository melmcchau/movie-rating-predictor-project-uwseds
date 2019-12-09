"""
SentimentSetup.py
"""

from .sentiments_nrc import SENTIMENTS
from .sentiments_nrc import EMOTIONS

# support function 1
def words_with_specific_emotion(list_of_split_words, emotion):
    '''Produce a list that include the words that contain a specific emotion
       Parameters: list_of_split_words (String): A list with split words
                   emotion(string): the emotion words in EMOTIONS list
       Returns: list: the words in the string with one certain kind of emotion'''
    #get the emotion list of every word in the list
    look_up = [SENTIMENTS.get(word) for word in list_of_split_words]
     #zip the emotion list with word in one list
    combine = list(zip(list_of_split_words, look_up))
    words_with_specific_emotion = [line[0] for line in combine if line[1]
                                   is not None and line[1].get(emotion) == 1]
    #find the words in a specific emotion
    return words_with_specific_emotion

# support function 2
def words_list_for_each_emotion(split_test_string):
    '''Produce a disctionary with emotion words as keys and words list
       having that emotion as values
       Parameters: split_test_string (String): A list with split words
       Returns: list-the  most common words in the input list'''
    matching_words = [words_with_specific_emotion(split_test_string, emotion)
                      for emotion in EMOTIONS]
    distinct_matching = [i for i in matching_words]
    return {emotion:matching_word for (emotion, matching_word)
            in zip(EMOTIONS, distinct_matching)}

# support function 3
def get_common_words_list(wordlist):
    '''Produce a list with the most common words of the input list
       Parameters: wordlist (string):
       Returns: dict: the key-values pairs of emotions word and its
       corresponding words in the string'''
    wordfreq = list(zip(wordlist, [wordlist.count(w) for w in wordlist]))
    wordfreq_sort = list(set(sorted(wordfreq, key=lambda freq: freq[1],
                                    reverse=True)))
    new_word_freq_sort = sorted(wordfreq_sort, key=lambda freq: freq[1],
                                reverse=True)
    return [i[0] for i in new_word_freq_sort]
