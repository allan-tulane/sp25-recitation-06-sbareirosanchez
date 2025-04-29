# CMPS 2200 Recitation 06
## Answers

**Name:** Sofia Bareiro
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
- **W(n) = W(n-1) + W(n-2) + O(1)**
- **This recurrence solves to W(n) = O(2^n), which reflects the exponential number of calls due to duplicate work.**

- **3)**
- **S(n) = max (S(n-1), S(n-2)) + O(1)**
- **Since each recursive call waits for both children to finish, the span is dominated by the longer branch. In the worst case, this gives: S(n)=O(n)**

- **4)**
- **The values in 'counts' resemble the Fibonacci sequence in reverse: 'counts[i]' approximates how often 'fib_recursive(i)' is called. This happens because the naive recursive approach recomputes the same subproblems many times, leading to exponential duplication.**

- **6)**
- **Each fib_top_down(i) is called at most once, since results are memoized. This, the total number of function calls is O(n).**
- **Work= O(n), because each value is computed only once.**
- **Span= O(n), due to the depth of recursive calls.**

- **8)**
- **Each value 'F[i]' is computed exactly once in order from 0 to n.**
- **Work= O(n), because there are n iterations.**
- **Span = O(1), since it is a sequential look with no recursion or dependency chains.**
