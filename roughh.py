n = list(map(int,input().split()))
pre = 1 
suf = 1
res = [1]*len(n)


for i in range(len(n)-1):
    s *= n[-i-1]
    pre *= n[i]
    
    res[-i-2] *= suf
    res[-i-2] *= pre
    
print(res)