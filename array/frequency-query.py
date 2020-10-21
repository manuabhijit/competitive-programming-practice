def freqQuery(queries):
    occ = {}
    freqEq = {}
    ans = []
    for (c, e) in queries:
        if c == 1:
            if occ.get(e) is None:
                occ[e] = 1
            else:
                occ[e] += 1
            freqEq[occ[e]] = True
        elif c == 2 and occ.get(e) is not None:
            if occ[e] > 0:
                occ[e] -= 1
                freqEq[occ[e]] = True
            else:
                del occ[e]
        elif c == 3:
            isMatch = False
            if freqEq.get(e) is True:
                for e_uq in occ:
                    if occ[e_uq] == e:
                        isMatch = True
                        break
            ans.append(1 if isMatch else 0)
    return ans


ans = freqQuery([
    (1, 5), (1, 6), (3, 2), (1, 10),
    (1, 10), (1, 6), (2, 5), (3, 2),
])

print("ans=", ans)
