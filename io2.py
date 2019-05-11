
my_list = [i**2 for i in range(1,11)]

filename = "output.txt"
print(f'creating file {filename} to write {my_list}')
my_file = open("output.txt", "r+")
# Add your code below!
for i in my_list:
    my_file.write(str(i) + "\n")
my_file.close()
