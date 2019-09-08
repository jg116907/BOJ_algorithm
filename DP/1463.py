# 시간 초과로 오답
n = int(input())
dp = n
count = 0
def findone(dp,count):
  print(dp,count)
  if dp == 1:
    return count
  if dp % 3 == 0 and dp % 2 == 0: 
    return min(findone(dp//3,count+1),findone(dp//2,count+1),findone(dp-1,count+1))
  elif dp % 3 == 0:
    return min(findone(dp//3,count+1),findone(dp-1,count+1))
  elif dp % 2 == 0:
    return min(findone(dp//2,count+1),findone(dp-1,count+1))
  else:
    return findone(dp-1,count+1)

res = findone(n,0)
print(res)
