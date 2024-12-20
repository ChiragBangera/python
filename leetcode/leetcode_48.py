def rotate_90(matrix):
    l, r = 0, len(matrix) - 1

    while l < r:
        top, bottom = l, r

        for i in range(r - l):

            # save the first value
            top_left = matrix[top][l + i]

            # moving bottom left point to the top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # moving bottom right value to the bottom left position
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # moving top right value to the bottom right value
            matrix[bottom][r - i] = matrix[top + i][r]

            # moving top left value to the top right position
            matrix[top + i][r] = top_left

        l += 1
        r -= 1
    return matrix


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(rotate_90(matrix))
