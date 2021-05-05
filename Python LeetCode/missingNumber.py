class Solution(object):
    def missingNumber(self, nums):
        
        counter = 0
        s = 0
        for y in nums:
            counter = counter+1
        counter = counter+1
        for z in range(counter):
            s=s+z
            print ("add")
            print (z)

        for x in nums:
            print("s ") 
            print (s)
            print("x ") 
            print (x)
            s=abs(s-x)
        return s