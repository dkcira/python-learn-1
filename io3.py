filename = "output.txt"
print(f'reading file {filename}')
my_file = open(filename,"r")
print(my_file.read())
my_file.close()
