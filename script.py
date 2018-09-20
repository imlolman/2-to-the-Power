from datetime import datetime
arr = [2]
mul = 2
power = 20000000
carry=0

for y in range(1,power):
    newarr = []
    for x in arr[::-1]:
        val = (x*mul)+carry
        newarr.append(val%10)
        carry = val//10
    if(carry != 0):
        newarr.append(carry)
    newarr.reverse()
    arr = newarr.copy()
    	
    if(y%10000 == 0):
        print(str(arr) + "\n\n Status: 2^" + str(y) + " => " + str(len(arr)) + "digits DATETIME: " + str(datetime.now()))
        f = open("log.txt","a+")
        f.write(str(arr) + "\n\n Status: 2^" + str(y) + " => " + str(len(arr)) + "digits DATETIME: " + str(datetime.now()) + " \n\n")
        f.close()
		
	