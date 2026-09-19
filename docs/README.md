# Общее описание

Это директория, содержащая файлы с различными функциями по вычислению площади и периметра(далее параметры).
Каждый файл содержит 2 функции: area(площадь) и perimeter(периметр)


# circle.py

Содержит функции для вычисления параметров круга:
- **Площадь**: $S = \pi \cdot r^2 $ Например, при area(5) вернет 25
- **Периметр**: $P = 2 \cdot \pi \cdot r $ Например, area(3) вернет 28.274...

# rectangle.py

Содержит функции для вычисления параметров прямоугольника
- **Площадь**: $S = a \cdot b$ Например, при area(3, 4) вернет 12
- **Периметр**: $P = (a + b) \cdot 2$ Например, при perimeter(3, 4) вернет 14

# square.py

Содержит функции для вычисления параметров квадрата
- **Площадь**: $S = a \cdot a$ Например, при area(5) вернет 25
- **Периметр**: $P = 4 \cdot a$ Например, при perimeter(5) вернет 20

# triangle.py

Содержит функции для вычисления параметров треугольника
- **Площадь**: $S = \frac{a \cdot h}{2}$ Например, при area(3, 4) вернет 6
- **Периметр**: $P = a \cdot b \cdot c$ Например, при perimeter(1, 3, 5) вернет 9


| Hash    | Commit                                                 |
| ------- | ------------------------------------------------------ |
| e529492 | (HEAD -> docs_558202) Fixed hash table                 |
| 6d023bf | (HEAD -> docs_558202) Added examples of calls          |
| f24cb20 | Added hash table                                       |
| e15d5b8 | Added triangle description and replaced '*' на '\cdot' |
| 0b1e2c5 | Aded rectangle and square description                  |
| f054115 | Added general description and circle description       |
| 120d534 | Add files                                              |
| 8ba9aeb | L-03: Circle and square added                          |