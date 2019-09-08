N = int(input())

lope = []
for i in range(0,N):
  lope.append(int(input()))
lope = sorted(lope)

w = []
for i in range(0,len(lope)):
  # print("lope : ",lope[i])
  # print("N-i : ",N-i)
  w.append(lope[i] * (N - i))

print(max(w))