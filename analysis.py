from unpacking_packing import pack_unpack
class analyser():
    def analyseSentence(sentence,word_list):
        score = 100


        for_analyse = pack_unpack.unpack_sentence(sentence) #turns string to list
        if type(word_list) == str and word_list[-4:] == '.csv':
            list_of_words = pack_unpack.unpack_csv(word_list) #list of words provided in csv format

            for word in for_analyse: #iterates through list of words provided by user
                if word in list_of_words: #checks if word is in word list provided by user (csv format)
                    score = score + int(list_of_words[word])
                else: #if word was not found in list_of_words than unknown words are stored are stored in List_of_unknown_words.csv file
                    pack_unpack.pack_uw(word)
        elif type(word_list) == dict:
            for word in for_analyse:  # iterates through list of words provided by user
                if word in word_list:  # checks if word is in word list provided by user (Dict format)
                    score = score + word_list.get(word)
                else:  # if word was not found in list_of_words than unknown words are stored are stored in List_of_unknown_words.csv file
                    pack_unpack.pack_uw(word)
        else:
            return 'you must input dictionary or .csv format file as List_Of_Words'

        #checks score and determines sentence's negativity/positivity
        if score < 0:
            print ('comment is aggressive')
        elif score <= 68:
            print ('comment is negative')
        elif score <= 138:
            print ('comment is normal')
        elif score <= 200:
            print ('comment is positive')
        else:
            print ('comment is very positive')
        return score
