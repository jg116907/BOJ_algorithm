# Longes Common String

s1 = "helloworld"
s2 = "yellomarin"

dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

## LCS DP 배열 생성
# dp[-1][-1]에 최장 길이가 저장된다. 
for i in range(1,len(s1)+1):
  for j in range(1,len(s2)+1):
    if s1[i-1]==s2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j],dp[i][j-1])

for d in dp:
  print(d)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2]
# [0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 4]
# [0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 4]
# [0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 4]
# [0, 0, 1, 2, 3, 4, 4, 4, 5, 5, 5]
# [0, 0, 1, 2, 3, 4, 4, 4, 5, 5, 5]
# [0, 0, 1, 2, 3, 4, 4, 4, 5, 5, 5]

## LCS 추출
lcs = ""
i = len(s1)
j = len(s2)
while i!=0 and j!=0:
  if s1[i-1]==s2[j-1]:
    lcs += s1[i-1]
    i-=1
    j-=1
  else:
    if dp[i-1][j]==max(dp[i-1][j],dp[i][j-1]):
      i-=1
    else:
      j-=1
print(lcs[::-1])
# ellor