from math import sqrt


class Mini:
    def __init__(self, to_hit, to_shoot, strength, toughness, wounds, attacks, save, special_save, damage, ap, name):
        self.to_hit = (6 - to_hit) / 6
        self.to_shoot = (to_shoot - 1) / 6
        self.strength = strength
        self.toughness = toughness
        self.attacks = attacks
        self.wounds = wounds
        self.save = (save - 1)
        self.special_save = (special_save - 1)
        if damage == '1d3':
            self.damage = 2
        elif damage == '1d6':
            self.damage = 3.5
        else:
            self.damage = damage
        self.ap = ap
        self.name = name

    def wound_roll(self, other):
        if self.strength == other.toughness:
            return 3 / 6
        elif self.strength >= other.toughness * 2:
            return 5 / 6
        elif self.strength > other.toughness:
            return 4 / 6
        elif self.strength <= other.toughness / 2:
            return 1 / 6
        else:
            return 2 / 6

    def hit_roll(self):
        return self.to_hit

    def save_roll(self, ap):
        return min(self.special_save, (self.save - ap)) / 6

    def attack_rolls(self, other):
        return self.attacks * min(other.wounds, self.hit_roll() * self.wound_roll(other) * other.save_roll(self.ap) * self.damage)


if __name__ == '__main__':

    minis = [
        Mini(4, 4, 3, 3, 1, 1, 5, 7, 1, 0, 'Guardsman'),
        Mini(4, 4, 4, 3, 1, 1, 6, 7, 1, 0, 'Ork'),
        Mini(3, 3, 4, 4, 1, 2, 3, 7, 1, 0, 'Marine'),
        Mini(3, 3, 4, 4, 1, 1, 3, 7, '1d3', -3, 'Grey Knight sword'),
        Mini(3, 3, 5, 4, 1, 1, 3, 7, '1d3', -2, 'Grey Knight axe'),
        Mini(3, 3, 6, 4, 1, 1, 3, 7, '1d3', -1, 'Grey Knight stave'),
        Mini(3, 3, 4, 4, 2, 3, 2, 5, 1, 0, 'Terminator'),
        Mini(3, 3, 4, 4, 2, 3, 2, 7, 1, 0, 'Primaris'),
        Mini(3, 3, 4, 4, 2, 2, 2, 5, '1d3', -3, 'Grey Knight Terminator'),
        Mini(3, 3, 6, 7, 8, 4, 3, 5, 1, 0, 'Dreadnough'),
        Mini(3, 5, 8, 8, 18, 4, 3, 7, 1, 0, 'Morknaut full'),
        Mini(4, 5, 8, 8, 9, 3, 3, 7, 1, 0, 'Morknaut 9'),
        Mini(5, 5, 8, 8, 4, 2, 3, 7, 1, 0, 'Morknaut 4'),
        Mini(2, 2, 6, 6, 9, 6, 2, 4, 1, 0, 'Guilliman'),
        Mini(2, 2, 9, 6, 9, 6, 2, 4, '1d3', -3, 'Guilliman cool'),
        Mini(2, 2, 9, 6, 9, 6, 2, 4, '1d6', -3, 'Guilliman uber cool'),
        Mini(3, 3, 8, 8, 24, 4, 3, 5, 6, 0, 'Knight errant'),
        Mini(4, 4, 8, 8, 12, 4, 3, 5, 6, 0, 'Knight errant 12'),
        Mini(5, 5, 8, 8, 6, 4, 3, 5, 6, 0, 'Knight errant 6'),
        Mini(3, 3, 4, 4, 3, 3, 2, 5, '1d3', -3, 'Paladin'),
    ]
    names = ('Guardman', 'Ork    ', 'Marine ', 'GK sword', 'GK axe ', 'GK stave', 'Termina', 'Primari', 'GK term', 'Dreadno',
             'Morkn f', 'Morkn 9', 'Morkn 4', 'Guillman', 'papasmrf', 'rowboat', 'errant f', 'errant 12', 'errant 6', 'paladin')
    print('\t\t\t', '\t   '.join(names))
    for i in range(len(minis)):
        r = []
        rs = []
        for j in minis:
            rs.append(str('%7.2f' % round(j.wounds / minis[i].attack_rolls(j), ndigits=1)))
            r.append(j.wounds / minis[i].attack_rolls(j))
        # print(names[i], '\t', '\t\t'.join(rs), '\t', str(1350 * len(r) / sum(r)))
        print(names[i], '\t', str(32 / sqrt(r[3])))
