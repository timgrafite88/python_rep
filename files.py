
#чтение из файла
def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            num_ingredients = int(file.readline().strip())
            ingredients = []
            for _ in range(num_ingredients):
                ingredient, quantity, measure = file.readline().strip().split(' | ')
                measure = measure.replace(' |', '').strip()
                measure = measure.replace('.', '')
                ingredients.append({'ingredient_name': ingredient, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book

#подсчет ингридиентов для указанного количества персон
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

#объединение файлов
def merge_files(file_names, output_file):
    file_info = []
    for file_name in file_names:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            file_info.append((file_name, len(lines), lines))
    file_info.sort(key=lambda x: x[1])

    with open(output_file, 'w') as file:
        for name, num_lines, lines in file_info:
            file.write(f"{name}\n{num_lines}\n")
            file.writelines(lines)


#тестирование функций
cook_book = read_recipes('recipes.txt')
print(cook_book)

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shop_list)

file_names = ['1.txt', '2.txt']
merge_files(file_names, 'merged_file.txt')