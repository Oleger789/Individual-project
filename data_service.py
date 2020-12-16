def get_price():
    with open("./data/price.txt") as file:
        from_file = file.readlines()
        #Массив с ценами
        arr_price = []
        for line in from_file:
            line = line[0:-1]
            line_list = line.split(";")
            arr_price.append(line_list)

        return arr_price

def show_price(price):

    input_code_from = input("Какой код вашего товара?\n")
    input_code_to = input("До какого кода ваш товар?\n")
    for line in price:
        if input_code_from <= line[0] <= input_code_to:
           print("Код товара: {} Ціни на 2.11: {} Ціни на 10.11: {} Ціни на 14.11: {} Ціни на 23.11: {} Рік: {}".format(line[0], line[1], line[2], line[3], line[4], line[5]))

def get_product():
    with open("./data/product.txt") as file:
        from_file = file.readlines()

        arr_product = []
        for line in from_file:
            line = line[0:-1]
            line_list = line.split(";")
            arr_product.append(line_list)

    return arr_product

def show_product(product):
    input_code_from = input("Какой код вашего товара?\n")
    input_code_to = input("До какого кода ваш товар ?\n")
    for line in product:
        if input_code_from <= line[0] <= input_code_to:
            print("Код товара: {} Найменування товару: {} ".format(line[0], line[1]))
