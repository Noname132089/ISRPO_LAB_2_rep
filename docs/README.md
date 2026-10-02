# Geometric Library Reference

Это директория, содержащая файлы с различными функциями по вычислению площади и периметра(далее параметры).

Каждый файл содержит 2 функции: area(площадь) и perimeter(периметр)


## `circle.py`

* **`area(r)`**
  Вычисляет площадь круга.
  * *Аргументы:* `r` (число) — радиус
  * *Возвращает:* $S = \pi \cdot r^2$
  * *Пример:* `area(5)` $\rightarrow$ `78.5398...`

* **`perimeter(r)`**
  Находит длину окружности.
  * *Аргументы:* `r` (число) — радиус
  * *Возвращает:* $P = 2 \cdot \pi \cdot r$
  * *Пример:* `perimeter(3)` $\rightarrow$ `18.8495...`


## `rectangle.py`

* **`area(a, b)`**
  Находит площадь прямоугольника.
  * *Аргументы:* `a`, `b` (числа) — стороны
  * *Возвращает:* $S = a \cdot b$
  * *Пример:* `area(3, 4)` $\rightarrow$ `12`

* **`perimeter(a, b)`**
  Рассчитывает периметр прямоугольника.
  * *Аргументы:* `a`, `b` (числа) — стороны
  * *Возвращает:* $P = (a + b) \cdot 2$
  * *Пример:* `perimeter(3, 4)` $\rightarrow$ `14`


## `square.py`

* **`area(a)`**
  Вычисляет площадь квадрата.
  * *Аргументы:* `a` (число) — длина стороны
  * *Возвращает:* $S = a^2$
  * *Пример:* `area(5)` $\rightarrow$ `25`

* **`perimeter(a)`**
  Рассчитывает периметр квадрата.
  * *Аргументы:* `a` (число) — длина стороны
  * *Возвращает:* $P = 4 \cdot a$
  * *Пример:* `perimeter(5)` $\rightarrow$ `20`


## `triangle.py`

* **`area(a, h)`**
  Находит площадь треугольника по стороне и высоте.
  * *Аргументы:* `a` (сторона), `h` (высота к ней)
  * *Возвращает:* $S = \frac{a \cdot h}{2}$
  * *Пример:* `area(4, 5)` $\rightarrow$ `10`

* **`perimeter(a, b, c)`**
  Вычисляет периметр треугольника по трём сторонам.
  * *Аргументы:* `a`, `b`, `c` (числа) — длины сторон
  * *Возвращает:* $P = a + b + c$
  * *Пример:* `perimeter(1, 3, 5)` $\rightarrow$ `9`


## Changelog / История версий

| Хеш | Изменения |
| :-: | :-- |
| `e529492` | Fixed hash table |
| `6d023bf` | Added examples of calls |
| `f24cb20` | Added hash table |
| `e15d5b8` | Added triangle description and replaced '*' на '\cdot' |
| `0b1e2c5` | Added rectangle and square description |
| `f054115` | Added general description and circle description |
| `120d534` | Add files |
| `8ba9aeb` | L-03: Circle and square added |