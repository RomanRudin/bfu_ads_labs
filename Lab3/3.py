from math import log
x = int(input("Please, enter the x: "))

ans = []
max_pow = int(log(x, 3) + 1) + 1

for k in range(max_pow):
    for l in range(max_pow-k):
        for m in range(max_pow-k-l):
            number = 3**k * 5**l * 7**m
            if (number <= x) and not (number in ans):
                ans.append([number, k, l, m])

print("The answer:\n" + "\n".join(f"{number}\t{k} {l} {m}" for number, k, l, m in sorted(ans, key=lambda x: x[0])))