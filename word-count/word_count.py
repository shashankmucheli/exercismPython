def count_words(sentence):
    count_dict = {}
    sentence.replace("\t"," ")
    sentence.replace("\n"," ")
    split_sentence = sentence.split(" ")
    for i in range(0, len(split_sentence)):
        value = count_dict.get(split_sentence[i])
        if value is None:
            count_dict[split_sentence[i]] = 1
        else: 
            count_dict[split_sentence[i]] = value+1
    return count_dict
            
