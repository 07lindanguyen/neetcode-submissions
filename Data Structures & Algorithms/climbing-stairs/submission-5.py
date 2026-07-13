class Solution:
    def climbStairs(self, n: int) -> int:
        # sounds like combinatronics in probability
        # TWO BRANCH: 2 RECURSIVE CALLS
        # looks like Fibonacci Sequence?
        if n <= 2:
            return n
        # Initialize the two most recent values of the Fibonacci-like sequence:
        prev1 = 2 # ways(2)
        prev2 = 1 # ways(1)
        # Compute f(3), f(4), ..., f(n) iteratively
        for i in range(3, n+1):
            current = prev1 + prev2  # f(i) = f(i-1) + f(i-2)
            # Slide the window: shift prev2 forward to old prev1,
            prev2 = prev1
            # and prev1 forward to the newly computed value.
            prev1 = current
        # After the loop, prev1 holds f(n).
        return prev1
        