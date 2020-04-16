class Project_manager:
    def __init__(self):
        pass

    def read(self, fileName):
        graph = []
        file = open(fileName, 'r')
        n = int(file.readline(100))
        for i in range(1, n + 1):
            line = file.readline(10000)
            line = line.replace('\n', '')
            line = line.split(',')
            node = []
            for j in range(0, n):
                if int(line[j]) != 0:
                    node.append((j + 1, int(line[j])))
            graph.append(node)
        start = int(file.readline(100))
        end = int(file.readline(100))
        file.close()
        return (graph, start, end)

    def getPairs(self, list):
        pairs = []
        for i in range(0, len(list)):
            for j in range(0, len(list[i])):
                pairs.append(((i + 1, list[i][j][0]), list[i][j][1]))
        pairs.sort(key = lambda x:x[1])
        return pairs

    def getPath(self, start, current, pairs, path, visited, n):
        i = 0
        if len(path) == 0:
            j = 0
            while pairs[j][0][0] != start:
                j = j + 1
            path = [pairs[j]]
            visited = [start, pairs[j][0][1]]
        while i < len(pairs) and (pairs[i][0][0] != pairs[current][0][1] or pairs[i][0][1] in visited):
            i = i + 1
        if i >= len(pairs):
            return False, 0, path
        path.append(pairs[i])
        visited.append(pairs[i][0][1])
        exist = False
        dist = 0
        for node in pairs:
            if node[0][0] == pairs[i][0][0] and start == node[0][1]:
                exist = True
                dist = node[1]
        if len(visited) == n and exist:
            return True, dist, path
        else:
            found, dist, path = self.getPath(start, i, pairs, path, visited, n)
            if not found:
                current = current + 1
                path.pop(len(path) - 1)
                visited.pop(len(visited) - 1)
                return False, dist, self.getPath(start, current, pairs, path, visited, n)
            else:
                return found, dist, path

    def search_total_path(self, start, list):
        pairs = self.getPairs(list)
        i = 0
        while pairs[i][0][0] != start:
            i = i + 1
        path = [pairs[i]]
        visited = [start, pairs[i][0][1]]
        found, dist, path = self.getPath(start, 0, pairs, path, visited, len(list))
        length = dist
        nodes = [start]
        for node in path:
            nodes.append(node[0][1])
            length = length + node[1]
        return length, nodes


    def search_path(self, start, elem, list):
        distances = []
        parents = []
        for i in range(0, len(list)):
            distances.append(float("Inf"))
            parents.append(0)
        distances[start - 1] = 0
        toVisit = [(start, 0)]
        while len(toVisit) != 0:
            node = toVisit.pop(0)
            for i in list[node[0] - 1]:
                if distances[i[0] - 1] > distances[node[0] - 1] + i[1]:
                    distances[i[0] - 1] = distances[node[0] - 1] + i[1]
                    toVisit.append(i)
                    parents[i[0] - 1] = node[0]
            toVisit.sort(key = lambda x: x[1])
        return (distances[elem - 1], parents)

    def get_length(self):
        f=open("output.txt","r")
        lines=f.readlines()

        return lines[0]

    def get_target(self):
        with open('output.txt') as f:
            array = [[int(x) for x in line.split()] for line in f]
        return array

    def solution(self, input, output):
        graph, start, end = self.read(input)
        length, path = self.search_total_path(1, graph)
        file = open(output, 'w')
        file.write(str(len(graph)) + "\n")
        for node in path:
            file.write(str(node) + " ")
        file.write("\n" + str(length) + "\n")
        length, parents = self.search_path(start, end, graph)
        path = [end]
        node = parents[end - 1]
        while node != start:
            path.insert(0, node)
            node = parents[node - 1]
        path.insert(0, start)
        file.write(str(len(path)) + "\n")
        for node in path:
            file.write(str(node) + " ")
        file.write("\n" + str(length))
        file.close()
