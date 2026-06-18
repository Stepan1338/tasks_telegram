# Введение ООП на примере Python
# Задача 1
"""class LittleBell:
    def sound(self):
        print('ding')
        pass

bell = LittleBell()
bell.sound()"""

# Задача 2
"""
class Button:
    def __init__(self):
        self.click_count = 0

    def click(self):
        self.click_count += 1

    def click_count(self):
        return self.click_count

    def reset(self):
        self.click_count = 0

button = Button()
button.click()
button.click()
print(button.click_count)
button.click()
print(button.click_count)
"""

# Задача 3
"""
class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_left(self, weight: int):
        self.left_weight += weight

    def add_right(self, weight: int):
        self.right_weight += weight

    def result(self) -> str:
        if self.left_weight > self.right_weight:
            return 'L'
        elif self.right_weight > self.left_weight:
            return 'R'
        else:
            return '='

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())
"""

# Задача 4
"""
class OddEvenSeparator:
    def __init__(self):
        self.even_numbers = []
        self.odd_numbers = []

    def add_number(self, number: int):
        if number % 2 == 0:
            self.even_numbers.append(number)
        else:
            self.odd_numbers.append(number)

    def even(self) -> list:
        return self.even_numbers

    def odd(self) -> list:
        return self.odd_numbers

separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))
"""

# Задача 5
"""
class BigBell:
    def __init__(self):
        self.is_ding = True

    def sound(self):
        if self.is_ding:
            print("ding")
        else:
            print("dong")
        self.is_ding = not self.is_ding

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
"""
# Задача 6
"""
class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence: str):
        self.words.extend(sentence.split())

    def shortest_words(self) -> list:
        if not self.words:
            return []
        min_len = min(len(word) for word in self.words)
        return sorted([word for word in self.words if len(word) == min_len])

    def longest_words(self) -> list:
        if not self.words:
            return []
        max_len = max(len(word) for word in self.words)
        return sorted(list(set(word for word in self.words if len(word) == max_len)))

finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('abc')
finder.add_sentence('world')
finder.add_sentence('def')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))
"""

# Задача 7
"""
class BoundingRectangle:
    def __init__(self):
        self.x_coords = []
        self.y_coords = []

    def add_point(self, x: int, y: int):
        self.x_coords.append(x)
        self.y_coords.append(y)

    def left_x(self) -> int:
        return min(self.x_coords)

    def right_x(self) -> int:
        return max(self.x_coords)

    def bottom_y(self) -> int:
        return min(self.y_coords)

    def top_y(self) -> int:
        return max(self.y_coords)

    def width(self) -> int:
        return self.right_x() - self.left_x()

    def height(self) -> int:
        return self.top_y() - self.bottom_y()


rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
"""

# Полиморфизм
# Задача 1
"""
class Selector:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def get_odds(self) -> list:
        return [x for x in self.numbers if x % 2 != 0]

    def get_evens(self) -> list:
        return [x for x in self.numbers if x % 2 == 0]

values = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
"""

# Задача 2
"""
class Paragraph:
    def __init__(self, width: int):
        self.width = width
        self.words = []

    def add_word(self, word: str):
        self.words.append(word)

    def _get_lines(self) -> list:
        lines = []
        if not self.words:
            return lines

        current_line = []
        current_length = 0

        for word in self.words:
            spaces_needed = len(current_line)
            if current_length + spaces_needed + len(word) <= self.width:
                current_line.append(word)
                current_length += len(word)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(" ".join(current_line))
        return lines


class LeftParagraph(Paragraph):
    def end(self):
        lines = self._get_lines()
        for line in lines:
            print(line)
        self.words = []


class RightParagraph(Paragraph):
    def end(self):
        lines = self._get_lines()
        for line in lines:
            print(line.rjust(self.width))
        self.words = []

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
"""
# Задача 3
"""
class BaseDate:
    def __init__(self, year: int, month: int, day: int):
        self._year = year
        self._month = month
        self._day = day

    def set_year(self, year: int):
        self._year = year

    def set_month(self, month: int):
        self._month = month

    def set_day(self, day: int):
        self._day = day

    def get_year(self) -> int:
        return self._year

    def get_month(self) -> int:
        return self._month

    def get_day(self) -> int:
        return self._day


class AmericanDate(BaseDate):
    def format(self) -> str:
        return f"{str(self._month).zfill(2)}.{str(self._day).zfill(2)}.{str(self._year).zfill(4)}"


class EuropeanDate(BaseDate):
    def format(self) -> str:
        return f"{str(self._day).zfill(2)}.{str(self._month).zfill(2)}.{str(self._year).zfill(4)}"

american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())
"""

