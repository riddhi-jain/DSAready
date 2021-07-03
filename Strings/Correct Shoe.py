from collections import Counter


num_shoes = int(input("Number of shoes: "))
size_shoes = Counter(input("All sizes of shoes (separated by space): ").split())
cust = int(input("Enter the number of customers: "))

size_price = []
price = []

for i in range(cust):
    size_price.append(input("Enter the size and price (separated by space): ").split())

for size in size_price:
    if size[0] in size_shoes.keys():
        price.append(size[1])
        if size_shoes[size[0]] == 1:
            size_shoes.pop(size[0])
        else:
            size_shoes[size[0]] = int(size_shoes[size[0]]) - 1

price = list(map(int, price))
print(sum(price))

'''
Input Format
The first line contains, the number of shoes. 
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains, the number of customers. 
The next lines contain the space separated values of the desired by the customer and , the price of the shoe.

Output Format
Print the amount of money earned by owner.

Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output
200

Explanation
Customer 1: Purchased size 6 shoe for $55. 
Customer 2: Purchased size 6 shoe for $45. 
Customer 3: Size 6 no longer available, so no purchase. 
Customer 4: Purchased size 4 shoe for $40. 
Customer 5: Purchased size 18 shoe for $60. 
Customer 6: Size 10 not available, so no purchase.

Total money earned = 55 + 45 + 40 + 60 = 200
'''
