print('escriba una lista de numeros separados x comas')
y=input()
x=y.split(',')
#print(list(map(int,x)))
z=list(map(int,x))

def bubblesort(lis):
    swapped=True
    while swapped ==True:
        swapped=False
        for i in range(len(lis)-1):
            if lis[i] > lis[i+1]:
                lis[i] , lis[i+1]= lis[i+1], lis[i]
                swapped=True
bubblesort(z)
print(z)