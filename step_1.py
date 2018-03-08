def transform_products_to_list(products_string):
    split_products = products_string.split('\n')
    products_list = []
    for products_line in split_products:
        if products_line:
            product = products_line.split(',')
            products_list.append(product)
    return products_list