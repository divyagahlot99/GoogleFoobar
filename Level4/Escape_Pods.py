def matrix_generator(sources, sinks, mat):
    mat.insert(0, [0] * (len(mat[0]) + 2))
    mat.append([0] * (len(mat[0])))
    for i in sources:
        mat[0][i+1] = 1000000
    for i in range(1,len(mat)-1):
        mat[i].insert(0,0)
        mat[i].append(0)
    for i in sinks:
        mat[i+1][len(mat)-1] = 1000000
    return mat

class Network: 
    def __init__(self,mat): 
        self.mat = mat 
        self.ROW = len(mat) 
    def BFS(self,s, t, parent): 
        visited =[False]*(self.ROW) 
        queue=[] 
        queue.append(s) 
        visited[s] = True
        while queue: 
            u = queue.pop(0) 
            for ind, val in enumerate(self.mat[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
        return True if visited[t] else False
    def FordFulkerson(self, source, sink): 
        parent = [-1]*(self.ROW) 
        max_flow = 0 
        while self.BFS(source, sink, parent) : 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.mat[parent[s]][s]) 
                s = parent[s] 
            max_flow +=  path_flow 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.mat[u][v] -= path_flow 
                self.mat[v][u] += path_flow 
                v = parent[v] 
        return max_flow    

def solution(entrances, exits, paths):
    mat=matrix_generator(entrances, exits, paths)
    g = Network(mat) 
    collective_source = 0
    collective_sink = len(mat)-1
    print( (g.FordFulkerson(collective_source, collective_sink)) )

solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
