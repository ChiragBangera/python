heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
heights2 = [4, 2, 0, 3, 2, 5]


def trap(height):
    l, r = 0, len(height) - 1
    max_left = height[l]
    max_right = height[r]

    total_units_stored = 0

    if len(height) == 0:
        return total_units_stored

    while l < r:

        if max_left <= max_right:
            l += 1
            max_left = max(max_left, height[l])
            total_units_stored += max_left - height[l]

        else:
            r -= 1
            max_right = max(max_right, height[r])
            total_units_stored += max_right - height[r]

    return total_units_stored


print(trap(heights))
