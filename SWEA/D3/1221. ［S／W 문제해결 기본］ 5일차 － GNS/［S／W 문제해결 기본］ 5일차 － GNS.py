#GNS - 첫 접근 : 딕셔너리 사용해서 해결하자
numDict = {
    "ZRO": 0, "ONE": 1, "TWO": 2,
    "THR": 3, "FOR": 4, "FIV": 5,
    "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9,
}
valueDict = {
     0: "ZRO", 1: "ONE", 2: "TWO",
     3: "THR", 4: "FOR", 5: "FIV",
     6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN",
}
T = int(input())
for tc in range(1, T+1):
    tc_num, tcLen = input().split()
    testCase = list(input().split())

    for i in range(len(testCase)):
        testCase[i] = numDict[testCase[i]]

    testCase.sort()

    for i in range(len(testCase)):
        testCase[i] = valueDict[testCase[i]]

    print("#{}".format(tc))
    print("{}".format(' '.join(testCase)))
