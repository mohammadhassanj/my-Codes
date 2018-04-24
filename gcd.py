def prime_factorz(a):
    res_a = []
    q = 2
    while a>1:
        if a % q == 0:
            res_a.append(q)
            a /= q
        elif q == 2:
            q+=1
        else:
            q+=2 
    return res_a

def gcd(a,b):
    temp = []
    result = 1
    a = prime_factorz (a)
    b = prime_factorz (b)
    moshtarak = set(a) & set(b)
    for item in moshtarak:
        temp+=[item for i in range(min(a.count(item),b.count(item)))]
    for factor in temp:
        result*=factor
    return result

