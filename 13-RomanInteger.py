class Solution:
    def romanToInt(s) -> int:
        # Initalize dictionary of values for each symbol.
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Replace each subtractive element in the string with its addition-exclusive equivalent.
        # Care is taken here to do low replacements first, since they can create additional higher subtractive elements, but not vice versa.
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # Iterate over the string, adding each element's value to the total.
        for char in s:
            total += values[char]
        return total