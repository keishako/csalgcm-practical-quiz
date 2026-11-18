from edit_distance import edit_table

def find_differences(a, b):
    dp = edit_table(a, b)
    i, j = len(a), len(b)
    path = []

    while i > 0 or j > 0:
        cost = 1
        if i > 0 and j > 0 and a[i-1] == b[j-1]:
            cost = 0

        if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + cost:     # diagonal
            path.append((a[i-1], b[j-1]))
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:  # up
            path.append((a[i-1], ""))
            i -= 1
        else:                                   # left
            path.append(("", b[j-1]))
            j -= 1

    path.reverse()

    # keeping differences only
    diffs =[]
    part_a, part_b = "", ""

    for letter_a, letter_b in path:
        if letter_a == letter_b:   # if same letter
            if part_a or part_b:  # if difference being built, save
                diffs.append((part_a, part_b))
                part_a, part_b = "", ""
        else:           # different letter
            part_a += letter_a      # add current difference
            part_b += letter_b

    if part_a or part_b:  # save
        diffs.append((part_a, part_b))

    return diffs
