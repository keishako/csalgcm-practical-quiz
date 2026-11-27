import pandas as pd

# filename = "grouped_words.csv"

# using libraries
'''
import Levenshtein
def lev_dist(a, b):
   distance = Levenshtein.distance(a,b)
   return distance
'''

# w/o libraries
def edit_table(a, b):
    m, n = len(a), len(b)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # Initialize base cases
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    # Fill the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i-1][j] + 1,      # deletion
                dp[i][j-1] + 1,      # insertion
                dp[i-1][j-1] + cost  # substitution
            )

    return dp


def levenshtein_distance(a, b):
    return edit_table(a, b)[len(a)][len(b)]

'''
if __name__ == "__main__":
    df = pd.read_csv(filename, encoding="utf-8")

    groups = (
        df.iloc[:,0]
    )
'''


