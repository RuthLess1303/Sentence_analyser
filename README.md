# Sentence_analyser
Program analyses sentence depending on word list you provide where will be specified word with their score

Format for word list as csv file:
1. word,score
2. disaster,-20
3. happy,10
4. worried,-3

As you see first line must be name of columns, first column must be words and second score for each word.
You can include negative and positive words in one csv file, but scores for negative words need to be negative numbers.

Format for word list as dictionary:
{"disaster":-20,"happy":10,"worried":-3}

As you see Key for dictionary must be word and Value must be score.
You can include negative and positive words in one csv file, but scores for negative words need to be negative numbers.



In main.py you can exclude 'sentence' and 'word_list' variables and type manually desired sentence and word list in 'analyser.analyserSentence()',
first argument needs to be sentence and second argument needs to be list of words as Dictionary or CSV file format, otherwise program would not work
