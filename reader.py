from random import choice

from model import Weapon, Model, Buff


def read_units_file(name):
    units = {}
    with open(name) as f:
        lines = f.readlines()
        for line in lines[1:]:
            unit = []
            items = line.strip().split(', ')
            unit += [int(x) for x in items[1:]]
            units[items[0]] = unit

    # print(units)
    return units


def read_weapon_file(name):
    weapons = {}
    with open(name) as f:
        lines = f.readlines()
        for line in lines[1:]:
            items = line.strip().split(', ')
            weapons[items[0]] = items[1:]

    # print(weapons)
    return weapons


def read_options_file(name):
    options = {}

    with open(name) as f:
        lines = f.readlines()
        for line in lines[1:]:
            items = line.strip().split(', ')
            prev = options.get(items[0], None)
            if prev is None:
                options[items[0]] = [items[1:]]
            else:
                options[items[0]] = prev + [items[1:]]

    # print(options)
    return options


def random_model(units, options, weapons):
    u = choice(list(units.keys()))
    model_weapons = []
    for option in options[u]:
        if len(option) == 0:
            continue
        option_name = choice(option)
        model_weapons.append(Weapon(option_name, *weapons[option_name]))
    return Model(u, *units[u], model_weapons)


# if __name__ == '__main__':
