from step_1 import transform_products_to_list

def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    
    products = {}
    for product in products_list:
        customer_id = product[-2]
        invoice_id = product[0]
        products.setdefault(customer_id, {})
        products[customer_id].setdefault(invoice_id, 0)
        products[customer_id][invoice_id] += round((float(product[-3]) * float(product[-5])), 2)
    return products