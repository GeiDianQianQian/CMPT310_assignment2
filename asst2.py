def getNumber(v,k,G,color):
    list = []
    for i in range (1,k+1):
        list.append(i)
    #print list

    for j in range (1,len(G[v-1])):
        #print "j",j
        #print "G[v-1][j]:",G[v-1][j]
        if G[v-1][j] < v :
            #print color
            #print "neighbor:",G[v-1][j]
            if color[G[v-1][j]] in list:
                list.remove(color[G[v-1][j]]);
                #print list
    if not list:
        return -1;
    else:
        return list[0];




def solve(n, k, G):
    color = [0]*(n+1)
    #print color
    color[1] = 1
    list = []
    for i in range (1, n+1):
        #print ("-----")

        if getNumber(i,k,G,color) == -1:
            list = []
            break
        else:
            color[i] = getNumber(i,k,G,color)
            #print ("i: ", i," color:", color[i])
            # for j in range (1,len(G[i-1])):
            #     if color[i] < k and G[i-1][j] > i:
            #         color[G[i-1][j]] = color[i] +1
            #         #print ("[G[i-1][j]]:",[G[i-1][j]]," color[G[i-1][j]]: ", color[G[i-1][j]])
            #     elif color[i] == k and G[i-1][j] > i:
            #         color[G[i-1][j]] = 1
            tup = (i,color[i])
            list.append(tup)
    return list



#
# G = [[1,2,3], [2,1,3], [3,1,2], [4,5], [5,4]] # a list of lists
# n = 5  # number of vertices
# k = 3  # number of colours

G = [[1,2,3,4,6,7,10], [2,1,3,4,5,6], [3,1,2], [4,1,2], [5,2,6],
[6,1,2,5,7,8],[7,1,6,8,9,10],[8,6,7,9],[9,7,8,10],[10,1,7,9]] # a list of lists
n = 10  # number of vertices
k = 4  # number of colours
list = []
list = solve(n, k, G)

print list
