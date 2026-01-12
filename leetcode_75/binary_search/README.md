# 374. Guess Number Higher or Lower

**Difficulty:** Easy  
**Topic:** Binary Search  
**LeetCode Problem:** [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

---

## Problem Description

We are playing the Guess Game. I pick a number from `1` to `n`. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:
- `-1`: Your guess is higher than the number I picked (i.e. `num > pick`)
- `1`: Your guess is lower than the number I picked (i.e. `num < pick`)
- `0`: Your guess is equal to the number I picked (i.e. `num == pick`)

Return the number that I picked.

---

## Solution Approach: Binary Search

### Algorithm

This is a classic binary search problem where we need to find a target number in the range `[1, n]`.

**Key Idea:**
- Start with the full range `[1, n]`
- Pick the middle element
- Use the `guess()` API to check if our guess is correct, too high, or too low
- Eliminate half of the search space based on the result
- Repeat until we find the target

### Time Complexity
- **O(log n)** - We eliminate half the search space in each iteration

### Space Complexity
- **O(1)** - Only using a few variables

---

## Code Walkthrough with Example

**Example:** `n = 10, pick = 6`

### Initial Setup:
```python
l = 1  # left pointer
r = 10  # right pointer
```

### Iteration 1:
```
l = 1, r = 10
mid = 1 + (10 - 1) // 2 = 5
guess(5) → returns 1 (5 is lower than 6)
Update: l = 5 + 1 = 6
```
**Visual:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 l          ^mid              r
Guess 5 → too low, move left pointer right
```

### Iteration 2:
```
l = 6, r = 10
mid = 6 + (10 - 6) // 2 = 8
guess(8) → returns -1 (8 is higher than 6)
Update: r = 8 - 1 = 7
```
**Visual:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
               l     ^mid       r
Guess 8 → too high, move right pointer left
```

### Iteration 3:
```
l = 6, r = 7
mid = 6 + (7 - 6) // 2 = 6
guess(6) → returns 0 (FOUND IT!)
Return 6 ✅
```
**Visual:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
               l,^mid r
Guess 6 → FOUND! Return 6
```

---

## Key Points

1. **Mid Calculation:** Use `mid = l + (r - l) // 2` to avoid integer overflow
2. **API Return Values:**
   - `-1`: Your guess is **too high** → move right pointer left (`r = mid - 1`)
   - `1`: Your guess is **too low** → move left pointer right (`l = mid + 1`)
   - `0`: **Found it!** → return mid
3. **Loop Condition:** Continue while `l <= r`
4. **Efficiency:** Finds answer in just 3 guesses instead of potentially 10!

---

## Related Problems

- First Bad Version (LeetCode #278)
- Search Insert Position (LeetCode #35)
- Find Peak Element (LeetCode #162)

---

**Practice Tip:** This is a fundamental binary search problem. Make sure you understand:
- How to calculate mid without overflow
- When to update left vs right pointer
- The loop termination condition
