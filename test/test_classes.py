import pytest
from src.classes import Category, Product, Smartphone, LawnGrass, ProductMixin


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
        == f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
    )


def test_product_add_():
    product_a = Product("Товар A", "Описание A", 100, 10)
    product_b = Product("Товар B", "Описание B", 200, 2)

    total_value = product_a + product_b
    assert total_value == 1400  # 100 * 10 + 200 * 2 = 1400


def test_add_product_different_types():
    prod = Product("Товар A", "Описание A", 100, 10)
    with pytest.raises(TypeError):
        prod.__add__("Not a product")


def test_smartphone():
    smartphone = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray space"


def test_grass():
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


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


def test_product_str_():
    product = Product("Товар 1", "Описание товара 1", 80, 15)
    assert str(product) == "Товар 1, 80 руб. Остаток: 15 шт."

    product2 = Product("Товар 2", "Описание товара 2", 120, 10)
    assert str(product2) == "Товар 2, 120 руб. Остаток: 10 шт."


def test_category_str_():
    product1 = Product("Товар 1", "Описание товара 1", 80, 15)
    product2 = Product("Товар 2", "Описание товара 2", 120, 10)
    category = Category("Категория 1", "Описание категории 1", [product1, product2])
    assert str(category) == "Категория 1, количество продуктов: 25 шт."


def test_category_add_product():
    category = Category("Electronics", "Devices and gadgets", [])
    smartphone = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    category.add_product(smartphone)
    assert len(category.products) == 1
    assert Category.product_count > 0


def test_product_mixin_attributes():
    product = ProductMixin("Продукт1", "Описание продукта", 1200, 10)
    assert product.name == "Продукт1"
    assert product.description == "Описание продукта"
    assert product.price == 1200
    assert product.quantity == 10


def test_average_price_with_products():
    category = Category("Test Category", "Description")
    category.add_product(Product("Продукт1", "Описание продукта", 100.0, 1))
    category.add_product(Product("Продукт2", "Описание продукта", 200.0, 1))
    category.add_product(Product("Продукт3", "Описание продукта", 300.0, 1))

    assert category.avg_price() == 200.0  # (100 + 200 + 300) / 3 = 200


def test_average_price_empty_category():
    empty_category = Category("Empty Category", "Description")
    assert empty_category.avg_price() == 0  # Не должно быть продуктов, возврат 0


def test_average_price_one_product():
    single_product_category = Category("One Product Category", "Description")
    single_product_category.add_product(
        Product("Продукт1", "Описание продукта", 150.0, 1)
    )
    assert single_product_category.avg_price() == 150.0

