list_of_products = ["хлеб", "молоко", "сыр", "колбаса", "кефир"]
for product in filter(lambda x: len(x) % 2 == 0, list_of_products):
    print(product)
