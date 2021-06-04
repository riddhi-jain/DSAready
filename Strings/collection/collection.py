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
