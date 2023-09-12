def fun(num,t):
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            if num[i]+num[j] == t:
                print("found",(num[i],num[j]))
                return
    print("not found")
num = [3, 1, 4, 6, 8, 2]
t = 10
result = fun(num, t)
# another method
def fun(num,t):
    d={}
    for i, e in enumerate(num):
        if t-e in d:
            print("found",(num[d.get(t-e)], num[i]))
            return
        d[e] = i       
    print("not found")
if __name__ == '__main__':
    num = [8, 7, 2, 5, 3, 1]
    t = 10
    fun(num, t)
 
