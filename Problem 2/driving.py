def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   #write your code here
   return(dollars_per_gallon / miles_per_gallon * miles_driven)

if __name__ == '__main__':
    print('Enter your cars gas millage: ')
    miles_per_gallon = float(input())
    print('Enter the cost of gas: ')
    dollars_per_gallon = float(input())
    #print your costs here like example below
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400.0):.2f}')
   