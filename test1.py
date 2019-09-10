a = []
d = []
f = []
for i in range(1,10):
    a.append(i)
for item in range(0,3):   
    d.append(list(a[(3 * item):(3 + 3 * item)]))
for item in range(0, 3):
    e = []
    for item in range(len(a) - (2-item),0,-3):
        e.append(item)
    print(e)