class Solution:
    def romanToInt(self, s: str) -> int:
        number_vals = { "I" : 1,
                        "V" : 5,
                        "X" : 10,
                        "L" : 50,
                        "C" : 100,
                        "D" : 500,
                        "M" : 1000}
        total = 0
        for i in range(len(s)):
            if i+1 < len(s) and number_vals[s[i]] < number_vals[s[i+1]]:
                total -= number_vals[s[i]]
            else:
                total += number_vals[s[i]]
        return total