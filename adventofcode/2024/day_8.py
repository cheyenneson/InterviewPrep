input = open('input/day_8_input.txt', 'r')
# 289 is too low
graph = []
nodes = {}
row = 0

def print_graph(graph):
    for arr in graph:
        print(''.join(arr))

def find_antinodes_2(graph, node1, node2):
    x1, y1, x2, y2 = node1[0], node1[1], node2[0], node2[1]
    antinodes = []
    x_diff = abs(node1[0] - node2[0])
    y_diff = abs(node1[1] - node2[1])

    while 1:
        # set the x's
        if x1 > x2:
            x1 = x1 + x_diff
            x2 = x2 - x_diff
        elif x1 < x2:
            x1 = x1 - x_diff
            x2 = x2 + x_diff
        # set the y's
        if y1 > y2:
            y1 = y1 + y_diff
            y2 = y2 - y_diff
        elif y1 < y2:
            y1 = y1 - y_diff
            y2 = y2 + y_diff
        
        if 0 <= x1 < len(graph) and 0 <= y1 < len(graph[0]):
            antinodes.append((x1, y1))
        if 0 <= x2 < len(graph) and 0 <= y2 < len(graph[0]):
            antinodes.append((x2, y2))
        if not (0 <= x1 < len(graph) and 0 <= y1 < len(graph[0])) and not (0 <= x2 < len(graph) and 0 <= y2 < len(graph[0])):
            break

    return antinodes

def find_antinodes(node1, node2):
    x1, y1, x2, y2 = 0, 0, 0, 0
    x_diff = abs(node1[0] - node2[0])
    y_diff = abs(node1[1] - node2[1])

    # set the x's
    if node1[0] > node2[0]:
        x1 = node1[0] + x_diff
        x2 = node2[0] - x_diff
    if node1[0] < node2[0]:
        x1 = node1[0] - x_diff
        x2 = node2[0] + x_diff
    # set the y's
    if node1[1] > node2[1]:
        y1 = node1[1] + y_diff
        y2 = node2[1] - y_diff
    if node1[1] < node2[1]:
        y1 = node1[1] - y_diff
        y2 = node2[1] + y_diff

    return [(x1, y1), (x2, y2)]

for line in input:
    line = line.strip()
    arr = list(line)
    graph.append(arr)

    for col in range(len(arr)):
        char = arr[col]
        if char != '.':
            if char not in nodes:
                nodes[char] = []
            nodes[char].append((row, col))

    row += 1

# make a copy of graph to separate parts I and II
graph_1 = [x[:] for x in graph]
count = 0   
for frequency in nodes:
    for i in range(len(nodes[frequency])):
        for j in range(i + 1, len(nodes[frequency])):
            node1, node2 = nodes[frequency][i], nodes[frequency][j]

            # calc the position of the two antinodes between each two nodes
            antinodes = find_antinodes(node1, node2)

            # add the antinodes, increment the count if there isn't already an antinode there
            for antinode in antinodes:
                # if has a spot on the graph and doesn't already have a #
                if 0 <= antinode[0] < len(graph_1) and 0 <= antinode[1] < len(graph_1[0]) and graph_1[antinode[0]][antinode[1]] != '#':
                    count += 1
                    graph_1[antinode[0]][antinode[1]] = '#'

print("Part I:", count)

# Part II
for frequency in nodes:
    if len(nodes[frequency]) > 1:
        for node in nodes[frequency]:
            graph[node[0]][node[1]] = '#'

    for i in range(len(nodes[frequency])):
        for j in range(i + 1, len(nodes[frequency])):
            node1, node2 = nodes[frequency][i], nodes[frequency][j]

            # calc the position of the two antinodes between each two nodes
            antinodes = find_antinodes_2(graph, node1, node2)

            # add the antinodes, increment the count if there isn't already an antinode there
            for antinode in antinodes:
                # if has a spot on the graph and doesn't already have a #
                if graph[antinode[0]][antinode[1]] != '#':
                    graph[antinode[0]][antinode[1]] = '#'

count = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == '#':
            count += 1

print("Part II:", count)

