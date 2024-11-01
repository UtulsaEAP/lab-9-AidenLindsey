def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    while num1 > 0:
        output = num1 % 2

    return binary_val;


def string_reverse(input_string): 
    reverse_input = ''
    
   #write your for loop here
    

    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)