class Vertex():
    visitCount = 0

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            # self.neighbors.sort()

    def print(self):
        print(self.name, self.visitCount, len(self.neighbors))
        for neighbor in self.neighbors:
            print("   ===>", neighbor)


class Graph():
    vertices = {}

    def print(self):
        for vertex in self.vertices:
            self.vertices[vertex].print()

    def bfs(self, vertex, visitIndex=1):
        q = list()
        if vertex.visitCount != 0:
            return False

        vertex.visitCount = islandCount

        for neighbor in vertex.neighbors:
            neighbor = self.vertices[neighbor]
            q.append(neighbor.name)

        while len(q) > 0:
            v = q.pop(0)
            v = self.vertices[v]

            if v.visitCount == 0:
                v.visitCount = 1
                for neighbor in v.neighbors:
                    neighbor = self.vertices[neighbor]
                    if neighbor.visitCount == 0:
                        q.append(neighbor.name)

        return True


earth = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0]
]

g = Graph()

for i, r in enumerate(earth):
    for j, e in enumerate(earth[i]):
        if earth[i][j] == 1:
            name = str(i) + "-" + str(j)
            v = Vertex(name)
            g.vertices[name] = v

for i, r in enumerate(earth):
    for j, e in enumerate(earth[i]):
        if earth[i][j] == 1:
            name = str(i) + "-" + str(j)
            if i > 0 and earth[i-1][j] == 1:
                nabourName = str(i-1) + "-" + str(j)
                g.vertices[name].add_neighbor(nabourName)
            if j > 0 and earth[i][j-1] == 1:
                nabourName = str(i) + "-" + str(j-1)
                g.vertices[name].add_neighbor(nabourName)
            if i < (len(earth)-1) and earth[i+1][j] == 1:
                nabourName = str(i+1) + "-" + str(j)
                g.vertices[name].add_neighbor(nabourName)
            if j < (len(earth[i])-1) and earth[i][j+1] == 1:
                nabourName = str(i) + "-" + str(j+1)
                g.vertices[name].add_neighbor(nabourName)

# g.print()
islandCount = 1

for v in g.vertices:
    c = g.bfs(g.vertices[v], islandCount)
    if c is True:
        islandCount = islandCount + 1

print("Island Count =", islandCount - 1)
