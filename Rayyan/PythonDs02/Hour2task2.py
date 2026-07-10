product = {"Name":"Apple", "Price":300, "Quantity":4}
product.update({"Price":400})
print(product)

print(product.pop("Quantity"))
print(product)

print(product.get("x1","not exist"))