import bruth
import listofprimes


# except:
#	print("file missing download it from https://www.github.com/spiderskillshare")
# ask for
# calculator
# power
# every word list
# artimatic or geometric question solver
# prime check and twin prime list


def main():
    what = input("what do you wanna do \na, calculater \nb, power calculation \nc, brutforce \nd, sequence "
                 "calculation \ne, list of primes or twin primes \n\nyou@python$ ")
    if what == 'a':
        cal()
    elif what == 'b':
        power()
    elif what == 'c':
        try:
            bruth.main()
        except:
            print("file missing download bruth.py from https://www.github.com/spiderskillshare")
    elif what == 'd':
        archgeo()
    elif what == 'e':
        try:
            if __name__ == '__main__':
                numb = 1
                rang = int(input("enter the range that you wanna see: "))
                what = input("which types of list you want \na, twin primes \nb, just primes \n>>")
                if rang < 0:
                    print("range is less than zero quiting...")
                    quit()
                listofprimes.main(what, rang, numb)
        except:
            print("file missing download listofprimes.py from https://www.github.com/spiderskillshare")
    else:
        print("invalid input")


def cal():
    num1 = int(input("enter the first number: "))
    op = input("enter the operation you wanna do: ")
    num2 = int(input("enter the second number: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("invalid operation")


def power():
    base = int(input("enter the base number: "))
    powe = int(input("enter the power number: "))
    answer = 1
    for num in range(powe):
        answer *= base
    print(answer)


def archgeo():
    methods = input("what you want to do  \na) the program to distinguish the sequence b/n arithmetic and geometric\nb) you manually type it \n>>")
    if methods == "a":
        n1 = int(input("enter the first number: "))
        n2 = int(input("enter the second number: "))
        n3 = int(input("enter the third number: "))
        if n3 - n2 == n2 - n1:
            n = int(input("enter which number you wanna calculate or n: "))
            d = n2 - n1
            print(n1 + (n - 1) * d)
        elif n3 / n2 == n2 / n1:
            n = int(input("enter which number you wanna calculate or n: ")) - 1
            r = (n3 / n2)
            print(pow(r, n) * n1)
    elif methods == "b":
        manual = input("enter the sequence type \na) arithmetic \nb) geometric \n>>")
        if manual == 'a':
            a1 = int(input("enter the first number: "))
            a2 = int(input("enter the second number: "))
            n = int(input("enter which number you wanna calculate or n: "))
            d = int(input("enter the value of d: "))
            print(a1 + (n - 1) * d)
        elif methods == 'b':
            g1 = int(input("enter the first number: "))
            n = int(input("enter which number you wanna calculate or n: ")) - 1
            r = int(input("enter the value of r: "))
            print(pow(r, n) * g1)
        else:
            print("invalid input")
            quit()
    else:
        print("invalid input try again")
        quit()


if __name__ == '__main__':
    main()
