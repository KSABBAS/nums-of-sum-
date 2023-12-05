import random
def function() :
    list_of_numbers=[]
    amount =  int(input("enter the number : "))
    amount_of_tries = int(input("enter the number of tries : "))
    total_lists=[]
    total_amount_of_lists=0
    c=0
    v=amount/4
    v=int(v)
    while amount_of_tries!=0:
        while c!=amount and c<amount :
            n=random.randint(1,v)
            while (n==amount) or n>(amount-c):
                n=random.randint(1,v)
            l=n
            list_of_numbers.append(l)
            c+=l
        if list_of_numbers not in total_lists:
            print(list_of_numbers)
            total_lists.append(list_of_numbers)
            amount_of_tries-=1
            list_of_numbers =[]
            c=0
            total_amount_of_lists+=1
function()



