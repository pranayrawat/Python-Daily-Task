def email_validator(l1):
    valid = []
    
    for i in l1:
        if i.count('@') == 1:
            if i[-4:] == '.com':
                if i[0] != '@':
                    valid.append(i)
        
    if len(valid) == 0:
        return "all emails are invalid"
    else:
        return valid
    
print(email_validator(['ben@mail.com','john@mail.cm','kenny@gmail.com','@list.com']))