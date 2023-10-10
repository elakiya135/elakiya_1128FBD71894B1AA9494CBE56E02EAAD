def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage
products = ['Apple', 'Banana', 'Apple', 'Orange', 'Apple', 'Grapes']
target = 'Apple'
result = linear_search_product(products, target)
print("Indices of", target, ":", result)  # Output: Indices of Apple : [0, 2, 4]


