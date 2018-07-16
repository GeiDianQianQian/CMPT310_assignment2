

def findNeighbor(v,k,G,color):
    list = []
    for i in range (1,k):
        list.append(i)
    print ("haha")
    print list

    for j in range (1,len(G[v-1])):
        if color[G[v-1][j]] != 0:
            list.remove(color[G[v-1][j]]);
    if not list:
        return -1;
    else:
        return colors[0];


def solve(n, k, G):
    color = [0]*n
    color[1] = 1
    tup = ()
    list = []
    for i in range (1,n):
        length = len(G[i-1]);
        for j in range (1,length):
            color[G[i-1][j]] = findSafe(i,k,G,color)
            if color[G[i-1][j]] == -1:
                print ("[]")
                break;
        tuple(i,color[i])
        list.append(tuple)



    return list

G = [[1,2,3], [2,1,3], [3,1,2], [4,5], [5,4]] # a list of lists
n = 5  # number of vertices
k = 3  # number of colours
lists = []
lists = solve(n,k,G)
print lists
