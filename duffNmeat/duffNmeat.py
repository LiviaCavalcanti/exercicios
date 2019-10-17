n_days = int(input())
meat_amount = []
meat_price = []
total_meat = 0


for i in range(n_days):
    tuple_input = input().split(' ')
    meat_amount.append(int(tuple_input[0]))
    total_meat += int(tuple_input[0])
    meat_price.append(int(tuple_input[1]))

best_value = total_meat * meat_price[0]
total_meat -= meat_amount[0]
partial_sum = meat_amount[0] * meat_price[0]

for i in range(1, n_days):
    partial_sum += meat_amount[i] * meat_price[i]
    total_meat -= meat_amount[i]
    temp = partial_sum + meat_price[i] * total_meat
    if temp < best_value:
        best_value = temp

print(best_value)