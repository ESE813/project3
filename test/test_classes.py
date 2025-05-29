import pytest
from src.classes import Category, Product


@pytest.fixture
def category():
    return Category("Electronics", "Devices and gadgets", [])


@pytest.fixture
def product(product_data):
    return Product(**product_data)


@pytest.fixture
def product_data():
    return {
        "name": "Laptop",
        "description": "A high-performance laptop",
        "price": 1200.00,
        "quantity": 10,
    }


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert Category.category_count == 1
    assert category.products == []


def test_product_initialization(product):
    assert product.name == "Laptop"
    assert product.description == "A high-performance laptop"
    assert product.price == 1200.00
    assert product.quantity == 10


def test_add_product(category, product):
    category.add_product(product)
    category.add_product(product)
    assert len(category.products) == 2
    assert Category.product_count == 2
    assert (
        category.products[0]
        == f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
    )


def test_new_product(product_data):
    new_product = Product.new_product(product_data)
    assert new_product.name == product_data["name"]
    assert new_product.description == product_data["description"]
    assert new_product.price == product_data["price"]
    assert new_product.quantity == product_data["quantity"]


def test_category_count():
    initial_count = Category.category_count
    Category("Home Appliances", "Appliances for home", [])
    assert Category.category_count == initial_count + 1


def test_price_setter(product):
    product.price = 1500.00
    assert product.price == 1500.00
