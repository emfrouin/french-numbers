import math

# Identify number type
def nameNumber(num):
    if num>=0 and num<=16:
        name = nameUnit(num)
    elif num >=1000000:
        raise Exception(OverflowError)
    elif num >= 1000:
        name = nameThousand(num)
    elif num >= 100:
        name = nameHundred(num)
    elif num >= 16:
        name = nameTen(num)
    return name


# name a number 0-16
def nameUnit(num):
    unitdictionary= {
         0: 'zéro', 
         1: 'un',
         2: 'deux',
         3: 'trois',
         4: 'quatre',
         5: 'cinq', 
         6: 'six', 
         7: 'sept',
         8: 'huit',
         9: 'neuf', 
         10: 'dix',
         11: 'onze',
         12: 'douze',
         13: 'treize',
         14: 'quatorze',
         15: 'quinze',
         16: 'seize' 
         }
    return unitdictionary[num]

# name a number 16 and up 
def nameTen(num):
    tensdictionary = {
        10: 'dix',
        20: 'vingt',
        30: 'trente',
        40: 'quarante',
        50: 'cinquante',
        60: 'soixante',
        80: 'quatre-vingt',
    }
    ten = math.floor(num/10) * 10
    if ten == 70:
        ten = 60
    if ten == 90:
        ten = 80

    if num % 10 == 0 and not (num in [70, 90]):
        return tensdictionary[ten]
    
    name = nameNumber(num - ten)
    if num % 10 == 1 and not (num in [81, 91]):
        return f"{tensdictionary[ten]}-et-{name}"
    return f"{tensdictionary[ten]}-{name}"


# name a number 100 and up
def nameHundred(num):
    name = 'cent'
    hundred = math.floor(num/100)
    if hundred > 1:
        name = name + 's'
        name = nameNumber(hundred) + '-' + name
    if num % 100 != 0:    
        name = name + '-' + nameNumber(num % 100)
    return name

#name a number 1000 and up
def nameThousand(num):
    name = 'mille'
    thousand = math.floor(num/1000)
    if thousand > 1:
        name = name + 's'
        name = nameNumber(thousand) + '-' + name
    if num % 1000 != 0:    
        name = name + '-' + nameNumber(num % 1000)
    return name
