import pymysql
connection_ack = pymysql.connect(port=3306, host='localhost', user='root', passwd='989044', db='python')
print(connection_ack)

communication_channel = connection_ack.cursor()
communication_channel.execute('select * from persons')
results = communication_channel.fetchall()
print('Results',results)
file = open('abc.txt','w')
listOfKeys = []
listOfValues= []

for item in results:
    listOfVal = []
    for index,words in enumerate(item):
        print(index,words)
        if index==0:
            listOfKeys.append(words)
        else:
            listOfVal.append(words)
            listOfValues.append(listOfVal)
        print(listOfValues)
        print(listOfKeys)


        dictionary = {}
        for index,key in enumerate(listOfKeys) :
            dictionary[key] = listOfValues[index]


#dictionary[None] = 'A'
#dictionary[None] = 'B'
#print(dictionary)
print('--------------')
#print(dictionary.get(2))