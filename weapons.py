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
        'name':'Whalen Dagger',
        'dmgbuff':900,
        'scales':False
    },
    {
        'id':5,
        'name':'Whalen Pro Max',
        'dmgbuff':1000,
        'scales':False
    },
    {
        'id':6,
        'name':'Mecha Whalen Core',
        'dmgbuff':1200,
        'scales':False
    }
]

def filter(list, parameter):
    return [t for t in list if parameter.lower() in t['name'].lower()]

