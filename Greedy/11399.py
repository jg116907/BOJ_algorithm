class Solution:
  def solution(self,num,time):
    time_sort=sorted(time)
    temp = 0
    sum_list=[]
    for i in range(0,len(time)):
      temp += time_sort[i]
      sum_list.append(temp)
    return sum(sum_list)
num = int(input())
time = list(map(int,input().split()))
s = Solution()
print(s.solution(num,time))
