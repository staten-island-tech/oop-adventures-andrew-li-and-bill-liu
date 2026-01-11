import random
def cut(x):
    return round(x, 2)
def ask(list, prompt = 'type index :'):
    for i, thing in enumerate(list):
        print(f"{i}: {thing}")
    chosen = input(prompt)
    if chosen.lower() == 'x':
        return None
    try:
        index = int(chosen)
        if 0 <= index < len(list):
            return list[index]
        return None
    except:
        return None
def find_item(list, item):
    if isinstance(item, int):
        if 0 <= item < len(list):
            return list[item]
        else:
            return None
    for i in list:
        if i['name'].lower() == item['name'].lower():
            return i
    return None
def proc_chance(x):
    if random.randint(1,100) <= x:
        return True
    else:
        return False
