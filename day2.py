def count_valid_passwords(passwords):
    valid = 0
    password_list = passwords.split('\n')
    for password in password_list:
        if password == '':
            continue
        elif is_valid(password):
            valid += 1
    return valid

def parse_password(input):
    return input.split(": ")[1]

def parse_rule(input):
    raw_rule = input.split(": ")[0]
    letter = raw_rule.split(" ")[1]
    min_max = raw_rule.split(" ")[0].split("-")
    return {"letter": letter, "min": min_max[0], "max": min_max[1]}

def count_letter(input, letter):
    return input.count(letter)

def is_valid(input):
    password = parse_password(input)
    rule = parse_rule(input)
    count = count_letter(password, rule.get('letter'))
    if count >= int(rule.get('min')) and count <= int(rule.get('max')):
        return True
    else:
        return False

def letter_in_first_position(password, rule):
    try:
        if password[int(rule.get('min'))] == rule.get('letter'):
            return True
    except:
        return False

def letter_in_last_position(password, rule):
    try:
        if password[int(rule.get('max'))] == rule.get('letter'):
            return True
    except:
        return False

def new_is_valid(input):
    password = parse_password(input)
    rule = parse_rule(input)
    if letter_in_first_position(password, rule) and letter_in_last_position(password, rule):
        return False
    elif letter_in_first_position(password, rule) or letter_in_last_position(password, rule):
        return True

def count_valid_passwords(passwords):
    valid = 0
    password_list = passwords.split('\n')
    for password in password_list:
        if password == '':
            continue
        elif is_valid(password):
            valid += 1
    return valid

def new_count_valid_passwords(passwords):
    valid = 0
    password_list = passwords.split('\n')
    for password in password_list:
        if password == '':
            continue
        elif new_is_valid(password):
            valid += 1
    return valid
