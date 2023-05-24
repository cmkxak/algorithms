from itertools import combinations

def get_max_orders(candidates):
    order = {}
    answer = []
    for c in candidates:
        order[c] = order.get(c, 0) + 1
    if order:
        for k, v in order.items():
            if v == max(order.values()) and v >= 2:
                answer.append(''.join(k))
        return answer

def solution(orders, course):
    answer = []
    result = []
    for i in course:
        tmp = []
        if len(orders) >= i:
            for order in orders:
                for o in combinations(order, i):
                    candidate = ''.join(sorted(o))
                    tmp.append(candidate)
            res = get_max_orders(tmp)
            answer.append(res)
    for i in answer:
        for k in i:
            result.append(k)
    result.sort()
    return result