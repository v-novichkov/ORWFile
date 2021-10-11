from pprint import pprint
Recipes = "recipes.txt"
cook_book = dict()


def get_data(file_name):

    with open(file_name, encoding="utf-8") as file:
        for line in file:
            cook_name = line.strip()
            amound_cook = int(file.readline())

            temp_list = []
            for item in range(amound_cook):
                ingredient, quantity, measure = file.readline().split('|')
                temp_list.append(
                    {"ingredient_name": ingredient, "quantity": quantity, "measure": measure}
                )
            cook_book[cook_name] = temp_list

            file.readline()
    return cook_book


pprint(get_data(Recipes))


def get_shop_list_by_dishes(dishes, person_count):
    cooking_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] not in cooking_list:
                    val = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
                    cooking_list[ingr['ingredient_name']] = val
                else:
                    cooking_list[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count

    return cooking_list

