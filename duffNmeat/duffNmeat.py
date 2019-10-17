
MAX_DAYS = 100000
MAX_PRICE = 100

n_days = int(input())
best_price = MAX_DAYS * MAX_PRICE
min_cost = 0

for i in range(n_days):
    a, p  = list(map(lambda x: int(x), input().split()))
    best_price = min(best_price, p)
    min_cost += best_price * a

print(min_cost)
