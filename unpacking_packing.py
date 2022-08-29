class pack_unpack():
    def unpack_csv(csv_file):
        t = 0
        word_storage = {}
        if ".csv" not in csv_file:
            return "use csv file"
        else:
            with open(csv_file,'r') as csv_read:
                for i in csv_read.readlines():
                    if t == 0:
                        t += 1
                        continue
                    key = i[:i.find(',')]
                    val = i[i.find(',')+1:]
                    if '\n' in val:
                        val = val[:-1]
                    word_storage.update({key:val})
        return word_storage

    def unpack_sentence(sentence):
        seperated_words = []
        space = 0
        while space != -1:
            space = sentence.find(" ")
            if space == -1:
                seperated_words.append(sentence.lower())
                break
            seperated_words.append(sentence[:space].lower())
            sentence = sentence[space + 1:]
        return seperated_words


    def pack_uw(unknown_word):
        with open("List_of_unknown_words.csv", "r") as unknown_words:
            if unknown_word in unknown_words.read():
                pass
            else:
                with open("List_of_unknown_words.csv", "a") as unknown_words:
                    unknown_words.write(unknown_word)
                    unknown_words.write("\n")