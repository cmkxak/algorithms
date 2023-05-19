t = int(input())
for test_case in range(1, t+1):
    cardInfo = input()

    s_cnt, d_cnt, h_cnt, c_cnt = 13,13,13,13
    check = []
    for i in range(0,len(cardInfo),3):
        inventory = cardInfo[i: i+3]
        if inventory in check:
            print("#{} {}".format(test_case, "ERROR"))
            break
        else:
            check.append(inventory)

        cardType = inventory[0]
        if cardType == "S":
            s_cnt -=1
        elif cardType == "D":
            d_cnt -=1
        elif cardType == "H":
            h_cnt -=1
        elif cardType == "C":
            c_cnt -=1
    else:
        print("#{} {} {} {} {}".format(test_case, s_cnt, d_cnt, h_cnt, c_cnt))