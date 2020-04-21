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

products = []
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
        print(products)
    elif choice == '1':
        id = int(input('Enter the product id = '))
        name = input('Enter the product name = ')
        model = input('Enter the model = ')
        cp = float(input('Enter the cost price = '))
        sp = float(input('Enter the sell price = '))
        product = [id,name,model,cp, sp]
        products.append(product)
    elif choice == '2' :
        id = int(input('Enter the product id = '))
        name = input('Enter the product name = ')
        model = input('Enter the model = ')
        cp = float(input('Enter the cost price = '))
        sp = float(input('Enter the sell price = '))
        product = [id,name,model,cp, sp]
        products.insert(0,product)
    elif choice == '3':
        products.remove(product)
    elif choice == '4':
        products.pop(products[1])
    elif choice == '5':
        print(products)
    else:
        exit(0)

    