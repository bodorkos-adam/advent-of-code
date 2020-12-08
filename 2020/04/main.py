import re


with open('input.txt') as f:
    data = f.read()
    passports = [p.rstrip().replace('\n', ' ').split(' ') for p in data.split('\n\n')]


def p1():
    num_valid = 0
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    for p in passports:
        fields = {keyval[:3] for keyval in p}

        if required_fields.issubset(fields):
            num_valid += 1

    print(num_valid)


def p2():
    num_valid = 0

    for p in passports:
        fields = {keyval[:3]: keyval[4:] for keyval in p}

        byr = fields.get('byr')
        if not (byr and 1920 <= int(byr) <= 2002):
            continue

        iyr = fields.get('iyr')
        if not (iyr and 2010 <= int(iyr) <= 2020):
            continue

        eyr = fields.get('eyr')
        if not (eyr and 2020 <= int(eyr) <= 2030):
            continue

        hgt = fields.get('hgt')
        if hgt:
            hgt_unit = hgt[-2:]
            hgt_val = int(hgt[:-2])

            valid = {
                'cm': lambda val: 150 <= val <= 193,
                'in': lambda val: 59 <= val <= 76,
            }.get(hgt_unit, lambda val: False)(hgt_val)

            if not valid:
                continue
        else:
            continue

        hcl = fields.get('hcl')
        if not (hcl and re.match('^#[0-9a-f]{6}$', hcl)):
            continue

        ecl = fields.get('ecl')
        if not (ecl and ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
            continue

        pid = fields.get('pid')
        if not (pid and re.match('^[0-9]{9}$', pid)):
            continue

        num_valid += 1

    print(num_valid)


p1()
p2()
