def solution(cards1, cards2, goal):
    for g in goal:
        if g==cards1[0] and len(cards1) > 0:
            cards1.pop(0)
        elif g==cards2[0] and len(cards2) > 0:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"