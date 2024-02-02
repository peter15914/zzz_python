#for a in range(-2021,2021):
    #for b in range(-2021,2021):
        #if (a + 1) * (b - 1) * (a + b) == 2020:
            #print(a, b)
            
            
x = 2020

y = 2
while x > 1:
    if x % y == 0:
        print(y)
        x /= y
    else:
        y += 1
        
