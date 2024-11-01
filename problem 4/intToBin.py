def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    while num1 > 0:
        output = num1 % 2
        binary_val= binary_val + f'{output:.0f}'
        num1 =num1 // 2
    
    return binary_val


def string_reverse(input_string): 
    reverse_input = ''
    length = len(int_to_reverse_binary(num1))
    spot = length - 1
    empty = [0]*length
   #write your for loop here
    for i in int_to_reverse_binary(num1):
        empty[spot] = i
        spot -= 1
    reverse_input = ''.join(empty)
    return reverse_input
if __name__ == '__main__':
    print('Enter your number: ')
    num1 = int(input())
    
    binary_string = str(int_to_reverse_binary(num1))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)