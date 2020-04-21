menu = """
Enter the number 
0 => View Products
1 => Add Product
2 => Update Product
3 => Delete Product
4 => Sell Items
5 => Report
6 => Exit
"""
# structure of dictionary will be
# {
#   '<code>' :  {
#        'name': '<product name>',
#        'quantity': <product quantity> 
#   }  
# }

# example:
#  products = {
#      'dell': { 'name': 'dell', 'cp': 30000, 'sp': 34000, 'quantity': 20, 'model': 'latitude'},
#      'hp': { 'name': 'hp', 'cp': 30000, 'sp': 34000, 'quantity': 20, 'model': 'elitebook'},
# }
products = {}

while True:
    choice = input(menu)
    if choice == '0':
        for code, product in products.items():
            print(f"{code} = {product}")
    elif choice == '1':
        code = input('Enter the product code name = ')
        if code in products:
            print(f'{code} already exists')
            continue
        product = {}
        product['name'] = input('Enter the product name = ')
        product['model'] = input('Enter the model = ')
        product['cp'] = float(input('Enter the cost price = '))
        product['sp'] = float(input('Enter the sell price = '))
        product['quantity'] = int(input('Enter the availablie quantity = '))
        products[code] = product
    elif choice == '2':
        code = input('Enter the product code name = ')
        if code not in products.keys():
            print('Invalid code entered. Please check the code')
            continue
        quantity = int(input('Enter the quantity to be added ='))
        new_quantity = quantity  + products[code]['quantity']
        products[code]['quantity'] = new_quantity
        print(f'quantity updated and new quantity is {new_quantity}')
    elif choice == '3':
        code = input('Enter the product code name = ')
        if code not in products.keys():
            print('Invalid code entered. Please check the code')
            continue
        return_product = products.pop(code)
        print(f"{return_product} has been deleted")
    else:

        exit(0)