from typing import Dict, Any
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов,
    представляющий общую функциональность"""

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass


class ProductMixin:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, ProductMixin):
    name: str
    description: str
    price: float
    quantity: int

    @classmethod
    def new_product(cls, product_data: Dict[str, Any] = None):
        if product_data is None:
            product_data = {}
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
        )

    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных типов.")


class Smartphone(Product):
    efficiency: int
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return [str(product) for product in self.__products]

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def avg_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            average = total_price / len(self.__products)
            return average
        except ZeroDivisionError:
            return 0
