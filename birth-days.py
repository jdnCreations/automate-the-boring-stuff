birthdays = {'Jordan': '21 Dec'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("I don't have the birthday information for " + name)
        print("What's their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday Database updated.")

print(birthdays.keys())
