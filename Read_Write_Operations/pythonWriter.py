with open('demo.txt', 'r') as reader:
    list = []
    for line in reader.readlines():
        list.append(line)

#print(list)
with open('demo1.txt', 'w') as writer:
    for i in range(len(list)-1, -1, -1):
        writer.write(list[i]+"\n")