def solution(s):
    small = "abcdefghijklmnopqrstuvwxyz"
    rev = "zyxwvutsrqponmlkjihgfedcba"
    a = ""
    for i in range(len(s)):
        if s[i] in small:
            a += rev[small.index(s[i])]
        else: 
            a += s[i]
    return a
print(solution("vmxibkgrAlm"))
