from copy import deepcopy


def print_3d(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            st = "["

            for k in range(len(m[i][j])):
                st += str(m[i][j][k])
                st += " " if k != len(m[i][j]) - 1 else ""

            print("{0:19}".format(st + "]"), end=' ')
        print()
        if (i+1) % 3 == 0:
            print()


def clear_positions(pos, i, j, val):
    for k in range(i // 3 * 3, i // 3 * 3 + 3):
        for l in range(j // 3 * 3, j // 3 * 3 + 3):
            if val in pos[k][l]:
                if i != k and j != l:
                    pos[k][l].remove(val)

    for k in range(9):
        if k != i and val in pos[k][j]:
            pos[k][j].remove(val)

        if k != j and val in pos[i][k]:
            pos[i][k].remove(val)


def solve(m):
    pos = [[[i for i in range(1, 10)] for _ in range(9)] for _ in range(9)]
    marked = [[False for _ in range(9)] for _ in range(9)]
    total_marked, history = 0, [{}]

    for i in range(9):
        for j in range(9):
            if m[i][j] != 0:
                total_marked += 1
                marked[i][j] = True
                pos[i][j] = [m[i][j]]
                clear_positions(pos, i, j, m[i][j])

    print_3d(pos)

    while total_marked < 81:
        min_pos, min_i, min_j = 9, 0, 0

        for i in range(9):
            for j in range(9):
                if not marked[i][j] and len(pos[i][j]) < min_pos:
                    min_pos = len(pos[i][j])
                    min_i, min_j = i, j

        if min_pos > 1:
            val = pos[min_i][min_j].pop()

            history.append({
                "remain": pos[min_i][min_j],
                "pos": deepcopy(pos),
                "marked": deepcopy(marked),
                "total_marked": total_marked,
                "i": min_i,
                "j": min_j
            })

            pos[min_i][min_j] = [val]

        elif min_pos == 0:
            val = history[len(history) - 1]["remain"].pop()
            min_i, min_j = history[len(history) - 1]["i"], history[len(history) - 1]["j"]
            total_marked = history[len(history) - 1]["total_marked"]

            pos = deepcopy(history[len(history) - 1]["pos"])
            marked = deepcopy(history[len(history) - 1]["marked"])

            pos[min_i][min_j] = [val]

            if len(history[len(history) - 1]["remain"]) == 0:
                history.pop()

        marked[min_i][min_j] = True
        total_marked += 1
        clear_positions(pos, min_i, min_j, pos[min_i][min_j][0])

    print_3d(pos)

if __name__ == '__main__':
    s = [
        [3, 0, 4, 0, 0, 0, 0, 0, 0],
        [6, 0, 1, 8, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9],

        [0, 0, 0, 0, 9, 6, 4, 0, 0],
        [0, 7, 0, 0, 2, 0, 0, 5, 0],
        [0, 0, 6, 1, 8, 0, 0, 0, 0],

        [2, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 1, 8, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 5]
    ]

    solve(s)


