"""
#Задача 1
class User():
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password

    def check_password(self, password: str):
        if password == self.__password:
            return True
        else:
            return False

    def set_password(self, old_password: str, new_password: str):
        if self.check_password(old_password):
            self.__password = new_password
            return True
        else:
            return False


u = User("alice", "1234")
print(u.username)
print(u.check_password("0000"))
print(u.check_password("1234"))

print(u.set_password("0000", "abcd"))
print(u.set_password("1234", "abcd"))
print(u.check_password("abcd"))
"""
"""
#Задача 2
class Counter():
    def __init__(self, start: int = 0):
        self._value = start

    def inc(self):
        self._value += 1

    def dec(self):
        self._value -= 1

    def value(self) -> int:
        return self._value

class LimitedCounter(Counter):
    def __init__(self, min_value: int, max_value: int):
        Counter.__init__(self, start=min_value)
        self.min_value = min_value
        self.max_value = max_value

    def inc(self):
        if self._value < self.max_value:
            Counter.inc(self)

    def dec(self):
        if self._value > self.min_value:
            # Прямой вызов родительского метода dec
            Counter.dec(self)




c = LimitedCounter(min_value=0, max_value=2)

print(c.value())
c.dec()
print(c.value())

c.inc(); c.inc(); c.inc()
print(c.value())
"""

"""
#Задача 3
class BankAccount():
    def __init__(self, initial: int):
        self.__balance = initial

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: int) -> bool:
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

acc = BankAccount(100)

print(acc.balance)
acc.deposit(50)
print(acc.balance)

print(acc.withdraw(30))
print(acc.balance)

print(acc.withdraw(1000))
print(acc.balance)
"""

"""
#Задача 4
class Report():
    def render(self, data: list) -> str:
        return self._format_header() + self._format_body(data) + self._format_footer()

    def _format_header(self) -> str:
        return "Report Header\n"

    def _format_body(self, data: list) -> str:
        return f"Data: {data}\n"

    def _format_footer(self) -> str:
        return "Report Footer"


class HtmlReport(Report):
    def _format_header(self) -> str:
        return "<html><h1>Report</h1>"

    def _format_body(self, data: list) -> str:
        items = "".join(f"<li>{item}</li>" for item in data)
        return f"<ul>{items}</ul>"

    def _format_footer(self) -> str:
        return "<p>End</p></html>"


r = HtmlReport()
print(r.render(["A", "B"]))
"""

"""
#Задача 5
class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self._content = content
        self.__audit_log = []

    def read(self) -> str:
        return self._content

    def history(self) -> tuple[str, ...]:
        return tuple(self.__audit_log)

    def _log(self, event: str) -> None:
        self.__audit_log.append(event)


class EditorDocument(Document):
    def edit(self, new_content: str) -> None:
        log_message = f"edit: {self._content} -> {new_content}"
        self._log(log_message)

        self._content = new_content


class AdminDocument(EditorDocument):
    def purge_history(self) -> None:
        self._Document__audit_log.clear()

doc = AdminDocument("Spec", "v1")

print(doc.read())
doc.edit("v2")
doc.edit("v3")

print(doc.history())

doc.purge_history()
print(doc.history())
"""

"""
#Задача 1
class Temperature:
    @staticmethod
    def c_to_f(c: float) -> float:
        res = (c * 9 / 5) + 32
        return round(res, 2)

    @staticmethod
    def f_to_c(f: float) -> float:
        res = (f - 32) * 5 / 9
        return round(res, 2)

print(Temperature.c_to_f(0))
print(Temperature.f_to_c(212))
print(Temperature.c_to_f(-40))
print(Temperature.f_to_c(-40))
"""

"""
#Задача 2
class Password:
    @staticmethod
    def is_strong(p: str) -> bool:
        has_len = len(p) >= 8
        has_digit = any(char.isdigit() for char in p)
        has_upper = any(char.isupper() for char in p)
        has_lower = any(char.islower() for char in p)
        return has_len and has_digit and has_upper and has_lower

print(Password.is_strong('qwerty'))
print(Password.is_strong('Qwerty12'))
print(Password.is_strong('QWERTY12'))
print(Password.is_strong('Qwerty123'))
"""

