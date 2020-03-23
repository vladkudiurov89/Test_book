matr = [
         [0, -1, 15, 20, 15],
         [-1, 0, 60, 50, 80],
         [15, 60, 0, 50, 10],
         [20, 50, 50, 0, 30],
         [15, 80, 10, 30, 0]
       ]


def search_min(tr, vizited):#1 место для оптимизации
    min = max(tr)
    for ind in vizited:
        for index, elem in enumerate(tr[ind]):
            if 0 < elem < min and index not in vizited:
                min = elem#веса путей
                index2 = index# индекс города
    return [min, index2]


def prim(matr):
    toVisit=[i for i in range(1,len(matr))]# города кроме начального(0)
    vizited=[0]
    result=[0]
    for index in toVisit:
        weight, ind=search_min(matr, vizited)
        result.append(weight)
        vizited.append(ind)
    return result

print(prim(matr))