class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.readlines()
        file.close()
        cleaned_products = []
        for product in products:
            cleaned_product = product.strip()
            cleaned_products.append(cleaned_product)
        result = '\n'.join(cleaned_products)
        return result

    def add(self, *products):
        existing_products = self.get_products()
        existing_products_list = existing_products.split('\n')
        file = open(self.__file_name, 'a')
        for product in products:
            product_str = str(product)
            if product_str in existing_products_list:
                print(f'Продукт {product_str} уже есть в магазине')
            else:
                file.write(product_str + '\n')
                existing_products_list.append(product_str)

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
