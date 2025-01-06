last_val = 2880
step = last_val / 10

for i in range(1, 10):
    next_val = last_val - (i * step)
    print(next_val)