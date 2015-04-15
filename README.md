# Dynamic Programing Problems

## Dynamic Programing
This is a collection of interesting algorithm problems meant to illustrate the variety and simplicity of the dynamic programing approach.

The idea behind dynamic programing as describe in The Algorithm Design Manual (S. Skiena) 

- Find the recursion in the problem
- Build a table of possible values
- Find the right order to evaluate the results so that partial results are available when needed.

There are two main approaches in the implementation of dynamic programming : 

### Top Down - Memoization
When the recursion does a lot of unecessary calculation, an easy way to solve this is to cache the results and to check before executing the call if the result is already in the cache.

### Bottom-Up
A better way to do this is to get rid of the recursion all-together by evaluating the results in the right order and building the array as we iterate. The partial results are available when needed if the iteration is done in the right order.

We have to identify and initialize the boundary conditions such as when we start the iteration, those are available.

We can most of the time optimize the space and avoid storing all the partial results along the way by storing only the stricly necessary partials. 


## Collection

For each problem, a simple recursion is presented together with a top down and a bottom-up approach. This allows to have a clear view of the different steps of dynamic programing.

The simple recursion is very inefficient obviously and very limited in use, it is there for illustration.