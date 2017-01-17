## A Collection of Dynamic Programming Problems
This is a collection of interesting algorithm problems written first recursively, then using memoization and finally a bottom-up approach.This allows to well capture the logic of dynamic programming.

### Dynamic Programming

The idea behind dynamic programming as describe in The Algorithm Design Manual (S. Skiena):
- Find the recursion in the problem
- Build a table of possible values
- Find the right order to evaluate the results so that partial results are available when needed.

There are two main approaches in the implementation of dynamic programming : 

#### Top Down - Memoization
When the recursion does a lot of unecessary calculation, an easy way to solve this is to cache the results and to check before executing the call if the result is already in the cache.

#### Bottom-Up
A better way to do this is to get rid of the recursion all-together by evaluating the results in the right order and building the array as we iterate. The partial results are available when needed if the iteration is done in the right order.

We have to identify and initialize the boundary conditions such as when we start the iteration, those are available.

We can most of the time optimize the space and avoid storing all the partial results along the way by storing only the stricly necessary partials. 


### Collection

For each problem, a simple recursion is presented together with a top down and a bottom-up approach. This allows to have a clear view of the logic of dynamic programming.

The simple recursion is very inefficient obviously and very limited in use, it is there for illustration only.

#### [Fibonnaci](https://github.com/tristanguigue/dynamic-programming/tree/master/fibonacci)
Finding the nth fibonacci number

Input: `4`

Output: `3`

#### [String Partition](https://github.com/tristanguigue/dynamic-programming/tree/master/partition_string)
The partition string problem retrieving the original string whose spaces were removed.
We are given a list of words belonging to a dictionary

Input: "carlosthinksthattheweatherisnice"

Output: "carlos thinks that the weather is nice"

#### [Counting Paths](https://github.com/tristanguigue/dynamic-programming/tree/master/count_path)
Count the number of possible paths from `(x1, y1)` to `(x2, y2)` by moving right or down

Input: `(0, 0, 1, 1)`

Output : `2`

#### [Largest Increasing Sequence](https://github.com/tristanguigue/dynamic-programming/tree/master/increasing_sequence)
Find the largest non-continuous increasing sequence from an array

Input: `[1, 6, 7, 4, 6, 1, 3, 4, 6, 19, 12, 14, 35, 66]`

Output: `[1, 3, 4, 6, 12, 14, 35, 66]`

Note that for this problem, the memoization solution is not available since the recursion access each partial solution once.




