"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

"""

import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        #First Create a map of all given values
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        
        arr = list(s)
        
        l = len(arr)
        sum = 0
        
        #Then in O(n) calculate the total
        for x in range(0,l):
            #If the roman number follows a higher roman number subtract it
            if x+1 < l and d[arr[x]] < d[arr[x+1]]:
                sum = sum - d[arr[x]]
            #Else just add it
            else:
                sum = sum + d[arr[x]]
        
        return sum


class TestStringMethods(unittest.TestCase):
    def tests(self):
        new = Solution()
        # Pass your Test values in brackets of fib function
        self.assertEqual(new.romanToInt("III"), 3, msg="Success")
        self.assertEqual(new.romanToInt("IV"), 4, msg="Success")

        




if __name__ == '__main__':
    unittest.main()