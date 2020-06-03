def get_ing(i_line):
    i_line = i_line.split(' | ')

    ing_dict = {"ingredient_name" : i_line[0] , 'quantity': i_line[1] ," measure" : i_line[2].strip()}
    return ing_dict


def creating_dict(file_name):
    ing_dict = {}
    with open(file_name, 'r') as f:
        for line in f:
            if ('|' not in line) and (len(line) > 2):
                x = line.strip()
            elif '|' in line:
                ing_dict.setdefault(x, [])
                ing_dict[x].append(get_ing(line))
    print(ing_dict)

def get_shop_list_by_dishes(dishes, person_count,ing_dict):
    list_by_dishes = { }
    for dish in dishes:
        for ingridient in ing_dict[dish]:
            if ingridient["ingridient_name"] not in list_by_dishes.keys():
                list_by_dishes[ingridient["ingridient_name"]] = {"measure": ingridient["measure"], "quantity": ingridient["quantity"] * person_count}
            else:
                list_by_dishes[ingridient["ingridient_name"]]["quantity"] += ingridient["quantity"] * person_count
    print(list_by_dishes)

print('Словарь из продуктов: ')

creating_dict('df')
print()

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2,ing_dict)


