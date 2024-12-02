arr_2 = {"play", "game", "pass"}
arr_1 = ["play", "game", "life"]
arr_0 = []

set_1 = set()
set_2 = set()
for i in arr_1:
    set_1.add(i)
for i in arr_2:
    set_2.add(i)

solution = set_1 | set_2

for i in solution:
    arr_0.append(i)

print(arr_0)