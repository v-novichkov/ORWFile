from pprint import pprint
Recipes = "recipes.txt"
cook_book = dict()


def get_data(file_name):

    with open(file_name) as file:
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