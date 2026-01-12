lista_weapons = [
    {
        'id':1,
        'name':'fists',
        'dmgbuff':2,
        'scales':True
    },
    {
        'id':2,
        'name':'Whalen Blade',
        'dmgbuff':9999999999999999999999999999999999,
        'scales':True
    },
    {
        'id':3,
        'name':'test sword',
        'dmgbuff':1,
        'scales':False
    },
    {
        'id':4,
        'name':'tester pro max',
        'dmgbuff':900,
        'scales':False
    }
]

def filter(list, parameter):
    return [t for t in list if parameter.lower() in t['name'].lower()]

