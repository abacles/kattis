class Graph:
    def __init__(self,nodes,edges):
        self.node_count=nodes
        self.edge_count=edges
        self.edge_list=[]
        self.node_list=[]
        for i in range(self.node_count):
            self.node_list.append(Graph.Node(i))
    class Node:
        def __init__(self,node_id):
            self.edges=[]
            self.visited=False
            self.cc=-1
            self.nid=node_id
        def reset(self):
            self.visited=False
            self.cc=-1
        def explore(self,nextcc):
            self.visited=True
            self.cc=nextcc
            for edge in self.edges:
                if not edge.visited:
                    edge.explore(nextcc)
        def explore_iter(self,nextcc):
            disc=[self]
            while disc!=[]:
                curr=disc.pop()
                if curr.visited:
                    continue
                curr.visited=True
                curr.cc=nextcc
                for edge in curr.edges:
                    if not edge.visited:
                        disc.append(edge)
    def reset(self):
        for node in self.node_list:
            node.reset()
    def get_graph(self):
        for i in range(self.edge_count):
            buff=[int(x) for x in input().split()]
            self.edge_list.append((self.node_list [buff [0]-1],self.node_list [buff [1]-1]))
            (self.node_list [buff [0]-1]).edges.append(self.node_list [buff [1]-1])
            (self.node_list [buff [1]-1]).edges.append(self.node_list [buff [0]-1])
    def dfs(self):
        self.reset()
        cc=0
        for node in self.node_list:
            if not node.visited:
                node.explore(cc)
                cc+=1
        return cc

houses,cables=input().split()
houses=int(houses)
cables=int(cables)
town=Graph(houses,cables)
town.get_graph()
town.node_list [0].explore_iter(0)
unconnected=[]
for house in town.node_list:
    if not house.visited:
        unconnected.append(house.nid+1)
if unconnected==[]:
    print('Connected')
else:
    unconnected.sort()
    for house in unconnected:
        print(house)