# Задача 4
"""
class MinStat:
    def __init__(self):
        self.min_val = None

    def add_number(self, number: int):
        if self.min_val is None or number < self.min_val:
            self.min_val = number

    def result(self) -> int or None:
        return self.min_val


class MaxStat:
    def __init__(self):
        self.max_val = None

    def add_number(self, number: int):
        if self.max_val is None or number > self.max_val:
            self.max_val = number

    def result(self) -> int or None:
        return self.max_val


class AverageStat:
    def __init__(self):
        self.total_sum = 0
        self.count = 0

    def add_number(self, number: int):
        self.total_sum += number
        self.count += 1

    def result(self) -> float or None:
        if self.count == 0:
            return None
        return self.total_sum / self.count

values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
"""
# Задача 5
"""
class Table:
    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def get_value(self, row: int, col: int):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self.matrix[row][col]
        return None

    def set_value(self, row: int, col: int, value: int):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            self.matrix[row][col] = value

    def n_rows(self) -> int:
        return self._rows

    def n_cols(self) -> int:
        return self._cols

tab = Table(2, 2)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()
"""

# Задача 6
"""
class Rectangle:
    def __init__(self, x: float, y: float, w: float, h: float):
        self._x = x
        self._y = y
        self._w = w
        self._h = h

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def get_w(self) -> float:
        return self._w

    def get_h(self) -> float:
        return self._h

    def intersection(self, other: 'Rectangle') -> 'Rectangle' or None:
        left = max(self._x, other._x)
        right = min(self._x + self._w, other._x + other._w)

        bottom = max(self._y, other._y)
        top = min(self._y + self._h, other._y + other._h)

        intersect_w = right - left
        intersect_h = top - bottom

        if intersect_w <= 0 or intersect_h <= 0:
            return None

        return Rectangle(left, bottom, intersect_w, intersect_h)

rect1 = Rectangle(3, 5, 2, 1)
rect2 = Rectangle(1, 2, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
"""

# Задача 7
"""
class Table:
    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def get_value(self, row: int, col: int):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self.matrix[row][col]
        return None

    def set_value(self, row: int, col: int, value: int):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            self.matrix[row][col] = value

    def n_rows(self) -> int:
        return self._rows

    def n_cols(self) -> int:
        return self._cols

    def delete_row(self, row: int):
        if 0 <= row < self._rows:
            self.matrix.pop(row)
            self._rows -= 1

    def delete_col(self, col: int):
        if 0 <= col < self._cols:
            for r in range(self._rows):
                self.matrix[r].pop(col)
            self._cols -= 1

    def add_row(self, row: int):
        new_row = [0] * self._cols
        self.matrix.insert(row, new_row)
        self._rows += 1

    def add_col(self, col: int):
        for r in range(self._rows):
            self.matrix[r].insert(col, 0)
        self._cols += 1

tab = Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()
"""

# Задача 8
"""
class Person:
    def __init__(self, first_name: str, patronymic: str, last_name: str, phones: dict):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.phones = phones

    def get_phone(self) -> str or None:
        return self.phones.get('private')

    def get_name(self) -> str:
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def get_work_phone(self) -> str or None:
        return self.phones.get('work')

    def get_sms_text(self) -> str:
        return f"Уважаемый {self.first_name} {self.patronymic}! Примите участие в нашем беспроигрышном конкурсе для физических лиц."


class Company:
    def __init__(self, name: str, company_type: str, phones: dict, *employees: Person):
        self.name = name
        self.company_type = company_type
        self.phones = phones
        self.employees = list(employees)

    def get_phone(self) -> str or None:
        if 'contact' in self.phones:
            return self.phones['contact']

        for employee in self.employees:
            work_phone = employee.get_work_phone()
            if work_phone:
                return work_phone

        return None

    def get_name(self) -> str:
        return self.name

    def get_sms_text(self) -> str:
        return f"Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.company_type}."


def send_sms(*objects: Person or Company):
    for obj in objects:
        phone = obj.get_phone()
        if phone:
            print(f"Отправлено СМС на номер {phone} с текстом: {obj.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {obj.get_name()}")

person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
"""

