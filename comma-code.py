def commafy(list):
    length = len(list)
    commafied = ""
    for x in range(0, length):
        if x == length - 1:
            commafied = commafied + "and " + list[x]
            break
        commafied = commafied + list[x] + ", "
    return commafied

testList = ["frogs", "dogs", "logs"]

commad = commafy(testList)
print(commad)