m = int(input('請輸入里程數'))
n = 0
if m % 300 != 0:
  n = int(m / 300) + 1
  print((n*5)+70)
else:
  n = int(m / 300)
  print((n*5)+70)