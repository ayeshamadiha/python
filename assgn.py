temp =["aa","bb","aa","bb","aa","cc"]
freq={}
for word in temp:
        count =freq.get(word,0)
        freq[word]=count +1
freq_list= freq.keys()
for words in freq_list:
        print(words,freq[words]
