def feet_to_steps(user_feet):
   #write your code here
   steps = user_feet / 2.5
   return(int(steps))

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    print('Enter the number of feet you walked')
    user_feet = float(input())
    #print your steps here
    print(feet_to_steps(user_feet))
    feet_to_steps(5280)