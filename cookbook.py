
def get_ing(i_line):
    i_line = i_line.split(' | ')

    ing_dict = {"ingridient_name" : i_line[0] , 'quantity': int(i_line[1]) ,"measure" : i_line[2].strip()}
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
    return ing_dict




def get_shop_list_by_dishes(*dishes,ingr_dict= creating_dict('df'), person_count = 6):
    list_by_dishes = {}
    for key in ingr_dict.keys():
        for dish in dishes:
            if key == dish:
                for dictionary in ingr_dict[key]:
                    list_by_dishes_name = dictionary['ingridient_name']
                    try:
                        list_by_dishes[list_by_dishes_name]['quantity'] = (dictionary['quantity']*person_count)
                    except:
                           list_by_dishes[list_by_dishes_name] = {"measure": dictionary['measure'],  "quantity": dictionary['quantity'] * person_count}
    for dish in dishes:
        for element in list_by_dishes:
            print(f"{element} = {list_by_dishes[element]}")


print('Словарь из продуктов: ')

print(creating_dict('df'))
print()

get_shop_list_by_dishes(*['Омлет','Омлет'])
