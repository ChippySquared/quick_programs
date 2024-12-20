# Shoe Size Finder

This program helps find the best-fitting shoe size from an unsorted list of available sizes. It uses a linear search algorithm to locate the first shoe size that fits or is larger than the specified foot size. If an exact match isn't found, the program suggests the closest available sizes. If no suitable size is available, it returns a message indicating the shoe size is not in stock.

## Features

- Validates input for foot size to ensure correctness.

- Finds the first shoe size that fits or is larger than the foot size.

- Suggests closest available sizes (e.g., half sizes up or down).

- Handles invalid foot size inputs gracefully.

## Scenario

Imagine you're shopping for shoes. The store has a list of shoe sizes in random order, and you want to find a size that fits. Since the store doesn’t organise the sizes in a sorted way, the program uses a linear search approach to locate the best fit.

## Input Requirements

- Foot size must be a positive number.

- Foot size must be a whole number or a half size (e.g., 5, 6.5).

- Invalid inputs (e.g., negative numbers, strings, or sizes with excessive decimals) will return an error message.


## How It Works

**Validation**: Checks if the foot size is a positive number, either a whole number or half size.

**Linear Search, O(n):** Iterates through the unsorted list of shoe sizes to find the first size that fits or is larger than the specified size.

**Alternatives:** Suggests the closest sizes if the exact size isn’t available.

**Output:** Provides a suitable response based on the search result.

## Why Linear Search?

The list of shoe sizes is unsorted.

Linear search is straightforward and efficient for small, unsorted datasets.

Prioritizes readability and simplicity over computational optimization.

## License

This project is open-source and free to use for educational or personal projects.