with open('8.txt', 'r', encoding="utf-8") as file:
    N, K, M = map(int, file.readline().split())
    print()
    boxes = []
    for _ in range(N):
        size, cost = map(int, file.readline().split())
        boxes.append((size, cost))
boxes.sort(reverse=True, key=lambda x: x[0])
max_count = 0
min_cost = 1000000000000000000
for i in range(N):
    current_size, current_cost = boxes[i]
    if current_cost > M:
        continue
    count = 1
    total_cost = current_cost
    last_size = current_size
    for j in range(i + 1, N):
        next_size, next_cost = boxes[j]
        if last_size - next_size >= K and total_cost + next_cost <= M:
            count += 1
            total_cost += next_cost
            last_size = next_size
    if count > max_count or (count == max_count and total_cost < min_cost):
        max_count = count
        min_cost = total_cost
print(f"{max_count} — максимальное количество коробок, {min_cost} — его минимальная стоимость")