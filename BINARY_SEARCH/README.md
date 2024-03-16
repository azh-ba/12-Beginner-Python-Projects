**BINARY_SEARCH**

In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compuares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle lement to compare to the target value, and repeating this until the target value is found. If the searchends with the remining half being empty, the target is not in the array. [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

This project introduces and compares binary search algorithm to the normal search approach, which is looking through every element of the list.

> `binary_search.py`: Implements and executes binary search algorithm with a random-generated list of 10000 values. Also comparing time to the naive search side-by-side.