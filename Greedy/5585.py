coin = int(input())

change = 1000 - coin
coin_list = [500,100,50,10,5,1]
coin_count = []
for i in coin_list:
  coin_count.append(int(change/i))
  change = change%i

print(sum(coin_count))