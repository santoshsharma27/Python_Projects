file = open("test.txt")
# Read all the contents in the file
# print(file.read())
# print(file.read(5))

# print(file.readline())
# print(file.readline())


# Print Line By Line using readline method
# line =  file.readline()
# while line!= "":
#    print(line)
#   line = file.readline()


values = ["ant", "boy", "cat", "dog", "egg"]
for line in file.readline():
    print(line)

file.close()
