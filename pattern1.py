def pattern1(n, pattern_cycle=('*', '#','@','%')):
  pc_l = len(pattern_cycle)
  pattern = []
  for i in range(n):
    pattern.append(pattern_cycle[i % pc_l])
    print(*pattern)

pattern1(10)    

# ========== Output
# *
# * #
# * # @
# * # @ %
# * # @ % *
# * # @ % * #
# * # @ % * # @
# * # @ % * # @ %
# * # @ % * # @ % *
# * # @ % * # @ % * #
