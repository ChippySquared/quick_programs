# Scenario: we work for an e-commerce company that ships products in boxes of
# different sizes. The available box sizes (in cubic inches) are stored in
# a sorted list, and we need to pick the smallest box that can fit a given
# product's volume.

# Task:
# To write a function to find the smallest box size that can fit a given
# product. If no box can fit the product, return "No suitable box."


def find_smallest_box(box_sizes, product1_volume):  # Using descriptive names
    left = 0    # Assigning variable with index 0
    right = len(box_sizes) - 1     # Assigning variable with the last index of
                                   # box_sizes
    result = "No suitable box."

    while left <= right:   # Loop for counting from 0 to last index
        mid = (left + right) // 2   # We set the rules for a binary search
        if box_sizes[mid] >= product1_volume:  # Checking 1st condition
            result = box_sizes[mid]
            right = mid - 1  # Continue checking left
        else:
            left = mid + 1  # Continue checking right

    return result


# Example cases:
box_sizes = [100, 200, 300, 400, 500, 600]
is_box_suitable = find_smallest_box(box_sizes, 210)
print(is_box_suitable)
