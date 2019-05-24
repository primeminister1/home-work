def rec(n):
    if n < 10: return n
    return int(str(n % 10) + str(rec(n // 10)))

def sum_product(n):
    if n < 10: return (print("Введіть n>10"))

    product = 1
    summa = 0
    for i in list(str(n)):
        summa += int(i)
        product *= int(i)
    print(summa)
    print(product)

def count_p_and_nep(n):
    p=0
    np=0
    for i in list(str(n)):
        if int(i) == 0:
            continue
        if  (int(i) % 2) == 0:
            p +=1
        elif (int(i) % 2) != 0:
            np +=1
    print("парних " )
    print(p)
    print("непарних ")
    print(np)



def Diya(n):
    print("Введіть друге число  ")
    n2 = int(input())
    print("Виберіть дію над двома числами * 1, / 2, + 3, - 4 ")
    diya = int(input())
    if diya == 1:
        print(n*n2)
    elif diya == 2:
        print(n/n2)
    elif diya == 3:
        print(n+n2)
    elif diya == 4:
        print(n-n2)






while True:

    print("Виберіть завдання від 1 до 4 ")
    i = int(input())
    print("Введіть число більше 10 ")
    n = int(input())
    if i == 1:
            print(rec(n))
    elif i == 2:
            print(sum_product(n))
    elif i == 3:
            print(count_p_and_nep(n))
    elif i == 4:
            print(Diya(n))
    print("Щоб продовжити програму натисніть Enter")
    q = input()
    if not not q:
        exit()



