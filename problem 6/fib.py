def fibonacci(n):
    a=0
    b=1
    if n < 0:
       ans = -1
    elif n == 0:
       ans = 0
    elif n ==1:
        ans = 1
    else:
       for i in range(n-1): 
            c = a + b
            a= b
            b = c
       ans = c  
    #write your code here
    return ans

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')