"""
#Задача 3
class User:
    _counter = 0

    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name

    @classmethod
    def create(cls, name: str) -> "User":
        cls._counter += 1
        return cls(user_id=cls._counter, name=name)

    @classmethod
    def count(cls) -> int:
        return cls._counter

u1 = User.create("Ann")
u2 = User.create("Bob")
u3 = User.create("Cory")

print(u1.id, u2.id, u3.id)
print(User.count())
"""

"""
#Задача 4
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def from_string(cls, s: str) -> "Point":
        x_str, y_str = s.split(",")
        return cls(float(x_str.strip()), float(y_str.strip()))

    @classmethod
    def from_dict(cls, d: dict) -> "Point":
        return cls(float(d["x"]), float(d["y"]))

    @staticmethod
    def distance(a: "Point", b: "Point") -> float:
        res = math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
        return round(res, 2)

p1 = Point.from_string("3, 4")
p2 = Point.from_dict({"x": 0, "y": 0})

print(p1.x, p1.y)
print(Point.distance(p1, p2))
"""

"""
#Задача 5
class Shape:
    _registry = []

    def __init__(self):
        name = self.__class__.__name__
        if name not in Shape._registry:
            Shape._registry.append(name)

    @classmethod
    def available(cls) -> list[str]:
        return sorted(Shape._registry)

class Circle(Shape):
    def __init__(self):
        super().__init__()


class Square(Shape):
    def __init__(self):
        super().__init__()


class Triangle(Shape):
    def __init__(self):
        super().__init__()

c = Circle()
s = Square()
t = Triangle()

print(Shape.available())
"""

"""
#Single Responsibility
import json
from dataclasses import dataclass

@dataclass
class Order:
    id: str
    price: float
    qty: int
    customer_email: str


class JsonOrderLoader:
    def load(self, json_path: str) -> list[dict]:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)


class OrderValidator:
    def parse_orders(self, raw_data: list[dict]) -> list[Order]:
        orders = []
        for item in raw_data:
            if "id" not in item or "price" not in item or "qty" not in item or "email" not in item:
                raise ValueError("Invalid order payload")
            if item["qty"] <= 0:
                raise ValueError("qty must be positive")

            orders.append(
                Order(
                    id=item["id"],
                    price=float(item["price"]),
                    qty=int(item["qty"]),
                    customer_email=item["email"]
                )
            )
        return orders

class OrderCalculator:
    def calculate_total(self, orders: list[Order]) -> float:
        return sum(o.price * o.qty for o in orders)


class TextReportFormatter:
    def format(self, orders: list[Order], total: float) -> str:
        return f"Orders count: {len(orders)}\nTotal: {total:.2f}\n"

class EmailNotificationService:
    def send_report_to_customers(self, orders: list[Order], report_body: str) -> None:
        for o in orders:
            print(f"[EMAIL to={o.customer_email}] Your order report\n{report_body}")


class OrderReportFacade:
    def __init__(
            self,
            loader: JsonOrderLoader,
            validator: OrderValidator,
            calculator: OrderCalculator,
            formatter: TextReportFormatter,
            notifier: EmailNotificationService
    ):
        self.loader = loader
        self.validator = validator
        self.calculator = calculator
        self.formatter = formatter
        self.notifier = notifier

    def run(self, json_path: str) -> str:
        raw_data = self.loader.load(json_path)
        orders = self.validator.parse_orders(raw_data)
        total = self.calculator.calculate_total(orders)
        report = self.formatter.format(orders, total)
        
        self.notifier.send_report_to_customers(orders, report)

        return report
"""

