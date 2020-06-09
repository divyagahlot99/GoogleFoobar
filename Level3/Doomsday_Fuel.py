from fractions import Fraction

def lcm(a,b):
    i=max(a,b)
    while i%a!=0 or i%b!=0:
        i+=1
    return i

def lcm_list(lis):
    new_lcm=1
    for i in lis:
        new_lcm=lcm(new_lcm,i)
    return new_lcm

def generate_p(m,l,h):
    p=[]
    last=l-1
    t=0
    for i in range(h):
        u=[]
        y=sum(m[i])
        if y==0:
            p.append(m[i])
        else:
            for j in range(l):
                u.append(Fraction(m[i][j], y))
            p.append(u)
    m=p
    for i in range(l-1,-1,-1):
        if m[i][i]==1 or max(m[i])==0:
            t+=1
            c=m.pop(i)
            m.insert(last,c)
            for j in range(l):
                temp=m[j].pop(i)
                m[j].insert(last,temp)
            last-=1
    return m,t

def generate_q(p,t,l,h):
    q=[]
    for i in range((l-t)):
        q.append(p[i][0:l-t])
    return q

def generate_r(p,t,l,h):
    r=[]
    for i in range(l-t):
        r.append(p[i][l-t:])
    return r

def generate_Identity(t,l,h):
    m=[[Fraction(0) for i in range(t)] for i in range(t)]
    for i in range(t):
        m[i][i]=Fraction(1)
    return m

def generate_Inverse(A,l,h):
    n = len(A)
    AM = A
    I = generate_Identity(n,l,h)
    IM = I
    indices = list(range(n))
    for fd in range(n): 
        fdScaler = Fraction(1, AM[fd][fd])
        for j in range(n): 
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd+1:]: 
            crScaler = AM[i][fd]
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = Fraction(IM[i][j] - crScaler * IM[fd][j])
    return IM

def diff_matrices(A,B,l,h):
    C=[[Fraction(0) for i in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j]=A[i][j]-B[i][j]
    return C

def print_mat(Name,m):
    print(Name,"-----------")
    for i in m:
        for j in i:
            print(j, end=" ")
        print(" ")
    print("")

def mult_matrices(X,Y,l,h):
    C=[[Fraction(0) for i in range(len(Y[0]))] for i in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                C[i][j] += Fraction(X[i][k] * Y[k][j])
    return C


def solution(m):
    if m==[[0]]:
        return [1, 1]
    l=len(m[0])
    h=len(m)
    p,t=generate_p(m,l,h)
    q=generate_q(p,t,l,h)
    r=generate_r(p,t,l,h)
    I=generate_Identity(l-t,l,h)
    Diff_I_q=diff_matrices(I,q,l,h)
    N=generate_Inverse(Diff_I_q,l,h)
    B=mult_matrices(N,r,l,h)

    # print_mat("M",m)
    # print_mat("P",p)
    # print_mat("Q",q)
    # print_mat("Diff_I_q",Diff_I_q)
    # print_mat("N",N)
    # print_mat("B",B)
    # print_mat("R",r)
    if len(B)==0:
        ans=[0]*len(m[0])
        ans.append(1)
        return ans
    B=B[0]
    nums=[]
    dens=[]
    ans=[]
    for i in B:
        nums.append(i.numerator)
        dens.append(i.denominator)
    
    denmax=lcm_list(dens)
    for i in range(len(nums)):
        ans.append(nums[i]* int(denmax/dens[i]))
    ans.append(denmax)
    return ans

# print(solution([[0]]))
# print(solution([[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))

