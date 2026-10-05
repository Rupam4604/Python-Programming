# Given a dictionary of products and their prices, find the product with the
# highest price.


dict_products ={"egg" : 8, "oil" : 190, "ghee" : 250, "rice" : 50, "fruits" : 300}

def expensive_product(dict_products):
    return max(dict_products.items(), key=lambda x: x[1])


#dict_products ={"egg" : 8, "oil" : 190, "ghee" : 250, "rice" : 50, "fruits" : 300}
product, price = expensive_product(dict_products)
print(f"most expensive {product} price is {price}")