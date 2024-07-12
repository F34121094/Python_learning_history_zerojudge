r = input()
key = 0
for i in r:
    if i == ".":
        r = float(r)
        key += 1
        break
if key == 0 : r = int(r)

R = (r * 9) / 5 + 32
print(f"{R:g}")