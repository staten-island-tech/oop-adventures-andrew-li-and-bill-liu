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
        return list[item] if 0 <= item < len(list) else None
    for i in list:
        if i['name'].lower() == item.lower():
            return i
    return None