##Name:Aman Mehra

def exclusive_min(d,Q):
    temp_d=[]
    temp_i=[]
    for i in range(len(d)):
        if i in Q:
            temp_d.append(d[i])
            temp_i.append(i)
    m=min(temp_d)
    indx=temp_d.index(m)
    pos=temp_i[indx]
    return (m,pos)

def dijkstra(con,wt,src=0):
    Q=range(len(con))
    dist=[float('inf') for i in range(len(con))]
    prev=list(dist)
    dist[src]=0
    while Q != []:
        if prev==dist:
            break
        prev=list(dist)
        u,posn=exclusive_min(dist,Q)
        ind=posn
        q_ind=Q.index(ind)
        del Q[q_ind]
        for i in range(len(con[ind])):
            alt=u+wt[ind][i]
            if alt<dist[con[ind][i]]:
                dist[con[ind][i]]=alt
    return dist

def bfs(con,wt,src=0):
    dist=[float('inf') for i in range(len(con))]
    prev=list(dist)
    dist[src]=0
    Q=[src]
    while len(Q)!=len(dist):
        if prev==dist:
            break
        prev=list(dist)
        for j in Q:
            temp_q=[]
            for i in range(len(con[j])):
                if con[j][i] not in Q:
                    alt=dist[j]+wt[j][i]
                    if alt<dist[con[j][i]]:
                        dist[con[j][i]]=alt
                    temp_q.append(con[j][i])
            Q.extend(temp_q)
    return  dist 
        
