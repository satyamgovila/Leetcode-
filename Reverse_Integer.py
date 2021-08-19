# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside 
# the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))
        y = y.strip()
        y = y[::-1]
        output = int(y)
        if output >= 2** 31 -1 or output <= -2** 31:
           return 0
        elif x < 0:
          return -1 * output
        else:
          return output
