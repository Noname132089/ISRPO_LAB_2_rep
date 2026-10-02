# Geometric Library

Это директория, содержащая файлы с различными функциями по вычислению площади и периметра(далее параметры).

Каждый файл содержит 2 функции: area(площадь) и perimeter(периметр)


## `circle.py`

* **`area(r)`**
  Вычисляет площадь круга.
  * *Аргументы:*
    * `r` (float) — радиус
  * *Возвращает:* $S = \pi \cdot r^2$
  * *Пример:* `area(5)` $\rightarrow$ `78.5398...`

* **`perimeter(r)`**
  Вычисляет длину окружности.
  * *Аргументы:*
    * `r` (float) — радиус
  * *Возвращает:* $P = 2 \cdot \pi \cdot r$
  * *Пример:* `perimeter(3)` $\rightarrow$ `18.8495...`


## `rectangle.py`

* **`area(a, b)`**
  Вычисляет площадь прямоугольника.
  * *Аргументы:*
    * `a` (float) — первая сторона
    * `b` (float) — вторая сторона
  * *Возвращает:* $S = a \cdot b$
  * *Пример:* `area(3, 4)` $\rightarrow$ `12`

* **`perimeter(a, b)`**
  Вычисляет периметр прямоугольника.
  * *Аргументы:*
    * `a` (float) — первая сторона
    * `b` (float) — вторая сторона
  * *Возвращает:* $P = (a + b) \cdot 2$
  * *Пример:* `perimeter(3, 4)` $\rightarrow$ `14`


## `square.py`

* **`area(a)`**
  Вычисляет площадь квадрата.
  * *Аргументы:*
    * `a` (float) — длина стороны
  * *Возвращает:* $S = a^2$
  * *Пример:* `area(5)` $\rightarrow$ `25`

* **`perimeter(a)`**
  Вычисляет периметр квадрата.
  * *Аргументы:*
    * `a` (float) — длина стороны
  * *Возвращает:* $P = 4 \cdot a$
  * *Пример:* `perimeter(5)` $\rightarrow$ `20`


## `triangle.py`

* **`area(a, h)`**
  Вычисляет площадь треугольника по стороне и высоте.
  * *Аргументы:*
    * `a` (float) — сторона
    * `h` (float) — высота, опущенная на сторону `a`
  * *Возвращает:* $S = \frac{a \cdot h}{2}$
  * *Пример:* `area(4, 5)` $\rightarrow$ `10`

* **`perimeter(a, b, c)`**
  Вычисляет периметр треугольника по трём сторонам.
  * *Аргументы:*
    * `a` (float) — первая сторона
    * `b` (float) — вторая сторона
    * `c` (float) — третья сторона
  * *Возвращает:* $P = a + b + c$
  * *Пример:* `perimeter(1, 3, 5)` $\rightarrow$ `9`


## История версий

| Хеш       | Изменения                                              |
| --------- | ----------------                                       |
| `e529492` | Fixed hash table                                       |
| `6d023bf` | Added examples of calls                                |
| `f24cb20` | Added hash table                                       |
| `e15d5b8` | Added triangle description and replaced '*' на '\cdot' |
| `0b1e2c5` | Added rectangle and square description                 |
| `f054115` | Added general description and circle description       |
| `120d534` | Add files                                              |
| `8ba9aeb` | L-03: Circle and square added                          |