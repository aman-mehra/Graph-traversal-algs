##Name:Aman Mehra

from BnD import *
##TASK1:
print "TASK1"
print "__________________________________________________"
print
print "Test1"
connections=[[1, 2], [3], [1, 3, 4], [], [3]]
weights=[[5, 3], [3], [2, 5, 6], [], [1]]
#Dijkstra-0,5,3,8,9
#Bfs-0,5,3,8,9
dis=dijkstra(connections,weights)
di=bfs(connections,weights)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis==di,"Error!"
print "OK"
print "__________________________________________________"

print "Test2"
connections=[[1, 2], [3], [1, 3, 4], [], [3]]
weights=[[5, 2], [3], [2, 5, 6], [], [1]]
#Dijkstra-0,4,2,7,8
#Bfs-0,5,2,8,8
dis=dijkstra(connections,weights)
di=bfs(connections,weights)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis!=di,"Error!"
print "OK"
print "__________________________________________________"

print "Test3"
connections=[[1, 2], [3], [1, 3, 4], [], [3]]
weights=[[5, 2], [3], [1, 5, 6], [], [1]]
#Dijkstra-inf,1,0,4,6
#Bfs-inf,1,0,5,6
dis=dijkstra(connections,weights,src=2)
di=bfs(connections,weights,src=2)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis!=di,"Error!"
print "OK"
print "__________________________________________________"

print "Test4"
connections=[[1,2,3], [2,4], [1, 4], [4], []]
weights=[[3,5,6], [1,10], [1,5], [3],[]]
#Dijkstra-inf,1,0,inf,5
#Bfs-inf,1,0,inf,5
dis=dijkstra(connections,weights,src=2)
di=bfs(connections,weights,src=2)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis==di,"Error!"
print "OK"
print "__________________________________________________"

print "Test5"
connections=[[1,2,3], [2,4], [1, 4], [4], []]
weights=[[3,5,6], [1,10], [1,5], [3],[]]
#Dijkstra-0,3,4,6,9
#Bfs-0,3,5,6,13
dis=dijkstra(connections,weights)
di=bfs(connections,weights)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis!=di,"Error!"
print "OK"
print "__________________________________________________"

##TASK2
print "TASK2"
print "__________________________________________________"
print
print "Test1"
connections=[[1, 2], [3], [1, 3, 4], [], [3]]
weights=[[1, 1], [1], [1, 1, 1], [], [1]]
#Dijkstra-0,1,1,2,2
#Bfs-0,1,1,2,2
dis=dijkstra(connections,weights)
di=bfs(connections,weights)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis==di,"Error!"
print "OK"
print "__________________________________________________"

print "Test2"
connections=[[1, 2], [3], [1, 3, 4], [], [3]]
weights=[[1,1], [1], [1,1,1], [], [1]]
#Dijkstra-inf,1,0,1,1
#Bfs-inf,1,0,1,1
dis=dijkstra(connections,weights,src=2)
di=bfs(connections,weights,src=2)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis==di,"Error!"
print "OK"
print "__________________________________________________"

print "Test3"
connections=[[1,2,3], [2,4], [1, 4], [4], []]
weights=[[1,1,1], [1,1], [1,1], [1],[]]
#Dijkstra-inf,1,0,inf,1
#Bfs-inf,1,0,inf,1
dis=dijkstra(connections,weights,src=2)
di=bfs(connections,weights,src=2)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis==di,"Error!"
print "OK"
print "__________________________________________________"

print "Test4"
connections=[[1,2,3], [2,4], [1, 4], [4], []]
weights=[[1,1,1], [1,1], [1,1], [1],[]]
#Dijkstra-0,1,1,1,2
#Bfs-0,1,1,1,2
dis=dijkstra(connections,weights)
di=bfs(connections,weights)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
assert dis==di,"Error!"
print "OK"
print "__________________________________________________"

print "Testing exclusive_min"
print "__________________________________________________"
print "Test1"
assert exclusive_min([1,3,4,9],[1,2,3])==(3,1),"Error!"
print "OK"
print "__________________________________________________"
print "Test2"
assert exclusive_min([7,7,float('inf'),9],[1,2,3])==(7,1),"Error!"
print "OK"
print "__________________________________________________"
print "Test3"
assert exclusive_min([100,4,7,float('inf'),9],[0,3])==(100,0),"Error!"
print "OK"
print "__________________________________________________"


print "Lab test 1"
connections=[[4], [0], [1, 3], [1], [3]]
weights=[[10], [7], [6,3], [2],[5]]
dis=dijkstra(connections,weights)
weights=[[1],[1],[1,1],[1],[1]]
di=bfs(connections,weights)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
print "OK"
print "__________________________________________________"

print "Lab test 2"
connections=[[], [0], [1], [0,1]]
weights=[[], [6], [3], [8,1]]
dis=dijkstra(connections,weights)
weights=[[],[1],[1],[1,1]]
di=bfs(connections,weights)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
print "OK"
print "__________________________________________________"

print "Lab test 3"
connections=[[4,1,3,2], [0,3,2], [1,0,4], [4,0,2,1], [0,3,2]]
weights=[[6,5,11,6], [5,6,8], [8,1,2], [9,11,10,2],[6,9,2]]
dis=dijkstra(connections,weights)
weights=[[1,1,1,1],[1,1,1],[1,1,1],[1,1,1,1],[1,1,1]]
di=bfs(connections,weights)
print "%10s %10s %10s"%('Node','Dijkstra','Bfs')
for i in range(len(di)):
    print "%10s %10s %10s"%(str(i),str(dis[i]),str(di[i]))
print "OK"
print "__________________________________________________"



