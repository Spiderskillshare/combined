def main(what, rang, numb):
    if what == 'a':
        print("processing...")
        primity(rang, numb)
        num = 0
        twin(num)
    elif what == 'b':
        print("processing...")
        primity(rang, numb)
        print(primes)
    else:
        print("invalid input so quiting...")
        quit()


def pri(num):
    lists = []
    while num > 0:
        lists.append(num)
        num -= 1
    return lists


def primity(rang, numb):  # checking the primity of the number
    while numb <= rang:
        count = 0
        for number in pri(numb):
            check = numb % number

            if check == 0:
                count += 1

        if count == 2:
            primes.append(numb)
        else:
            pass
        numb += 1  # if numb += 1 is on the upper part of the if close the it won't work


def twin(num):
    prime2 = primes.copy()
    prime2.append(1)
    twin1 = []
    twin2 = []
    for prim in primes:
        if primes[num] + 2 == prime2[num + 1]:  # 'prime num(3)+2'=5 and 'next prime num'=5 twinprime
            print(str(primes[num]) + " and " + str(primes[num + 1]))
        num += 1


primes = []
if __name__ == '__main__':
    numb = 1
    rang = int(input("enter the range that you wanna see: "))
    what = input("which types of list you want \na, twin primes \nb, just primes \n>>")
    if rang < 0:
        print("range is less than zero quiting...")
        quit()
    main(what, rang, numb)