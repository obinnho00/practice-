"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 
#nums = [2,7,11,15]
def twosum():
    s ="abcabcbb"
    list = []
    count = 0
    cur = 0
    list.append(s[0])
    for i in range(len(s)):
        j = i +1
        for j in range(len(s)):
            if s[i] != s[j]:
                if s[i] and s[j] not in list:
                    list.append(s[j])
                    
                
        break
            
    print "list"
    print(len(list))   """
    
# leetcosw 4 hard

# median of of two sorted arrays
num1, num2 = [1,3],[2]
def median(v1,v2):
    val =[]
    val.append(v1+v2)
    for i in range(len(val)):
        j = i+1
        for j in range(len(val)):
            if val[i] > val[j]:
                val[j] = val[i]
            
            
    
    
    
median(num1,num2)

                    
            
                
                
            
        
                
                
            
            
    
    
    
