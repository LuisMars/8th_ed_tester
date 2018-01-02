import random

from reader import *


def defend_against():
    units = read_units_file('units.txt')
    weapons = read_weapon_file('weapon_profiles.txt')
    options = read_options_file('options.txt')
    buffs = read_weapon_file('buffs.txt')

    Buff('Sacred Banner', *buffs['Sacred Banner']),
    Buff('Rites of Battle', *buffs['Rites of Battle'])

    models_to_test = ['Grey Knight', 'Justicar',
                      'Interceptor', 'Interceptor Justicar',
                      'Purifier', 'Knight of the Flame',
                      'Grey Knight Terminator', 'Terminator Justicar',
                      'Paladin', 'Paragon',
                      'Nemesis Dreadknight',
                      'Grey Knight Dreadnought',
                      'Grey Knight Venerable Dreadnought',
                      'Grand Master',
                      'Paladin Ancient',
                      'Brotherhood Champion (Sword Strike)',
                      'Brotherhood Champion (Blade Shield)',
                      'Brother-Captain',
                      'Librarian in Terminator Armour',
                      'Razorback',
                      'Rhino',
                      'Castellan Crowe',
                      'Lord Kaldor Draigo']

    for model in models_to_test:
        if model == 'Lord Kaldor Draigo':
            specials = [Model(model, *units[model], [
                Weapon('The Titansword', *weapons['The Titansword']),
                Buff('Chapter Master', *buffs['Chapter Master']),
            ])]
        elif model == 'Castellan Crowe':
            specials = [Model(model, *units[model], [
                Weapon('None', *weapons['None']),
                Buff('Master Swordsman (hit)', *buffs['Master Swordsman (hit)']),
                Buff('Master Swordsman (wound)', *buffs['Master Swordsman (wound)']),
            ])]
        elif model.count('Dreadnought') == 1:
            specials = [Model(model, *units[model], [Weapon('None', *weapons['None'])]),
                        Model(model, *units[model],
                              [Weapon('Dreadnought combat weapon', *weapons['Dreadnought combat weapon'])])]
        elif model == 'Rhino' or model == 'Razorback':
            specials = [Model(model, *units[model], [Weapon('None', *weapons['None'])])]
        elif model.count('Brotherhood Champion'):
            if model.count('Sword Strike') == 1:
                specials = [Model(model, *units[model], [
                    Weapon('Nemesis force sword (Sword Strike)', *weapons['Nemesis force sword (Sword Strike)'])])]
            else:
                specials = [
                    Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword'])])]
        elif model == 'Nemesis Dreadknight':
            specials = [Model(model, *units[model], [Weapon('Dreadfist (single)', *weapons['Dreadfist (single)'])]),
                        Model(model, *units[model], [Weapon('Dreadfist (pair)', *weapons['Dreadfist (pair)'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis Daemon greathammer', *weapons['Nemesis Daemon greathammer'])]),
                        Model(model, *units[model], [Weapon('Nemesis greatsword', *weapons['Nemesis greatsword'])])]
        elif model == 'Grey Knight' or model == 'Interceptor' or model == 'Purifier':
            specials = [Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis Daemon hammer', *weapons['Nemesis Daemon hammer'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis falchion (pair)', *weapons['Nemesis falchion (pair)'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis warding stave', *weapons['Nemesis warding stave']), Buff('Nemesis warding stave', *buffs['Nemesis warding stave']) ]),
                        Model(model, *units[model],
                              [Weapon('Nemesis force halberd', *weapons['Nemesis force halberd'])]),
                        Model(model, *units[model], [Weapon('None', *weapons['None'])])]
        else:
            specials = [Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis Daemon hammer', *weapons['Nemesis Daemon hammer'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis falchion (pair)', *weapons['Nemesis falchion (pair)'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis warding stave', *weapons['Nemesis warding stave']), Buff('Nemesis warding stave', *buffs['Nemesis warding stave']) ]),
                        Model(model, *units[model],
                              [Weapon('Nemesis force halberd', *weapons['Nemesis force halberd'])])]

            if model == 'Grand Master':
                specials = [Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword']),
                                                         Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis Daemon hammer', *weapons['Nemesis Daemon hammer']),
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis falchion (pair)', *weapons['Nemesis falchion (pair)']),
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis warding stave', *weapons['Nemesis warding stave']), Buff('Nemesis warding stave', *buffs['Nemesis warding stave']) ,
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis force halberd',
                                          *weapons['Nemesis force halberd']),
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Voldus', *weapons['Voldus']),
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])])]
            if model == 'Paladin Ancient':
                specials = [Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword']),
                                                         Buff('Sacred Banner', *buffs['Sacred Banner'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis Daemon hammer', *weapons['Nemesis Daemon hammer']),
                                   Buff('Sacred Banner', *buffs['Sacred Banner'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis falchion (pair)', *weapons['Nemesis falchion (pair)']),
                                   Buff('Sacred Banner', *buffs['Sacred Banner'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis warding stave', *weapons['Nemesis warding stave']), Buff('Nemesis warding stave', *buffs['Nemesis warding stave']) ,
                                   Buff('Sacred Banner', *buffs['Sacred Banner'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis force halberd',
                                          *weapons['Nemesis force halberd']),
                                   Buff('Sacred Banner', *buffs['Sacred Banner'])])]
        for t in specials:
            s = model + '\t' + t.melee.name + '\t'
            for enemy_name in ['Genestealer', 'Space Marine', 'Terminator', 'Dreadnought', 'Roboute Guilliman']:
                m2 = Model(enemy_name, *units[enemy_name], [Weapon('None', *weapons['None'])])

                result = m2.attack_rolls(t)
                s += str(result / t.wounds) + '\t' + str((result / t.wounds) * t.get_points()) + '\t'
            print(s)
        print()


def fight_against():
    units = read_units_file('units.txt')
    weapons = read_weapon_file('weapon_profiles.txt')
    options = read_options_file('options.txt')
    buffs = read_weapon_file('buffs.txt')

    Buff('Sacred Banner', *buffs['Sacred Banner']),
    Buff('Rites of Battle', *buffs['Rites of Battle'])

    models_to_test = ['Grey Knight', 'Justicar',
                      'Interceptor', 'Interceptor Justicar',
                      'Purifier', 'Knight of the Flame',
                      'Grey Knight Terminator', 'Terminator Justicar',
                      'Paladin', 'Paragon',
                      'Nemesis Dreadknight',
                      'Grey Knight Dreadnought',
                      'Grey Knight Venerable Dreadnought',
                      'Grand Master',
                      'Paladin Ancient',
                      'Brotherhood Champion (Sword Strike)',
                      'Brotherhood Champion (Blade Shield)',
                      'Brother-Captain',
                      'Librarian in Terminator Armour',
                      'Razorback',
                      'Rhino',
                      'Castellan Crowe',
                      'Lord Kaldor Draigo']

    for model in models_to_test:
        if model == 'Lord Kaldor Draigo':
            specials = [Model(model, *units[model], [
                Weapon('The Titansword', *weapons['The Titansword']),
                Buff('Chapter Master', *buffs['Chapter Master']),
            ])]
        elif model == 'Castellan Crowe':
            specials = [Model(model, *units[model], [
                Weapon('None', *weapons['None']),
                Buff('Master Swordsman (hit)', *buffs['Master Swordsman (hit)']),
                Buff('Master Swordsman (wound)', *buffs['Master Swordsman (wound)']),
            ])]
        elif model.count('Dreadnought') == 1:
            specials = [Model(model, *units[model], [Weapon('None', *weapons['None'])]),
                        Model(model, *units[model],
                              [Weapon('Dreadnought combat weapon', *weapons['Dreadnought combat weapon'])])]
        elif model == 'Rhino' or model == 'Razorback':
            specials = [Model(model, *units[model], [Weapon('None', *weapons['None'])])]
        elif model.count('Brotherhood Champion'):
            if model.count('Sword Strike') == 1:
                specials = [Model(model, *units[model], [
                    Weapon('Nemesis force sword (Sword Strike)', *weapons['Nemesis force sword (Sword Strike)'])])]
            else:
                specials = [
                    Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword'])])]
        elif model == 'Nemesis Dreadknight':
            specials = [Model(model, *units[model], [Weapon('Dreadfist (single)', *weapons['Dreadfist (single)'])]),
                        Model(model, *units[model], [Weapon('Dreadfist (pair)', *weapons['Dreadfist (pair)'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis Daemon greathammer', *weapons['Nemesis Daemon greathammer'])]),
                        Model(model, *units[model], [Weapon('Nemesis greatsword', *weapons['Nemesis greatsword'])])]
        elif model == 'Grey Knight' or model == 'Interceptor' or model == 'Purifier':
            specials = [Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis Daemon hammer', *weapons['Nemesis Daemon hammer'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis falchion (pair)', *weapons['Nemesis falchion (pair)'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis warding stave', *weapons['Nemesis warding stave']), Buff('Nemesis warding stave', *buffs['Nemesis warding stave']) ]),
                        Model(model, *units[model],
                              [Weapon('Nemesis force halberd', *weapons['Nemesis force halberd'])]),
                        Model(model, *units[model], [Weapon('None', *weapons['None'])])]
        else:
            specials = [Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis Daemon hammer', *weapons['Nemesis Daemon hammer'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis falchion (pair)', *weapons['Nemesis falchion (pair)'])]),
                        Model(model, *units[model],
                              [Weapon('Nemesis warding stave', *weapons['Nemesis warding stave']), Buff('Nemesis warding stave', *buffs['Nemesis warding stave']) ]),
                        Model(model, *units[model],
                              [Weapon('Nemesis force halberd', *weapons['Nemesis force halberd'])])]

            if model == 'Grand Master':
                specials = [Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword']),
                                                         Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis Daemon hammer', *weapons['Nemesis Daemon hammer']),
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis falchion (pair)', *weapons['Nemesis falchion (pair)']),
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis warding stave', *weapons['Nemesis warding stave']), Buff('Nemesis warding stave', *buffs['Nemesis warding stave']) ,
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis force halberd',
                                          *weapons['Nemesis force halberd']),
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])]),
                            Model(model, *units[model],
                                  [Weapon('Voldus', *weapons['Voldus']),
                                   Buff('Rites of Battle', *buffs['Rites of Battle'])])]
            if model == 'Paladin Ancient':
                specials = [Model(model, *units[model], [Weapon('Nemesis force sword', *weapons['Nemesis force sword']),
                                                         Buff('Sacred Banner', *buffs['Sacred Banner'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis Daemon hammer', *weapons['Nemesis Daemon hammer']),
                                   Buff('Sacred Banner', *buffs['Sacred Banner'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis falchion (pair)', *weapons['Nemesis falchion (pair)']),
                                   Buff('Sacred Banner', *buffs['Sacred Banner'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis warding stave', *weapons['Nemesis warding stave']), Buff('Nemesis warding stave', *buffs['Nemesis warding stave']) ,
                                   Buff('Sacred Banner', *buffs['Sacred Banner'])]),
                            Model(model, *units[model],
                                  [Weapon('Nemesis force halberd',
                                          *weapons['Nemesis force halberd']),
                                   Buff('Sacred Banner', *buffs['Sacred Banner'])])]
        for t in specials:
            s = model + '\t' + t.melee.name + '\t'
            for enemy_name in ['Genestealer', 'Space Marine', 'Terminator', 'Dreadnought', 'Roboute Guilliman']:
                m2 = Model(enemy_name, *units[enemy_name], [])
                result = t.attack_rolls(m2)
                s += str(result / m2.wounds) + '\t' + str(result / t.get_points()) + '\t'
            print(s)
        print()


def shoot_against():
    units = read_units_file('units.txt')
    weapons = read_weapon_file('weapon_profiles.txt')
    options = read_options_file('options.txt')
    buffs = read_weapon_file('buffs.txt')

    units_to_test = [['Grey Knight', 'Justicar'],
                     ['Interceptor', 'Interceptor Justicar'],
                     ['Purifier', 'Knight of the Flame'],
                     ['Grey Knight Terminator', 'Terminator Justicar'],
                     ['Paladin', 'Paragon'],
                     ['Nemesis Dreadknight'],
                     ['Grey Knight Dreadnought'],
                     ['Grey Knight Venerable Dreadnought'],
                     ['Razorback'],
                     ['Rhino']]

    for squad in units_to_test:
        troop_size = 0
        special_size = 1

        if squad[0].count('Dreadnought') == 1:
            troop_size = 0
            special_size = 1
            specials = [Model(squad[0], *units[squad[0]], [Weapon('Assault cannon', *weapons['Assault cannon'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Heavy flamer', *weapons['Heavy flamer'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Frag missile', *weapons['Frag missile'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Krak missile', *weapons['Krak missile'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Twin autocannon', *weapons['Twin autocannon'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Twin Heavy flamer', *weapons['Twin Heavy flamer'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Twin Heavy bolter', *weapons['Twin Heavy bolter'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Twin Lascannon', *weapons['Twin Lascannon'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Storm bolter', *weapons['Storm bolter'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Multi-melta', *weapons['Multi-melta'])]),
                        Model(squad[0], *units[squad[0]],
                              [Weapon('Heavy plasma cannon', *weapons['Heavy plasma cannon'])])]
        elif squad[0] == 'Rhino':
            specials = [Model(squad[0], *units[squad[0]], [Weapon('Storm bolter', *weapons['Storm bolter'])])]
        elif squad[0] == 'Razorback':
            specials = [Model(squad[0], *units[squad[0]], [Weapon('Twin Heavy flamer', *weapons['Twin Heavy flamer'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Twin Heavy bolter', *weapons['Twin Heavy bolter'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Twin Lascannon', *weapons['Twin Lascannon'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Storm bolter', *weapons['Storm bolter'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Twin Assault cannon', *weapons['Twin Assault cannon'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Lascannon', *weapons['Lascannon'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Twin Plasma gun', *weapons['Twin Plasma gun'])])]
        elif squad[0] == 'Nemesis Dreadknight':
            troop_size = 0
            special_size = 1
            specials = [Model(squad[0], *units[squad[0]], [Weapon('Heavy incinerator', *weapons['Heavy Incinerator'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Gatling Psilencer', *weapons['Gatling Psilencer'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Heavy Psycannon', *weapons['Heavy Psycannon'])])]
        elif squad[0] == 'Grey Knight':
            specials = [Model(squad[0], *units[squad[0]], [Weapon('Storm bolter', *weapons['Storm bolter'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Psilencer', *weapons['Psilencer'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Psycannon', *weapons['Psycannon'])]),
                        Model(squad[0], *units[squad[0]], [Weapon('Incinerator', *weapons['Incinerator'])])]
        else:
            specials = [Model(squad[0], *units[squad[0]], [Weapon('Storm bolter', *weapons['Storm bolter'])]),
                        Model(squad[0], *units[squad[0]],
                              [Weapon('Psilencer (Terminator)', *weapons['Psilencer (Terminator)'])]),
                        Model(squad[0], *units[squad[0]],
                              [Weapon('Psycannon (Terminator)', *weapons['Psycannon (Terminator)'])]),
                        Model(squad[0], *units[squad[0]],
                              [Weapon('Incinerator (Terminator)', *weapons['Incinerator (Terminator)'])])]
        troop = Model(squad[0], *units[squad[0]],
                      [Weapon('Storm bolter', *weapons['Storm bolter'])]
                      )
        for t in specials:
            s = squad[0] + '\t' + t.ranged.name + '\t'
            for enemy_name in ['Genestealer', 'Space Marine', 'Terminator', 'Dreadnought', 'Roboute Guilliman']:
                m2 = Model(enemy_name, *units[enemy_name], [])
                list_range = list(range(24, 48, 2))
                avg_result = 0
                avg_wounds_per_point = 0
                for shoot_range in list_range:
                    troops_shooting = troop.shoot_rolls(m2, shoot_range, moved=shoot_range < 24) * troop_size
                    result = troops_shooting + t.shoot_rolls(m2, shoot_range, moved=shoot_range < 24) * special_size
                    avg_result += result
                    avg_wounds_per_point += result / (troop.get_points() * troop_size + t.get_points() * special_size)
                avg_result /= len(list_range)
                avg_wounds_per_point /= len(list_range)
                s += str(avg_result / m2.wounds) + '\t' + str(avg_wounds_per_point) + '\t'
            print(s)
        print()


defend_against()
