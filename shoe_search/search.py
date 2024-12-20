# Scenario: we're shopping for a pair of shoes. The store has a list of shoe
# sizes in random order, but we only want to find the first shoe size that
# fits or is larger than our foot size. The store clerk doesn’t organise the
# shoe sizes, so we must check each size sequentially.

# Task:
# Write a program using linear search to find the shoe size that
# is equal to your foot size. If no exact shoe size fits your foot size,
# suggest whether closest sizes are available, and if none,
# return "Shoe size not in stock."

# Approach: will make use of linear search as the data is unsorted, small,
# and can be easier to understand (readability).

def find_shoe_size(shoe_sizes, foot_size):
    if foot_size <= 0 or (foot_size * 2) % 1 != 0 or \
            not isinstance(foot_size, (int, float)):
        error_msg = ("Invalid foot size. Please enter whole numbers "
                     "greater than 0 (e.g., 5, 6), or half sizes "
                     "(e.g., 4.5, 7.5).")
        return error_msg    # We add a case of invalid foot_size values

    result = None

    for size in shoe_sizes:     # Linear search loop to iterate through each
        if size >= foot_size:   # shoe size to find best fit.
            if result is None or size < result:
                result = size

    if result is None:    # Handling a no-shoe-match case.
        return "Shoe size not in stock."

    if result != foot_size:       # Conditional for suggesting closest shoe
        alternative_sizes = []    # sizes if exact foot size isn't in stock.
        if foot_size + 0.5 in shoe_sizes:
            alternative_sizes.append(foot_size + 0.5)
        if foot_size - 0.5 in shoe_sizes:
            alternative_sizes.append(foot_size - 0.5)
        return (
            "Whilst the exact shoe size ins't in stock, the closest "
            f"available shoe sizes are "
            f"{', '.join(map(str, alternative_sizes))}"
        )

    return f"Shoe size {result} is in stock."


# We add an example list here.
shoe_sizes = [8, 5, 12, 7, 6, 11, 4, 13, 9, 10,]
shoe_availability = find_shoe_size(shoe_sizes, 13)
print(shoe_availability)
