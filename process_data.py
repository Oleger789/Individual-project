from data_service import get_price, get_product

temp_analytic = {
    "name"      : "", #Найменування товару
    "year"      : 0,  #Рік
    "mid_price" : 0,  #Середня ринкова ціна за місяць
    "retail"    : 0,
    "changes"   : 0
}

#Аналіз змін
def get_analytics():

    # Получаем информацию о продукте по коду товара
    def get_product_info(code):

        # Ищем нужный продукт по коду
        for product in products:
            if product[0] == code:
                return product

        return "Продукт не знайдено!"


    #Массив з кінцевою інформаціею
    analytic_list = []

    #Отримуемо 2 таблиці
    products = get_product()
    prices = get_price()


    for price in prices:
        temp = temp_analytic.copy()

        product = get_product_info(price[0])

        temp["name"] = product[1]
        temp["year"] = price[5]
        temp["mid_price"] = round((float(price[1]) + float(price[2]) + float(price[3]) + float(price[4])) / 4,2)
        temp["retail"] = product[3]
        temp["changes"] = round(float(temp["retail"]) - float(price[4]), 2)

        analytic_list.append(temp)

    return analytic_list
