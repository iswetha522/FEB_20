#  Requirements:
#     * The system should allow to update or add the products to the inventory
#     * Each Product should have 
#         * Id
#         * Name
#         * Model
#         * Cost Price
#         * Selling Price
#         * Number of Items
#     * The System should allow to sell items which means the inventory should be updated.
#     * The system should show the report of items sold
import os

products_file = "products.csv"
products_file_exists = os.path.exists(products_file)
products = []
with open(file=products_file,mode='r') as products_reader:
    products_read_lines = products_reader.readlines()
    for products_read_line in products_read_lines:
        arr = products_read_line.split(',')
        product = [int(arr[0]), arr[1], arr[2], float(arr[3]), float(arr[4], int(arr[5]))]
        products.append(product)
while True:
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
    choice = input(menu)
    if choice == '0':
        if not products_file_exists:
            print('No items in inventory')
            continue
        # open the file in the read mode
        with open(file= products_file, mode='r') as product_file_reader:
            products_file_lines = product_file_reader.readlines()
            for products_file_line in products_file_lines:
                print(products_file_line)
    elif choice == '1':
        # to write the files, use a(append) mode
        id = int(input('Enter the product id = '))
        name = input('Enter the product name = ')
        model = input('Enter the model = ')
        cp = float(input('Enter the cost price = '))
        sp = float(input('Enter the sell price = '))
        quantity = int(input('Enter the availablie quantity = '))
        product = [id,name,model,cp, sp,quantity]
        products.append(product)
        with open(file= products_file, mode= 'a') as products_file_appender:
            if not products_file_exists:
                products_file_appender.writelines(['id,name,model,cp,sp,quanity\n'])
                products_file_exists = True
            products_file_appender.writelines([f"{id},{name},{model},{cp},{sp},{quantity}\n"])
    elif choice == '2' :
        product_id = int(input('Enter the product id to update quantity = '))
        index = -1
        updated_product = []
        for product in products:
            # find product by id
            index += 1
            if product[0] == product_id:
                found = True
                new_quantity = int(input('Enter the quantity to be added = '))
                product[5] += new_quantity
                updated_product = product
                break
        products[index] = updated_product


    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    else:
        exit(0)