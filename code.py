times = []
for i in range(5):
  time = float(input())
  times.append(time)

times.remove(min(times))
times.remove(max(times))
print(sum(times)/3)
