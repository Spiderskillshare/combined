def main():
    leng = int(input("enter the length of the words you want the probablity to be with 4-9: "))

    if leng == 4:
        print("writing the worldlist...")
        if leng4():
            bets.close()
    elif leng == 5:
        print("writing the worldlist...")
        if leng5():
            bets.close()
    elif leng == 6:
        print("writing the worldlist...")
        if leng6():
            bets.close()
    elif leng == 7:
        print("writing the worldlist...")
        if leng7():
            bets.close()
    elif leng == 8:
        print("writing the worldlist...")
        if leng8():
            bets.close()
    elif leng == 9:
        print("writing the worldlist...")
        if leng9():
            bets.close()
    else:
        print("the number you entered isn't supported here ")
    print("file closed you can find the wordlist in current directory >> wordlist.txt")


def rite(lists):
    bets.write(lists)


def leng4():
    for word in alpha:
        print("progress is in " + word + "...")
        for subword in alpha:
            for subsubword in alpha:
                for iiisubword in alpha:
                    rite(word + subword + subsubword + iiisubword + "\n")
    return True


def leng5():
    for word in alpha:
        print("progress is in " + word + "....")
        for subword in alpha:
            for subsubword in alpha:
                for iiisubword in alpha:
                    for ivsubword in alpha:
                        rite(word + subword + subsubword + iiisubword + ivsubword + "\n")
    return True


def leng6():
    for word in alpha:
        print("progress is in " + word + ".....")
        for subword in alpha:
            for subsubword in alpha:
                for iiisubword in alpha:
                    for ivsubword in alpha:
                        for vsubword in alpha:
                            rite(word + subword + subsubword + iiisubword + ivsubword + vsubword + "\n")
    return True


def leng7():
    for word in alpha:
        print("progress is in " + word + "......")
        for subword in alpha:
            for subsubword in alpha:
                for iiisubword in alpha:
                    for ivsubword in alpha:
                        for vsubword in alpha:
                            for visubword in alpha:
                                rite(word + subword + subsubword + iiisubword + ivsubword + vsubword + visubword + "\n")
    return True


def leng8():
    for word in alpha:
        print("progress is in " + word + ".......")
        for word in alpha:
            for subword in alpha:
                for subsubword in alpha:
                    for iiisubword in alpha:
                        for ivsubword in alpha:
                            for vsubword in alpha:
                                for visubword in alpha:
                                    for viisubword in alpha:
                                        rite(word + subword + subsubword + iiisubword + ivsubword + vsubword + visubword + viisubword + "\n")
    return True


def leng9():
    for word in alpha:
        print("progress is in " + word + ".......")
        for word in alpha:
            for subword in alpha:
                for subsubword in alpha:
                    for iiisubword in alpha:
                        for ivsubword in alpha:
                            for vsubword in alpha:
                                for visubword in alpha:
                                    for viisubword in alpha:
                                        for viiisubword in alpha:
                                            rite(word + subword + subsubword + iiisubword + ivsubword + vsubword + visubword + viisubword + viiisubword + "\n")
    return True


alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]

first = open("wordlist.txt", "w")
first.write("written by The spider \n")
first.close()
bets = open("wordlist.txt", "a")

if __name__ == '__main__':
    main()
