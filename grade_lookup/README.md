# Student Grade Lookup

This project demonstrates a simple use case for a hash table (implemented as a Python dictionary) to store and retrieve student grades efficiently. The example includes adding grades, looking them up by student name, and updating existing grades.

## Features
- **Add Student Grades**: Insert student names and their corresponding grades into a hash table.
- **Lookup Grades**: Retrieve a student's grade in constant time.
- **Handle Missing Records**: Gracefully manage cases where the requested student's grade does not exist.

## Key Concepts
- **Hash Table**: The dictionary maps student names (keys) to grades (values).
- **Efficiency**: Operations like insertion and lookup run in constant time O(1) on average.
- **Graceful Error Handling**: The script checks if a student's name exists in the dictionary before attempting to access their grade.

## Applications
- **Education Systems**: Quickly retrieve student grades.
- **Real-Time Systems**: Use hash tables to manage and search data efficiently.