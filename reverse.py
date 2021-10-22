class Solution:
    def reverse(self, x: int) -> int:
        #reverses the number into the variable string as a string
        string = str(x)[::-1]
        #if the last element in the string is a negative number
        if(string[len(string)-1] == '-'):
            #put the negative at the front
            string = "-"+string[:-1]
        try:
            #if the string is out of range x is assigned to zero
            x = int(string)
            if(x < -(2**31) or x > (2**31)-1):
                x = 0
        except:
            #if x is already 0, leave it as x = 0
            x = 0
        finally:
            return x
