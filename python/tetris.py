# https://www.reddit.com/r/leetcode/comments/1f92vwa/matrix_coding_problem_tetris/
def add_up_pts(start, field, face):
    points = 0

    for row in range(len(field)):
        for col in range(len(field[0])):
            point = 1
            if field[row][col] == 1:
                continue
            elif start[0] + len(face) > row >= start[0] and start[1] + len(face[0]) > col >= start[1] and face[row - start[0]][col - start[1]] == 1:
                continue
            else:
                point -= 1
                break
        points += point

    return points

def valid(start, field, face):
    # for each 1 in face, can it be in field?
    for row in range(len(face)):
        for col in range(len(face)):
            if face[row][col] == 1:
                if field[start[0] + row][start[1] + col] == 1:
                    return False
                
    return True

def solve_tetris(field, face):
    max_pts = 0

    for i in range(len(field[1]) - len(face[1]) + 1):
        # test that location, see how many pts we get
        pts = 0

        start = [0, i]
        if not valid(start, field, face):
            continue

        while valid([start[0] + 1, start[1]], field, face):
            start[0] += 1

        # print(start)

        pts = add_up_pts(start, field, face)
        if pts > max_pts:
            max_pts = pts

    return max_pts

# example1: 
field = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1],
]
face = [[1, 1, 1], [0, 1, 1], [0, 1, 0]]
output = 2
print(solve_tetris(field, face), ' should equal ', output)

# example2:
field = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
face = [[1, 1, 1], [1, 0, 1], [1, 0, 1]]
output = 1
print(solve_tetris(field, face), ' should equal ', output)
