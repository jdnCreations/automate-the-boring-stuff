tableData = [['apples', 'oranges', 'cherries', 'banana'],              
             ['Alice', 'Bob', 'Carol', 'David'],              
             ['dogs', 'cats', 'moose', 'goose']]

maxWidths = []
biggest = ''

def printTable(tableData):
    colWidths = [0] * len(tableData)
    colWidths[0] = getLongestWord(tableData[0])
    colWidths[1] = getLongestWord(tableData[1])
    colWidths[2] = getLongestWord(tableData[2])

    for i in range(0, len(tableData[0])):
            print(tableData[0][i].rjust(colWidths[0]) + ' ' + 
                  tableData[1][i].rjust(colWidths[1]) + ' ' + 
                  tableData[2][i].rjust(colWidths[2]))

def getLongestWord(list):
    longestWord = 0
    for item in list:
        if int(len(item)) > longestWord:
            longestWord = len(item)
    return longestWord

printTable(tableData)



