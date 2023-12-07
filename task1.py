def result(N):
     
    # iterate from 0 to N
    for num in range(N):
         
            # Short-circuit operator is used
            if num % 3 == 0 and num % 6 ==0 and num % 9 == 0:
                print(str(num) + " ", end = "")
                 
            else:
                pass
 
# Driver code
if __name__ == "__main__":
     
    # input goes here
    N = 300
     
    # Calling function
    result(N)