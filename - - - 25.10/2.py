# В группе из 25 человек, произвольный человек узнаёт слух.
# Он передаёт его следуюшему чел. Новый человек может передать слух 23 людям.
# При передаче слуха уже знающему человеку распространение слуха прекращается.
# Найти мат. ожидание количества узнавших людей.
import random
count =int(input("введите количество моделируемых ситуаций:"))
returns = [0 for i in range(25)]
for i in range(count):
    knowers = [random.randint(0, 24)]
    while len(knowers) < 25:
        new = random.randint(0, 24)
        if new in knowers[-2:]:
            continue
        elif new in knowers[:-2]:
            break
        else:
            knowers.append(new)
    returns[len(knowers)] = returns[len(knowers)] + 1
answer = 0
for i in range(25):
    answer += i * returns[i]/count
print(answer)
print(sum(returns))
