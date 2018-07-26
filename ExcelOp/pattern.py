
num=int(input('Enter a Number:'))
for i in range(1,num+1):
    print(""*(num-1),end="")
    for j in range(1,i+1):
        print('*',end="")
    print()