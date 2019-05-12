import xlrd

def run_shortest_distance(d):
    # Source: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
    dist = d
    V = len(d)
    global nex
    
    for i in range(V):
        for j in range(V):
            nex[i][j] = j
    
    print("Started run.")
    for k in range(V): 
        for i in range(V): 
            for j in range(V):
                possible = dist[i][k]+ dist[k][j]
                if possible < dist[i][j]:
                    dist[i][j] = possible
                    nex[i][j] = nex[i][k]

    print("Finished run.")
    return nex, dist

def get_path(i, j):
    path = [i]
    while i!=j:
        print("->",i,j,path)
        i = nex[i][j]
        print("****",i,j,path)
        if i in path:
            if j not in path:
                path.append(j)
            break
        path.append(i)
    return path
        
def initialize_next(d):
    nex = []
    t = []
    for i in range(d):
        t.append([])
    for i in range(d):
        nex.append(t)
    return nex

if __name__ == "__main__":
    try:
        sheet = xlrd.open_workbook(".\Honors Research Data.xlsx").sheet_by_index(0)
        print("Sheet imported.")
    except:
        print("Error! Cannot open sheet.")

    d = []

    for i in range(1, sheet.nrows):
        row = []
        for j in range(1, sheet.ncols):
            val = sheet.cell_value(j,i)
            if val == '':
                val = 9999
            row.append(val)
        d.append(row)
    print("Data read.")

    nex = initialize_next(len(d))
    
    if len(d) == 0:
        print("Error! Dataset empty.")
    else:
        # shortest distance between points
        ans = run_shortest_distance(d)
        # shortest paths
        
