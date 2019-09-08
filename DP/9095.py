T = int(input())
nlist = []
for i in range(T):
  nlist.append(int(input()))
print(nlist)
anslist = []
for n in nlist:
  if n==1:
    anslist.append(1)
    continue
  elif n==2:
    anslist.append(2)
    continue
  elif n==3:
    anslist.append(4)
    continue
  arr = [0 for _ in range(n+1)]
  arr[1] = 1
  arr[2] = 2
  arr[3] = 4
  for i in range(4,n+1):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    print(arr)
  anslist.append(arr[n])

# print(anslist)
for ans in anslist:
  print(ans)

    
  
