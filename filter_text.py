logFile = "poppy.txt"

with open(logFile) as f:
    content = f.readlines()

# you may also want to remove empty lines
content = [l.strip() for l in content if l.strip()]

# flag
nextLine = False

# list to save the lines
textList = []

for line in content:
    find_TC = line.find('Totales')

    if find_TC > 0:
        nextLine = not nextLine
    else:
        if nextLine:
            pass
        else:
            textList.append(line)

print('\n')
print('Text list ..')
print(textList)

j = 0

for i in range(j, len(textList)):
    if j < len(textList):
        #print("index = {}".format(i))
        #print("index = {}".format(j))
        print(textList[j], textList[j]) # Insert into the gird here instead of print
        j = j + 2
