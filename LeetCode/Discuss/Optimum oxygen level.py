"""
After defeating Dr. Eggman, Sonic the Hedgehog has finally returned to the Green Hill Zone. The forest critters
make him the de facto king of the Hill for his victory. But unfortunately a new, more demanding problem awaits him;
The oxygen levels in the Zone are now unstable, and he has to evacuate all of his subjects to a safe area as soon as
possible.

Green Hill Zone is linear in geography and all the neighbourhoods in it are on a straight line. Each neighbourhood in
Green Hill Zone has an oxygen value assigned to it denoted by Oi. The oxygen value of a range of neighbourhoods l -> r
(both l and r inclusive) is calculated by the following equation derived by tails the fox:
O[l,r] = The bitwise AND of all the Oi values between both l and r.

To decide which neighbourhood or range of neighbourhoods is sade, Sonic has given a safe target oxygen value T to tails.
Help Tails prepare the safest range of neighbourhoods by finding the minimum possible value of |O[l,r] - T| where l <= r

Input format:
The first line contains N which is the number of neighbourhoods in Green Hill Zone
The next N lines contain N integers denoting the oxygen level Oi for each neighbourhood.
The last line contains T the target oxygen value.

Output:
An integer denoting the minimum possible value of |O[l,r] - T|
"""
def closest_to_target(oxygen_levels, target):
    min_diff = float('inf')

    for i in range(len(oxygen_levels)):
        and_value = oxygen_levels[i]
        min_diff = min(min_diff, abs(and_value - target))

        for j in range(i + 1, len(oxygen_levels)):
            and_value &= oxygen_levels[j]

            min_diff = min(min_diff, abs(and_value - target))
            if and_value == 0:
                break

        if min_diff == 0:
            break

    return min_diff

# Input
N = int(input())
oxygen_levels = [int(input()) for _ in range(N)]
target = int(input())

# Output
result = closest_to_target(oxygen_levels, target)
print(result)
