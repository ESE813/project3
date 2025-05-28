import pytest
from src.classes import Category, Product


@pytest.fixture
def category():
    return Category("Electronics", "Devices and gadgets")


@pytest.fixture
def product1():
    return Product("Laptop", "A high-performance laptop", 1200.00, 10)


@pytest.fixture
def product2():
    return Product("Smartphone", "Latest model smartphone", 800.00, 20)


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert Category.category_count == 1


def test_product_initialization(product1):
    assert product1.name == "Laptop"
    assert product1.description == "A high-performance laptop"
    assert product1.price == 1200.00
    assert product1.quantity == 10


def test_add_product(category, product1, product2):
    category.add_product(product1)
    category.add_product(product2)
    assert len(category.products) == 2
    assert Category.product_count == 2
