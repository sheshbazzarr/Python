Convert the mathematical function $f(n) = a^n$ into a recursive function.

In mathematics, $a^n$ denotes "$a$ raised to the power of $n$", which means multiplying $a$ by itself $n$ times. Your task is to create a function that takes two arguments, `a` and `n`, and calculates $a^n$ using recursion.

For example:
- If `a` is `2` and `n` is `3`, the function should return `8`, because $2^3$ = 2 x 2 x 2 = 8.
- If `a` is `5` and `n` is `0`, the function should return `1`, since any number raised to the power of 0 is 1.



#solutions:

- Base case: When `n` is `0`, return `1`, because any number raised to the power of 0 is 1.
- Recursive case: Otherwise, return `a` multiplied by `power(a, n-1)`, reducing the problem in each step.
