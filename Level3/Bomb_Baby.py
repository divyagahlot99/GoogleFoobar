def gcd(a, b):
    a,b=max(a,b),min(a,b)
    if a % b == 0: return b
    else: return gcd(b, a % b)

def solution(a,b):
    a=int(a)
    b=int(b)
    times=0
    if a==1 or b==1:
        return str(abs(a-b))
    if a%b==0 or b%a==0 or a==b or gcd(a,b)!=1:
        return "impossible"
    while a!=1 or b!=1:
        a,b=max(a,b),min(a,b)
        times+=int((a-(a%b))/b)
        a=a%b
        if a==1:
            times+=b-1
            break
    return str(times)

# print(solution("2","1"))
