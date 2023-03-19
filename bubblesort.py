y=input('escriba una lista de numeros separados x comas')
str_list=y.split(',')
#print(list(map(int,x)))
int_list=list(map(int,str_list))

def bubblesort(lis):
    swapped=True
    while swapped ==True:
        swapped=False
        for i in range(len(lis)-1):
            if lis[i] > lis[i+1]:
                lis[i] , lis[i+1]= lis[i+1], lis[i]
                swapped=True
bubblesort(int_list)
print(int_list)