# Определение операторов
# Задача 1
"""
class FoodInfo:
    def __init__(self, proteins: int, fats: int, carbohydrates: int):
        self._proteins = proteins
        self._fats = fats
        self._carbohydrates = carbohydrates

    def get_proteins(self) -> int:
        return self._proteins

    def get_fats(self) -> int:
        return self._fats

    def get_carbohydrates(self) -> int:
        return self._carbohydrates

    def get_kcalories(self) -> int:
        return 4 * self._proteins + 9 * self._fats + 4 * self._carbohydrates

    def __add__(self, other: 'FoodInfo') -> 'FoodInfo':
        return FoodInfo(
            self._proteins + other.get_proteins(),
            self._fats + other.get_fats(),
            self._carbohydrates + other.get_carbohydrates()
        )
    
food1 = FoodInfo(1, 2, 3)
food2 = FoodInfo(10, 20, 30)

food3 = food1 + food2
food4 = food2 + food1

print(food3.get_proteins(), food3.get_fats(),
      food3.get_carbohydrates(), food3.get_kcalories())
print(food4.get_proteins(), food4.get_fats(),
      food4.get_carbohydrates(), food4.get_kcalories())
"""
# Задача 2
"""
class ReversedList:
    def __init__(self, lst: list):
        self.lst = lst

    def __len__(self) -> int:
        return len(self.lst)

    def __getitem__(self, index: int):
        return self.lst[-1 - index]

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])
"""
# Задача 3
"""
class SquareFunction:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x: float) -> float:
        return self.a * (x ** 2) + self.b * x + self.c

sf = SquareFunction(1, 2, 1)
print(sf(-2))
print(sf(-1))
print(sf(-0))
print(sf(1))
print(sf(2))
print(sf(10))
"""
# Задача 4
"""
class Date:
    DAYS_IN_MONTHS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month: int, day: int):
        self.month = month
        self.day = day

    def _to_absolute_days(self) -> int:
        return sum(self.DAYS_IN_MONTHS[:self.month]) + self.day

    def __sub__(self, other: 'Date') -> int:
        return self._to_absolute_days() - other._to_absolute_days()

mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)
"""
# Задача 5
"""
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: 'Point') -> bool:
        return self.x != other.x or self.y != other.y


p1 = Point(0, 10)
p2 = Point(0, 0)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")
"""
# Задача 6
"""
class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, index: int, value: int):
        if value == 0:
            self.data.pop(index, None)
        else:
            self.data[index] = value

    def __getitem__(self, index: int) -> int:
        return self.data.get(index, 0)

def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))


arr = SparseArray()
index = 1000000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)
"""
# Задача 7
"""
class Polynomial:
    def __init__(self, coefficients: list):
        self.coefficients = list(coefficients)

    def __call__(self, x: float) -> float:
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        max_len = max(len(self.coefficients), len(other.coefficients))

        new_coeffs = []
        for i in range(max_len):
            c1 = self.coefficients[i] if i < len(self.coefficients) else 0
            c2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(c1 + c2)

        return Polynomial(new_coeffs)

# Ваш код

poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))
"""
# Задача 8
"""
class Queue:
    def __init__(self, *args):
        self.items = list(args)

    def append(self, *values):
        self.items.extend(values)

    def copy(self):
        new_q = Queue()
        new_q.items = list(self.items)
        return new_q

    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def extend(self, other: 'Queue'):
        self.items.extend(other.items)

    def next(self):
        new_q = Queue()
        if len(self.items) > 1:
            new_q.items = list(self.items[1:])
        return new_q

    def __add__(self, other: 'Queue') -> 'Queue':
        new_q = Queue()
        new_q.items = self.items + other.items
        return new_q

    def __iadd__(self, other: 'Queue') -> 'Queue':
        self.extend(other)
        return self

    def __eq__(self, other: 'Queue') -> bool:
        return self.items == other.items

    def __rshift__(self, n: int) -> 'Queue':
        new_q = Queue()
        if n < len(self.items):
            new_q.items = list(self.items[n:])
        return new_q

    def __str__(self) -> str:
        if not self.items:
            return "[]"
        return "[" + " -> ".join(map(str, self.items)) + "]"

    def __next__(self) -> 'Queue':
        return self.next()
# Ваш код

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
"""
# Наследование
# Задача 1
"""
class BaseObject:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self) -> list:
        return [self.x, self.y, self.z]


class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None


class Entity(BaseObject):
    def move(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Thing(BaseObject):
    # Класс наследует всё поведение BaseObject и не требует новых методов
    pass
"""
# Задача 2
"""
class Acellularia:
    pass


class Cellularia:
    pass


class Prokaryota(Cellularia):
    pass


class Eukaryota(Cellularia):
    pass


class Unicellularia(Eukaryota):
    pass


class Fungi(Eukaryota):
    pass


class Plantae(Eukaryota):
    pass


class Animalia(Eukaryota):
    pass
"""
# Задача 3
"""
class User:
    def solve(self, n: int):
        pass


class Student(User):
    pass


class Teacher(User):
    def check_solution(self, user: User, n: int):
        pass


class Admin(User):
    def edit(self, n: int):
        pass


class SuperAdmin(Admin):
    def grant(self, user: User):
        pass
"""
# Задача 4
"""
class User:
    def __init__(self, name: str):
        self.name = name

    def send_message(self, user: 'User', message: str):
        pass

    def post(self, message: str):
        pass

    def info(self) -> str:
        return ""

    def describe(self):
        additional_info = self.info()
        if additional_info:
            print(f"{self.name} ({additional_info})")
        else:
            print(self.name)


class Person(User):
    def __init__(self, name: str, birth_date: str):
        super().__init__(name)
        self.birth_date = birth_date

    def info(self) -> str:
        return f"Дата рождения: {self.birth_date}"

    def subscribe(self, user: User):
        pass


class Community(User):
    def __init__(self, name: str, description: str):
        super().__init__(name)
        self.description = description

    def info(self) -> str:
        return f"Описание: {self.description}"
"""
# Задача 5
"""
class Animal:
    def breathe(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass
"""
# Задача 6
"""
# Базовый класс для всего транспорта
class Transport:
    pass


#ВОДНЫЙ ТРАНСПОРТ
class WaterTransport(Transport):
    pass


#ВОЗДУШНЫЙ ТРАНСПОРТ
class AirTransport(Transport):
    pass

class Aviation(AirTransport):          # Авиация (тяжелее воздуха)
    pass

class Aeronautics(AirTransport):       # Воздухоплавание (легче воздуха)
    pass


#НАЗЕМНЫЙ ТРАНСПОРТ
class GroundTransport(Transport):
    pass

class RailwayTransport(GroundTransport):     # Железнодорожный
    pass

class AutomobileTransport(GroundTransport):  # Автомобильный
    pass

class BicycleTransport(GroundTransport):     # Велосипедный
    pass

class AnimalDrawnTransport(GroundTransport):  # Движимый животными
    pass

#КОСМИЧЕСКИЙ ТРАНСПОРТ
class SpaceTransport(Transport):
    pass
"""
# Задача 7
"""
# Базовый класс для всех фигур
class Shape:
    pass


# Многоугольник — это частный случай фигуры
class Polygon(Shape):
    pass


#Ветвь треугольников
# Треугольник — это многоугольник
class Triangle(Polygon):
    pass

# Равнобедренный треугольник — это частный случай треугольника
class IsoscelesTriangle(Triangle):
    pass

# Равносторонний треугольник — это частный случай равнобедренного треугольника
class EquilateralTriangle(IsoscelesTriangle):
    pass


#Ветвь четырехугольников
# Четырехугольник — это многоугольник
class Quadrilateral(Polygon):
    pass

# Параллелограмм — это четырехугольник с параллельными противоположными сторонами
class Parallelogram(Quadrilateral):
    pass

# Прямоугольник — это параллелограмм с прямыми углами
class Rectangle(Parallelogram):
    pass

#Квадрат — это прямоугольник с равными сторонами (или ромб с прямыми углами)
class Square(Rectangle):
    pass
"""
# Задача 8
"""
class Summator:
    def transform(self, n: int) -> int:)
        return n

    def sum(self, N: int) -> int:
        total_sum = 0
        for n in range(1, N + 1):
            total_sum += self.transform(n)
        return total_sum


class SquareSummator(Summator):
    def transform(self, n: int) -> int:
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n: int) -> int:
        return n ** 3
"""
# Задача 9
"""
class Profile:
    def __init__(self, profession: str):
        self.profession = profession

    def info(self) -> str:
        return ""

    def describe(self):
        additional_info = self.info()
        if additional_info:
            print(f"{self.profession} ({additional_info})")
        else:
            print(self.profession)


class Vacancy(Profile):
    def __init__(self, profession: str, salary: int or str):
        super().__init__(profession)
        self.salary = salary

    def info(self) -> str:
        return f"Предлагаемая зарплата: {self.salary}"


class Resume(Profile):
    def __init__(self, profession: str, experience: int or str):
        super().__init__(profession)
        self.experience = experience

    def info(self) -> str:
        return f"Стаж работы: {self.experience}"
"""
# Задача 10
"""
class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side: float):
        super().__init__(side, side, side)
"""
# Задача 11
"""
class Summator:
    def transform(self, n: int) -> int or float:
        return n

    def sum(self, N: int) -> int or float:
        total_sum = 0
        for n in range(1, N + 1):
            total_sum += self.transform(n)
        return total_sum


class PowerSummator(Summator):
    def __init__(self, b: float):
        self.b = b

    def transform(self, n: int) -> float:
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)
"""
# Задача 12
"""
class A:
    def __str__(self) -> str:
        return "A.__str__ method"

    def hello(self):
        print("Hello")


class B:
    def __str__(self) -> str:
        return "B.__str__ method"

    def good_evening(self):
        print("Good evening")


class C(A, B):
    # Наследует __str__ от A, так как A указан первым
    pass


class D(B, A):
    # Наследует __str__ от B, так как B указан первым
    pass


def new_method(arg):
    return  "new method"

def new_method2(arg):
    return "new method 2"


A.__str__ = new_method
B.__str__ = new_method2
c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(isinstance(c, A), isinstance(c, B))
print(isinstance(d, A), isinstance(d, B))
print(c)
print(d)
"""
# Задача 13
"""
import math

class Weapon:
    def __init__(self, name: str, damage: int, range_val: int):
        self.name = name
        self.damage = damage
        self.range = range_val

    def hit(self, actor, target):
        # 1. Проверяем, жив ли противник
        if not target.is_alive():
            print("Враг уже повержен")
            return

        # 2. Вычисляем расстояние между actor и target по формуле гипотенузы
        ax, ay = actor.get_coords()
        tx, ty = target.get_coords()
        distance = math.hypot(tx - ax, ty - ay)

        # 3. Проверяем радиус действия оружия
        if distance > self.range:
            print(f"Враг слишком далеко для оружия {self.name}")
        else:
            print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
            target.get_damage(self.damage)

    def __str__(self) -> str:
        return self.name


class BaseCharacter:
    def __init__(self, pos_x: int, pos_y: int, hp: int):
        self.x = pos_x
        self.y = pos_y
        self.hp = hp

    def move(self, delta_x: int, delta_y: int):
        self.x += delta_x
        self.y += delta_y

    def is_alive(self) -> bool:
        return self.hp > 0

    def get_damage(self, amount: int):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def get_coords(self) -> tuple:
        return (self.x, self.y)


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x: int, pos_y: int, weapon: Weapon, hp: int):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        # Проверяем, является ли цель Главным героем
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self) -> str:
        return f"Враг на позиции {self.get_coords()} с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x: int, pos_y: int, name: str, hp: int):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.inventory = []  # Список оружия
        self.current_weapon_idx = -1  # Индекс текущего оружия экипировки

    def hit(self, target):
        # Если цель является BaseEnemy, её можно атаковать
        if not isinstance(target, BaseEnemy):
            print("Могу ударить только врага")
            return

        # Проверяем, есть ли оружие
        if self.current_weapon_idx == -1:
            print("Я безоружен")
        else:
            weapon = self.inventory[self.current_weapon_idx]
            weapon.hit(self, target)

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            print(f"Подобрал {weapon.name}")
            self.inventory.append(weapon)
            # Если это первое оружие в инвентаре, автоматически экипируем его
            if len(self.inventory) == 1:
                self.current_weapon_idx = 0
        else:
            print("Это не оружие")

    def next_weapon(self):
        if not self.inventory:
            print("Я безоружен")
        elif len(self.inventory) == 1:
            print("У меня только одно оружие")
        else:
            # Переключение по кругу
            self.current_weapon_idx = (self.current_weapon_idx + 1) % len(self.inventory)
            new_weapon = self.inventory[self.current_weapon_idx]
            print(f"Сменил оружие на {new_weapon.name}")

    def heal(self, amount: int):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Полечился, теперь здоровья {self.hp}")

# Ваш код

weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)
"""
#Переопределение функций и декораторы
#Задача 1
"""
import builtins

original_print = builtins.print

def print(*args):
    upper_args = [str(arg).upper() for arg in args]
    original_print(*upper_args)
"""
#Задача 2
"""
import functools

def check_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")

        if password == "password":
            return func(*args, **kwargs)
        else:
            print("В доступе отказано")
            return None

    return wrapper


@check_password
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
"""
#Задача 3
"""
import functools


def check_password(correct_password: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_password = input()

            if user_password == correct_password:
                return func(*args, **kwargs)
            else:
                print("В доступе отказано")
                return None

        return wrapper

    return decorator
"""
#Задача 4
"""
import functools


def cached(func):
    # Словарь для хранения результатов вычислений
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # В качестве ключа используем кортеж из позиционных аргументов
        # (для базовой функции fib(n) этого достаточно)
        key = args

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper
"""

