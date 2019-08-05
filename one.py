fhand = open("input.txt","r")
lst= fhand.readlines()   
freq = dict()
for line in lst:
        lne=line.split(" ")
        #lne.lower()
        for word in lne:
            count = freq.get(word,0)
            freq[word] = count +1
freq_list = freq.keys()
result = []
for word in freq_list:
    print(word,":",freq[word])
    result.append(word+":"+str(freq[word])+", ")

fo = open("output.txt","w")
for word in result:
    fo.write(word)

fo.close()
fhand.close()
