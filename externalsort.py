
###    Let me introduce you to this External Sorting Algorthm    ###

####################################################################
############## Written by: Benoît Drogou          ##################
############## last update : 17/08/2018           ##################
############## mail: benoit.drogou@gmail.com      ##################
############## Github: https://github.com/Bendrog ##################
####################################################################

# What is it about ? => To sort a large file that would normally saturate your RAM
# We are here dealing with .txt file, not going to work for .csv

# How to do so ? => 1/ Dividing the large file into small ones
#                   2/ Sorting this files
#                   3/ Merge-Sort this file into a big one
#                   4/ Delete temporary files created in step 1

# How is it so far ? => 1/ ok
#                       2/ ok
#                       3/ To Do
#                       4/ To Do

shunk=''
file_num = 0
temp_files = []
write_file = None
FileIsEmpty = False
my_list = []

# STEP 1:
with open('data.txt') as f:
    shunk = f.read(513)
    while len(shunk) > 0:
        file_name = 'split{0}.txt'.format(file_num)
        temp_files.append(file_name)
        write_file = open(file_name, 'w')
        write_file.write(shunk)
        write_file.close()
        shunk = f.read(513)
        file_num += 1
        print(file_num)

print("we're done spliting, let's sort'em all !!")

# STEP 2:
for k in range(0, len(temp_files)):
    with open('split{}.txt'.format(k), 'r+') as f:
        char = f.read(1)
        my_list = []
        while len(char) > 0:
            my_list.append(char)
            char = f.read(1)
        list_size = len(my_list) - 1
        print('this is the size of the list {}'.format(list_size))
        change = True
        while change:
                change = False
                for index in range(list_size):
                    if my_list[index] > my_list[index + 1]:
                        print(index)
                        aux = my_list[index]
                        my_list[index] = my_list[index + 1]
                        my_list[index + 1] = aux
                        change = True
        print(my_list[:])
        for k in range(0,list_size+1):
            f.seek(k)
            lettre = my_list[k]
            f.write(lettre)

''' So far we have splited the main file into pices of 512 characters
... And we sorted each one of them
... It is missing the merging part '''
