class Model:
    def __init__(self, name, movement, to_hit, to_shoot, strength, toughness, wounds, attacks, ld, save, special_save,
                 points, weapons):
        self.name = name
        self.movement = movement
        self.to_shoot = to_shoot
        self.strength = strength
        self.toughness = toughness
        self.attacks = attacks
        self.wounds = wounds
        self.ld = ld
        self.save = (save - 1)
        self.special_save = (special_save - 1)
        self.points = points
        melee = False
        ranged = False
        self.re_roll_to_hit_all = False
        self.re_roll_to_hit_1s = False
        self.re_roll_to_wound_all = False
        self.re_roll_to_wound_1s = False
        self.weapons = weapons
        for weapon in weapons:
            if weapon.__class__ is Weapon and weapon.type == 'Melee':
                self.melee = weapon
                if weapon.strength == 'User':
                    self.strength = strength
                elif weapon.strength[0] == '+' or weapon.strength[0] == '-':
                    self.strength = strength + int(weapon.strength)
                else:
                    self.strength = strength * int(weapon.strength[1:])

                self.to_hit = (7 - to_hit + weapon.hit_mod) / 6

                self.attacks += weapon.attacks

                melee = True
            elif weapon.__class__ is Weapon:
                self.ranged = weapon
                ranged = True
            else:
                mod = 0
                if weapon.amount[0] == '+' or weapon.amount[0] == '-':
                    mod = int(weapon.amount[1:])
                if weapon.attribute == 'A':
                    self.attacks += mod
                if weapon.attribute == 'to_hit':
                    if weapon.amount == 'rr1':
                        self.re_roll_to_hit_1s = True
                    elif weapon.amount == 'rr':
                        self.re_roll_to_hit_all = True
                if weapon.attribute == 'to_wound':
                    if weapon.amount == 'rr1':
                        self.re_roll_to_wound_1s = True
                    elif weapon.amount == 'rr':
                        self.re_roll_to_wound_all = True
                if weapon.attribute == 'special_save':
                    if weapon.amount == '+1':
                        special_save = min(special_save - 1, 5)
                        self.special_save = (special_save - 1)

        if not melee:
            self.melee = None
        if not ranged:
            self.ranged = None

    def get_points(self):
        points = self.points
        if self.ranged is not None:
            points += self.ranged.points
        if self.melee is not None:
            points += self.melee.points
        return points

    def wound_roll(self, other):

        if self.strength == other.toughness:
            roll = 3 / 6
        elif self.strength >= other.toughness * 2:
            roll = 5 / 6
        elif self.strength > other.toughness:
            roll = 4 / 6
        elif self.strength <= other.toughness / 2:
            roll = 1 / 6
        else:
            roll = 2 / 6
        roll = min(1, roll + self.melee.wound_mod)
        if self.re_roll_to_wound_all:
            return roll + ((1 - roll) * roll)
        if self.re_roll_to_wound_1s:
            return roll + ((1 / 6) * roll)
        return roll

    def wound_roll_ranged(self, other):
        strength = int(self.ranged.strength)
        if strength == other.toughness:
            roll = 3 / 6
        elif strength >= other.toughness * 2:
            roll = 5 / 6
        elif strength > other.toughness:
            roll = 4 / 6
        elif strength <= other.toughness / 2:
            roll = 1 / 6
        else:
            roll = 2 / 6

        return min(1, roll + self.ranged.wound_mod)

    def hit_roll(self):
        if self.re_roll_to_hit_all:
            return self.to_hit + ((1 - self.to_hit) * self.to_hit)
        if self.re_roll_to_hit_1s:
            return self.to_hit + ((1 / 6) * self.to_hit)
        return self.to_hit

    def shoot_roll(self, moved):

        if self.ranged.auto:
            return 1
        else:
            if self.ranged.type == 'Heavy' and moved:
                return max(0, ((7 - self.to_shoot) / 6) - (1 / 6))
            else:
                return max(0, (7 - self.to_shoot) / 6)

    def save_roll(self, ap):
        return max(1 / 6, min(1, (min(self.special_save, (self.save - ap))) / 6))

    def shoot_rolls(self, other, range, moved=False):
        if range > self.ranged.range:
            return 0
        if self.ranged is None:
            return 0
        else:
            ap = self.ranged.ap
            damage = self.ranged.damage
            attacks = self.ranged.attacks
            if self.ranged.type == 'Rapid Fire' and range < self.ranged.range / 2:
                attacks *= 2
        wounds = attacks * self.shoot_roll(moved) * self.wound_roll_ranged(other) * other.save_roll(ap)
        # if self.ranged.name == 'Psycannon':
        #     print(attacks, self.shoot_roll(moved), self.wound_roll_ranged(other), other.save_roll(ap), wounds)
        if other.wounds == 1:
            return wounds
        else:
            return wounds * damage

    def attack_rolls(self, other):
        if self.melee is None:
            ap = 0
            damage = 1
        else:
            ap = self.melee.ap
            damage = self.melee.damage
        special_rule = False
        for buff in self.weapons:
            if buff.name.count('Master Swordsman') != 0:
                special_rule = True
                wounds_rolled = self.attacks * self.hit_roll() * self.wound_roll(other)
                wounds_added = wounds_rolled * self.hit_roll() * self.wound_roll(other)
                wounds = (wounds_rolled + wounds_added) * other.save_roll(ap)
                break

        if not special_rule:
            wounds = self.attacks * self.hit_roll() * self.wound_roll(other) * other.save_roll(ap)

        if other.wounds == 1:
            return wounds
        else:
            return wounds * damage

    def __str__(self):
        s = self.name + '\n'
        s += ', '.join(
            [str(self.movement), str(self.to_hit), str(self.to_shoot), str(self.strength), str(self.toughness),
             str(self.wounds), str(self.attacks), str(self.ld), str(self.save), str(self.special_save)]) + '\n'
        if self.melee is not None:
            s += str(self.melee) + '\n'
        if self.ranged is not None:
            s += str(self.ranged) + '\n'
        s += str(self.get_points()) + ' points'
        return s

    def get_short_descriptor(self):
        s = self.name + ': '
        if self.melee is not None:
            s += self.melee.name + ', '
        if self.ranged is not None:
            s += self.ranged.name + '. '
        s += str(self.get_points()) + ' points.'
        return s


