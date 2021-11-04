def tri_bulle(t):
    n = len(t)
    for i in range(n):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
    return t
def tri_insertion(t):
    for i in range(1, len(t)):
        k = t[i]
        j = i-1
        while j >= 0 and k < t[j] :
                t[j + 1] = t[j]
                j -= 1
        t[j + 1] = k
    return t
def tri_selection(t):
    for i in range(len(t)):
        min = i
        for j in range(i + 1, len(t)):
            if t[min] > t[j]:
                min = j
        t[i], t[min] = t[min], t[i]
    return t
t = [12, 43, -20, 87, 99, -64, 45, 34]
tri_bulle(t)
print("Le tableau trié par la methode en bulle:",[t[i] for i in range(len(t))])
tri_insertion(t)
print("Le tableau trié par la methode en insertion:",[t[i] for i in range(len(t))])
tri_selection(t)
print("Le tableau trié par la methode en selection:",[t[i] for i in range(len(t))])