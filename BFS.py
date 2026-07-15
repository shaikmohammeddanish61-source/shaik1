from queue import Queue

def bfs(grapg,source):
    que = Queue()
    visited = []
    que.put(source)
    visited.append(source)
    
    while not que.empty():        
        vertex = que.get()
        print(vertex, end=" ")
        for u in graph[vertex]:
            if u not in visited:
                que.put(u)
                visited.append(u)
                
graph = {'A': ['B','D'], 
         'B': ['C', 'F'],
         'C':['E','G','H'],
         'D': ['F'], 
         'E': ['B', 'F'],                                                                                                                          
         'F': ['A'],
         'G': ['E', 'H'],
         'H': ['A']
         }

print("Given Graph " , graph)

print("\nBFS Traversal \n")
bfs(graph,"H")
graph={'A':['B','D'],'B':['C','F'],'C':['E','G','H'],'D':['F'],'E':['B','F'],'F':['A'],'G':['E','H'],'H':['A']}