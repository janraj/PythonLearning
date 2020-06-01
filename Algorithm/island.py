'''
Problem:
	Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island.
	2D matrix contains only 0 and 1, where 1 indiacate land and 0 indicate water.
        Boarder are full of water.
Solution:
	Depth first search 
'''
class Island():
    def __init__(self, row, col, data):
        self.data = data
        self.row = row
        self.col = col
        self.data = data
        self.dfsdata = data
        self.total_island = 0
    def DepathFirstSearch(self, i, j):
        if self.dfsdata[i][j] == 1:
            self.dfsdata[i][j] = 2
            if ((j+1 < self.row) and self.dfsdata[i][j+1] == 1):
                self.DepathFirstSearch(i, j+1)
            if ((i+1 < self.row) and self.dfsdata[i+1][j] == 1):
                self.DepathFirstSearch(i+1, j)
            if (i-1 >=0 and self.dfsdata[i-1][j] == 1):
                self.DepathFirstSearch(i-1, j) 
            if (j-1 >=0 and self.dfsdata[i][j-1] == 1):
                self.DepathFirstSearch(i, j-1)
        
    def totalIsland(self):
        for i in range(self.row):
            for j in range(self.col):
                if (self.dfsdata[i][j] == 1):
                    self.total_island = self.total_island + 1
                    self.DepathFirstSearch(i, j)   
                    print("Modified Graph", obj.dfsdata)
		 
        return self.total_island


if __name__ == "__main__":
    graph = [[1, 1, 0, 0, 0], 
             [0, 1, 0, 0, 1], 
             [1, 0, 0, 1, 1], 
             [0, 0, 0, 0, 0], 
             [1, 0, 1, 0, 1]] 
    obj=Island(5, 5, graph)
    tot = obj.totalIsland()
    print("Total Island is", tot)
