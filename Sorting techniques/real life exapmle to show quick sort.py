import random
class Product:
    def __init__(self, name, sales):
        self.name = name
        self.sales = sales
    def __repr__(self):
        return f"Product('{self.name}', {self.sales})"
def quicksort_products(products, low, high):
    if low < high:
        pivot_index = partition(products, low, high)
        quicksort_products(products, low, pivot_index - 1)
        quicksort_products(products, pivot_index + 1, high)
def partition(products, low, high):
    pivot = products[high].sales
    i = low - 1
    for j in range(low, high):
        if products[j].sales >= pivot:
            i += 1
            products[i], products[j] = products[j], products[i]
    products[i + 1], products[high] = products[high], products[i + 1]
    return i + 1
# Generate sample data
product_names = ["Laptop", "Smartphone", "Headphones", "Tablet", "Smartwatch", "Camera", "Speaker", "Keyboard",
"Mouse", "Monitor"]
products = [Product(name, random.randint(100, 10000)) for name in product_names]
# Sort products by sales
quicksort_products(products, 0, len(products) - 1)
# Display top 5 products
print("Top 5 selling products:")
for i, product in enumerate(products[:5], 1):
    print(f"{i}. {product.name}: {product.sales} units")
