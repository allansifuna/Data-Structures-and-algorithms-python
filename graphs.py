# -*- coding: utf-8 -*-
"""
Created on Sat March 21 10:10:24 2020

@author: allan sifuna,https://github.com/allansifuna
"""
class Node(object):
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,src,dest):
        self.dest=dest
        self.src=src

    def getDestination(self):
        return self.dest

    def getSource(self):
        return self.src

    def __str__(self):
        return f"{self.getSource()}-->{self.getDestination()}"

class Digraph(object):
    def __init__(self):
        self.edges={}
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node]=[]

    def addEdge(self,edge):
        src=edge.getSource()
        dest=edge.getDestination()

        if not(src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        else:
            self.edges[src].append(dest)

    def childrenOf(self,node):
        return self.edges[node]

    def hasNode(self,node):
        return node in self.edges

    def getNode(self,name):
        for n in self.edges:
            if n.getName()==name:
                return n
        raise NameError(name)

    def __str__(self):
        result=''
        for src in self.edges:
            for dest in self.edges[src]:
                result+=f"{src.getName()}->{dest.getName()}\n"
        return result[:-1]

class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev=Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self,rev)

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph,start,end,path,shortest,toPrint):
    path=path+[start]
    if toPrint:
        print(f"Current DFS Path:{printPath(path)}")
    if start==end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest==None or len(path)<len(shortest):
                newPath=DFS(graph,node,end,path,shortest,toPrint)
                if newPath!=None:
                    shortest=newPath
        elif toPrint:
            print(f"Already Visited {node}")
    return shortest

def shortestPath(graph, start, end, toPrint = True):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination),
                      toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)



printQueue = True

def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        if printQueue:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(printPath(p))
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
            print()
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)

testSP('Los Angeles', 'Phoenix')
