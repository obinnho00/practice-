"""1. Best Time to Buy and Sell Stock (LeetCode 121) 
You are given a list prices where prices[i] is the price of a given stock on the ith day. You 
want to maximize your profit by choose a single day to by one stock and choosing a 
different day in the future to sell that stock. 
Your program should display which day to buy and which day to sell stock and your 
profit. 
 
Use the following lists of prices to test your program: 
• Prices =  [7, , 4, 3, 1] 
o Your program should be able to display buy the stock on day 2 and sell the 
stock on day 5, and the profit is 5 
• Prices = [7, 6, 4, 3, 1] 
o Your program should be able to display not buying the stock and the profit 
is 0 """
""" #print(buy)
 # print(sell)
 for sell in range(len(price)):
    while profit < len(price):
        if price[sell] > price[buy]:
            profit = price[sell] - price[buy]
            #print(price[sell])
            print(price[buy])
            return
        else:
            buy = sell
        sell += 1"""

class stock:
    def track_stock(self):
        price =   [7, 1, 5, 3, 6,4] 
        #print(price[0])
        profit = 0
        #buy = 0
        
        for i in range(len(price)):
            i = 0
            j = i+1
            for j in range(len(price)):
                if price[i] > price[j]:
                    loss = price[i] - price[j]
                    #price[i]= price[i]+ 1
                    
                    
                    print(" do not buy stock in day", price[i], "and sell on day", price[j], "the profit is = -$", loss)
                    return
                else:
                    
                    
                    price[i] = price[j]
                price[j] = price[i] + 1
                
                #print("buy stock in day", price[i], "and sell on day", price[j], "the profit is = $", gain)
                
            return
                       
           
           
val = stock()                   
val.track_stock()
            
            
        











































    
        
        
    