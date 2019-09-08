nk = list(map(int,input().split()))
coin = [int(input()) for _ in range(nk[0])]
coin_sorted = sorted(coin,reverse = True)
count = 0
target=nk[1]
for c in coin_sorted:
  if target == 0:
    break
  if c <= target:
    count += target // c
    target = target % c
print(count)