a = input()
b = input()
m = a.split(" ")
n = b.split(" ")

    

j = 0

A = 0
B = 0
D = 0
for i in range(10) :
    h = m[j]
    k = n[j]
    if h < k :
        B+= 1
    if k < h :
        A+= 1
    if k == h :
        D+= 1 
    j+=1
if A > B :
    print("A")
if B > A :
    print("B")
if A == B :
    print("D")
