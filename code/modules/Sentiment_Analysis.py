
import re
import sentiments_nrc
from sentiments_nrc import SENTIMENTS
from sentiments_nrc import EMOTIONS

# support function 1
def words_with_specific_emotion(list_of_split_words,emotion):
    '''Produce a list that include the words that contain a specific emotion
       Parameters: list_of_split_words (String): A list with split words 
                   emotion(string): the emotion words in EMOTIONS list
       Returns: list: the words in the string with one certain kind of emotion
    '''
    Look_Up=[SENTIMENTS.get(word) for word in list_of_split_words] #get the emotion list of every word in the list 
    Combine=list(zip(list_of_split_words,Look_Up)) # zip the emotion list with word in one list 
    Words_With_Specific_Emotion=[line[0] for line in Combine if line[1] is not None and line[1].get(emotion)==1 ]
    return Words_With_Specific_Emotion #find the words in a specific emotion

# support function 2
def words_list_for_each_emotion(Split_Test_String):
    '''Produce a disctionary with emotion words as keys and words list having that emotion as values
       Parameters: Split_Test_String (String): A list with split words
       Returns: list-the  most common words in the input list
    '''
    matching_words=[words_with_specific_emotion(Split_Test_String,emotion) for emotion in EMOTIONS]
    distinct_matching=[i for i in matching_words]
    return {emotion:matching_word for (emotion,matching_word) in zip(EMOTIONS,distinct_matching)}

# support function 3 
def get_common_words_list(wordlist):
    '''Produce a list with the most common words of the input list
       Parameters: wordlist (string): 
       Returns: dict: the key-values pairs of emotions word and its corresponding words in the string
    '''
    wordfreq=list(zip(wordlist,[wordlist.count(w) for w in wordlist]))
    wordfreq_sort=list(set(sorted(wordfreq,key=lambda freq: freq[1], reverse=True)))
    new_word_freq_sort=sorted(wordfreq_sort,key=lambda freq: freq[1], reverse=True)
    return [i[0] for i in new_word_freq_sort]

## main analysis function 
def analyze_quote(movie_review,criticname):
    
#     criticname = input("Please enter the Critic that you are interested: ")
    critic_quote=movie_review[['critic','quote']]
    quote = critic_quote[critic_quote['critic'] == criticname]

    #### cominbine quotes into one row 
    content=quote.groupby('critic')['quote'].apply(' '.join).reset_index()['quote']
    Split_String=re.split(r'\W+',content[0]) 
    lower_words=[word.lower() for word in Split_String] 
    length_filtered=[word for word in lower_words if len(word)>1]
    
    ### calculate total number or words
    Total_Words=len(length_filtered)
    Words_List_for_Each_Emotion=words_list_for_each_emotion(length_filtered)
    
    result_list=[]
    for i in EMOTIONS:
        result={}
        example_words=[get_common_words_list(value)[:3] for key,value in Words_List_for_Each_Emotion.items() if key==i]
        result['EMOTION']=i
        result['PERCENT']= len(Words_List_for_Each_Emotion[i])/Total_Words
        result['EXAMPLE WORDS']=example_words[0]
        result_list.append(result)
    result=sorted(result_list,key=lambda k:k['PERCENT'],reverse=True)
    
    return pd.DataFrame(result)