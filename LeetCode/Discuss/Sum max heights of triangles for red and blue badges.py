"""
Trailhead is a learning platform and for every trail that you complete, you earn a badge.
There are two colour of badges, based on the difficulty of the trail.
You are very passionate about these badges, and like arranging them in a triangle as follows:
    1. You put 1 red badge in the 1st row, then put 2 blue badges in the 2nd row, then 3 red badges in the 3rd row
        and so on.
    2. If the row of your triangle will not suffice from the badges available, that row will not be counted
        in the height. This keeps you striving to learn more.
    3. Whenever one color of your badges get over, and you have more badges of the other, you could either make the
        next row with it if possible or simple make another similar triangle with only the color left.
        Whichever maximizes the height sum of both triangles.
Can you tell him the sum of maximum possible heights of the triangles for N red badges and M blue badges?
"""


def solution():
    # Taking input for the number of red (N) and blue (M) badges
    """
    INPUT GIVEN IN A SINGLE LINE, SEPARATED BY SPACES:
    N, M = map(int, input().split())
    """

    """
    INPUT GIVEN IN TWO LINES, FIRST LINE IS N AND SECOND LINE IS M
    """
    N = int(input())
    M = int((input()))

    # Initialize variables
    n1, m1 = 1, 2  # Number of badges to be added in each row for red and blue triangles, respectively
    ans = 0  # Initialize the answer variable to store the sum of maximum heights
    i = 0  # Counter to alternate between red and blue triangles

    # Loop to calculate the height of the first triangle (alternating between red and blue)
    while True:
        if i % 2 == 0:  # If it's the turn for red triangle
            if N < n1:  # If remaining red badges are less than the required badges in the current row, break
                break
            else:
                ans += 1  # Increment the height of the triangle
                N -= n1  # Reduce the number of remaining red badges
                n1 += 2  # Increase the number of badges in the next row
                if N == 0:  # If all red badges are used, break
                    break
        else:  # If it's the turn for blue triangle
            if M < m1:  # If remaining blue badges are less than the required badges in the current row, break
                break
            else:
                ans += 1  # Increment the height of the triangle
                M -= m1  # Reduce the number of remaining blue badges
                m1 += 2  # Increase the number of badges in the next row
                if M == 0:  # If all blue badges are used, break
                    break
        i += 1  # Increment the counter to alternate between red and blue triangles

    # Loop to calculate the height of the second triangle using remaining red badges
    n1 = 1  # Reset the number of badges for the red triangle
    while True:
        if N < n1:  # If remaining red badges are less than the required badges in the current row, break
            break
        else:
            ans += 1  # Increment the height of the triangle
            N -= n1  # Reduce the number of remaining red badges
            n1 += 1  # Increase the number of badges in the next row

    # Loop to calculate the height of the second triangle using remaining blue badges
    m1 = 1  # Reset the number of badges for the blue triangle
    while True:
        if M < m1:  # If remaining blue badges are less than the required badges in the current row, break
            break
        else:
            ans += 1  # Increment the height of the triangle
            M -= m1  # Reduce the number of remaining blue badges
            m1 += 1  # Increase the number of badges in the next row

    return ans  # Return the sum of maximum heights of the triangles


# Call the solution function and print the result
if __name__ == '__main__':
    print("Sum of maximum possible heights of the triangles:", solution())
