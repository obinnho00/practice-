"""leetcode"""
class solution:
    #list = [1,0,11,15,9]
    
    def two_sum(self):
        list = [2,7,11,15]
        target = 9
        for i in range(len(list)):
            j = i+1
            for j in range(len(list)):
                if list[i] + list[j] == target:
                    
                    print("[",i,',', j,"]")
                
            else:
                list[i] += 1
                list[j] += 1
                

    def longest_substring(self):
        s = "abcabcbb"
        item = {}
        for i,letter in enumerate(s):
            print(letter)
        
                   
               
        
                
                        
                        
            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
val = solution()
val.longest_substring()
