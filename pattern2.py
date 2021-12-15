def pattern2(n):
  pattern = ['*'] * n
  for i in range(n):
    print(*pattern)
    pattern.pop()

pattern2(5)    

# ========== Output
# * * * * *
# * * * *
# * * *
# * *
# *
