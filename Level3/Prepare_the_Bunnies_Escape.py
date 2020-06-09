def bfs(v, m, n):
    l=len(m)
    b=len(m[0])
    v=[]
    q=[]
    v.append(n)
    q.append(n)
    d=[[0 for i in range(b)] for i in range(l)]
    d[0][0]=1
    while q:
        # print(q)
        # print("Visited",v)
        s = q.pop(0) 
        tmp=[]
        if s[0]>0 and m[s[0]-1][s[1]]==0:
            tmp.append([s[0]-1,s[1]])
        if s[0]<l-1 and m[s[0]+1][s[1]]==0:
            tmp.append([s[0]+1,s[1]])
        if s[1]>0 and m[s[0]][s[1]-1]==0:
            tmp.append([s[0],s[1]-1])
        if s[1]<b-1 and m[s[0]][s[1]+1]==0:
            tmp.append([s[0],s[1]+1])   
        for e in tmp:
            # p=0
            if e not in v:
                v.append(e)
                q.append(e)
                d[e[0]][e[1]]=d[s[0]][s[1]]+1
                if e[0]==l-1 and e[1]==b-1:
                    return d[l-1][b-1]
    return 10000000

def solution(mat):
    q=[]
    v=[]
    d=[]
    d.append(bfs(v,mat,[0,0]))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==1:
                mat[i][j]=0
                v=[]
                q=[]
                d.append(bfs(v,mat,[0,0]))
                mat[i][j]=1
    # print(d)
    return(min(d))
# mat=[[0,1,1,0],[0,0,0,1],[1,1,0,0],[1,1,1,0]]
# mat=[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
mat=[[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(mat))
