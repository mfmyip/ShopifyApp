# Q1
import csv

arr = []

with open('q1Data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
    	arr.append(row)


###################################################################################################
# Q1 A:
# The reason we had a AOV of 3145.13 was because we did not take into account the order quantity,
# if we normalize it by dividing by the quantity, we will get the correct AOV value.
sum1 = 0
for i in range(1, len(arr)):
	sum1 += int(arr[i][3]) / int(arr[i][4])
aov = sum1 / (len(arr) - 1)

print("aov: ", aov) # AOV should be ~$387.74

###################################################################################################
# Q1 B:
# median OV, sort by order_amount / total_items, to get normalized median.
# That's because a pair of sneakers sell for ~$27k per pair, which will skew our average to the right
# The median does not get affected the same way
def getMedian(ls):
	mid = int(len(ls) / 2)
	if (len(ls) % 2): # if length is odd
		return ls[mid]
	else:
		return (ls[mid] + ls[mid-1]) / 2

def appendPPS(row):
	row.append(int(row[3])/int(row[4]))
	return row

arrPricePerShoe = list(map(appendPPS, arr[1:]))
sortByPPS = sorted(arrPricePerShoe, key = lambda row: row[7])
pps = list(map(lambda row: row[7], sortByPPS))

print("median: ", getMedian(pps)) # MOV should be ~$153.00

# This was to find the average price of a sneaker of the 100 shops.
# remove duplicate shop id
# we first sort by shop_id, then remove all duplicates
sortedByShopID = sorted(arr[1:], key = lambda row: int(row[1]))

dataNoDupedShop = []
for row in sortedByShopID:
	if (len(dataNoDupedShop) == 0 or row[1] != dataNoDupedShop[len(dataNoDupedShop)-1][1]):
		dataNoDupedShop.append(row)
dataNoDupedShop.sort(key = lambda row: int(row[7]))

sumAg = 0
for row in dataNoDupedShop:
		sumAg += row[7]
print("avg price per sneaker: ", sumAg / 100)

###################################################################################################
# Q2 C:
# AOV should be ~$387.74
# MOV should be ~$153.00

###################################################################################################
