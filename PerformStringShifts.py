"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
    [0,1] means shift to left by 1. "abc" -> "bca"
    [1,2] means shift to right by 2. "bca" -> "cab"

Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
    [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
    [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
    [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
    [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

Constraints:

    1 <= s.length <= 100
    s only contains lower case English letters.
    1 <= shift.length <= 100
    shift[i].length == 2
    0 <= shift[i][0] <= 1
    0 <= shift[i][1] <= 100

Hide Hint #1
    Intuitively performing all shift operations is acceptable due to the constraints.
Hide Hint #2
    You may notice that left shift cancels the right shift, so count the total left shift times (may be negative if the final result is right shift), and perform it once.
"""


def rotate(s: str, d: int, reverse=False) -> str:
    if d == 0:
        return s

    if reverse:
        Lfirst = s[0: d]
        Lsecond = s[d:]
        return Lsecond+Lfirst
    else:
        length_s = len(s)
        Rfirst = s[0: length_s - d]
        Rsecond = s[length_s - d:]
        return Rsecond+Rfirst


class Solution:
    def stringShift(self, s: str, shift) -> str:
        right_shift = 0
        left_shift = 0
        for i in shift:
            if i[0] == 0:
                left_shift += i[1]
            else:
                right_shift += i[1]


        print(left_shift)
        print(right_shift)
        return rotate(
            s,
            abs(right_shift - left_shift) % len(s),
            left_shift > right_shift
        )


s = Solution()
print(s.stringShift("xqgwkiqpif" ,[[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]))

