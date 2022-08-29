from analysis import analyser

dict_of_words = {} #you can insert, or write your own word dictionary here

sentence = input('Please type sentence here: ')

word_list = input('Please type name of file or dictionary where words are stored here: ')


print(analyser.analyseSentence(sentence,word_list))