class Buff:
    def __init__(self, name, attribute, amount):
        self.name = name
        self.attribute = attribute
        self.amount = amount


class Weapon:
    def __init__(self, name, range, type, strength, ap, damage, hit_mod, wound_mod, points):
        self.name = name
        if range != 'Melee':
            self.range = int(range)
        else:
            self.range = range
        self.auto = type.split(' ')[0] == 'Auto'
        if self.auto:
            self.type = ' '.join(type.split(' ')[1:-1])
        else:
            self.type = ' '.join(type.split(' ')[:-1])

        attacks = type.split(' ')[-1]
        if attacks == 'D3':
            self.attacks = 2
        elif attacks == 'D6':
            self.attacks = 3.5
        elif attacks == '2D6':
            self.attacks = 7
        elif range == 'Melee':
            self.attacks = int(attacks) - 1
        else:
            self.attacks = int(attacks)

        self.strength = strength
        self.ap = float(ap)

        if damage == 'D3':
            self.damage = 2
        elif damage == 'D6':
            self.damage = 3.5
        elif damage == 'D6(3)':
            self.damage = 4
        else:
            self.damage = float(damage)
        self.hit_mod = int(hit_mod)

        if wound_mod[0] == '+' or wound_mod[0] == '-':
            self.wound_mod = 1 / int(wound_mod)
        else:
            self.wound_mod = 0
        self.points = int(points)

    def __str__(self):
        return ', '.join(
            [self.name, self.range, self.type, str(self.attacks), self.strength, str(self.ap), str(self.damage),
             str(self.points)])
        # return self.range