"""
#Open/Closed
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Order:
    total: float

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, total: float) -> float:
        pass


class RegularDiscount(DiscountStrategy):
    def calculate(self, total: float) -> float:
        return total

class VipDiscount(DiscountStrategy):
    def calculate(self, total: float) -> float:
        return total * 0.9

class EmployeeDiscount(DiscountStrategy):
    def calculate(self, total: float) -> float:
        return total * 0.8

class BlackFridayDiscount(DiscountStrategy):
    def calculate(self, total: float) -> float:
        return total * 0.8

@dataclass
class Customer:
    discount_strategy: DiscountStrategy


def apply_discount(order: Order, customer: Customer) -> float:
    return customer.discount_strategy.calculate(order.total)

order = Order(total=1000.0)

vip_customer = Customer(discount_strategy=VipDiscount())
black_friday_customer = Customer(discount_strategy=BlackFridayDiscount())

print(apply_discount(order, vip_customer))
print(apply_discount(order, black_friday_customer))
"""

"""
#Liskov Substitution
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self, w: int, h: int):
        self._w = w
        self._h = h

    @property
    def width(self) -> int:
        return self._w

    @width.setter
    def width(self, v: int) -> None:
        self._w = v

    @property
    def height(self) -> int:
        return self._h

    @height.setter
    def height(self, v: int) -> None:
        self._h = v

    def area(self) -> int:
        return self._w * self._h

class Square(Shape):
    def __init__(self, side: int):
        self._side = side

    @property
    def side(self) -> int:
        return self._side

    @side.setter
    def side(self, v: int) -> None:
        self._side = v

    def area(self) -> int:
        return self._side * self._side

def resize_and_get_area(r: Rectangle) -> int:
    r.width = 10
    r.height = 5
    return r.area()

rect = Rectangle(2, 3)
print(resize_and_get_area(rect))
"""

"""
#Interface Segregation
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self, text: str) -> None:
        pass


class Scannable(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass


class Faxable(ABC):
    @abstractmethod
    def fax(self, number: str) -> None:
        pass


class Copiable(ABC):
    @abstractmethod
    def copy(self) -> None:
        pass

class SimplePrinter(Printable):
    def print(self, text: str) -> None:
        print(text)


class MultiFunctionalDevice(Printable, Scannable, Copiable):
    def print(self, text: str) -> None:
        print(f"Printing: {text}")

    def scan(self) -> str:
        return "Scanned text"

    def copy(self) -> None:
        print("Copying document")

def print_document(device: Printable, text: str) -> None:
    device.print(text)

printer = SimplePrinter()
print_document(printer, "Hello World")
"""

"""
#Dependency Inversion
from abc import ABC, abstractmethod

class NotificationClient(ABC):
    @abstractmethod
    def send(self, target: str, text: str) -> None:
        pass

class EmailClient(NotificationClient):
    def send(self, target: str, text: str) -> None:
        print(f"[EMAIL to={target}] {text}")


class SmsClient(NotificationClient):
    def send(self, target: str, text: str) -> None:
        print(f"[SMS to={target}] {text}")

class PushNotifier(NotificationClient):
    def send(self, target: str, text: str) -> None:
        print(f"[PUSH to={target}] {text}")

class FakeNotifier(NotificationClient):
    def __init__(self):
        self.sent_messages = []

    def send(self, target: str, text: str) -> None:
        self.sent_messages.append({"to": target, "text": text})


class NotificationService:
    def __init__(self, clients: list[NotificationClient]):
        self._clients = clients

    def notify(self, targets: dict[str, str], text: str) -> None:
        for client in self._clients:
            if isinstance(client, EmailClient) and "email" in targets:
                client.send(targets["email"], text)
            elif isinstance(client, SmsClient) and "phone" in targets:
                client.send(targets["phone"], text)
            elif isinstance(client, PushNotifier) and "push_token" in targets:
                client.send(targets["push_token"], text)
            elif isinstance(client, FakeNotifier):
                client.send(next(iter(targets.values())), text)


real_service = NotificationService([EmailClient(), SmsClient(), PushNotifier()])
contacts = {"email": "user@mail.com", "phone": "+79991112233", "push_token": "token_123"}


real_service.notify(contacts, "Hello!")

fake = FakeNotifier()
test_service = NotificationService([fake])

test_service.notify({"email": "test@mail.com"}, "Test message")
print(fake.sent_messages)
"""