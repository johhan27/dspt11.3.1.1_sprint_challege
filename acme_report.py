import random
from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    while len(products) < num_products:
        product = Product(
            name=random.sample(ADJECTIVES, k=1)[0] + " " + random.sample(NOUNS, k=1)[0],
            price=random.randint(5, 10),
            weight=random.randint(5, 10),
            flammability=random.uniform(0, 2.5))
        products.append(product)
    return products


def inventory_report(products):
    names = []
    prices = []
    weights = []
    flammabilities = []

    for product in products:
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

    num_unique_names = len(set(names))
    avg_price = sum(prices) / len(prices)
    avg_weight = sum(weights) / len(weights)
    avg_flammability = sum(flammabilities) / len(flammabilities)

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: ", num_unique_names)
    print("Average price: ", avg_price)
    print("Average weight: ", avg_weight)
    print("Average flammability: ", avg_flammability)

    return num_unique_names, avg_price, avg_weight, avg_flammability


if __name__ == '__main__':
    inventory_report(generate_products())
