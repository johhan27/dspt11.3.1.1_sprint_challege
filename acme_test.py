import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_values():
    """Test default product price being 10."""
    prod = Product('Test Product')
    assert (prod.price == 10 and
            prod.weight == 20 and
            prod.flammability == 0.5)


def test_product_methods():
    """Test stealability() and explode() with non default values"""
    prod = Product("Test Product 1", price=100, weight=50, flammability=0.1)
    assert (prod.stealability() == "Very stealable" and
            prod.explode() == "...fizzle")


def test_default_num_products():
    assert len(generate_products()) == 30


def test_legal_names():
    for product in generate_products():
        adj, noun = product.name.split()
        assert (adj in ADJECTIVES and noun in NOUNS)