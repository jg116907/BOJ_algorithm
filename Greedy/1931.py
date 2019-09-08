# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14


# print(time)
n = int(input())
time=[]
for i in range(0,n):
  time.append(tuple(map(int,input().split())))
times = 0

time = sorted(time,key=lambda x: x[0])
time = sorted(time,key=lambda x: x[1])
print(time)
end_time = time[0][0]
for j in time:
  if j[0] >= end_time:
    times += 1
    end_time = j[1]


print(times)
