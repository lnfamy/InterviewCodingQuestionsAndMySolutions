"""
2.In the game of cricket, players can score runs by hitting the ball delivered at them(by another player called bowler) and running between designated spots(wickets).

suppose if a player is only allowed to score 1,2,4 and 6 runs in a ball.How many ways the player can score N runs without hitting consecutive 4s?

for ex, to score 4 runs, the player can hit the runs in subsequent balls in the following ways.
1,1,1,1

1,1,2

1,2,1

2,1,1

2,2

4

Output=6
"""
def count_ways(score):
    return _count_ways(score, False, {})

def _count_ways(score, flag, cache):
    key = str(score) + "->" + str(flag)
    if key in cache:
        return cache[key]
    if score == 0:
        return 1
    if score < 0:
        return 0

    sum = 0
    if not flag:
        sum = sum + _count_ways(score - 1, False, cache) \
                + _count_ways(score - 2, False, cache) \
                + _count_ways(score - 4, True, cache) \
                + _count_ways(score - 6, False, cache)
    else:
        sum = sum + _count_ways(score - 1, False, cache) \
                + _count_ways(score - 2, False, cache) \
                + _count_ways(score - 6, False, cache)

    cache[key] = sum
    return sum


if __name__ == '__main__':
    # Example usage
    score = 4
    print(count_ways(score))  # Output: 6
