"""
最初に考えたパターン 何となく言いたいことはわかるけど、面倒くさい
a = range(1,10,1)
b = range(2,20,2)
c = range(3,30,3)
d = range(4,40,4)
e = range(5,50,5)
f = range(6,60,6)
g = range(7,70,7)
h = range(8,80,8)
i = range(9,90,9)
print(list(a))
print(list(b))
print(list(c))
print(list(d))
print(list(e))
print(list(f))
print(list(g))
print(list(h))
print(list(i))
"""
for cnt1 in range(1, 10):
    for cnt2 in range(1, 10):
        print( cnt1*cnt2, end=' ')
    print() # print('/n', end=") #取り敢えず完成
