def getSum(n): 
  
    sum = 0 
  
    # Single line that calculates sum  
    while(n > 0): 
        sum += int(n%10) 
        n = int(n/10) 
  
    return sum
