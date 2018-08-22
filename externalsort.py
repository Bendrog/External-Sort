
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
#                       3/ ok
#                       4/ ok

'''

new poste
revoir toute la partie marketing
faire des macros

tt en python
stage + data viz + automatisation des extractions de données

projets + 

fiche de route, force de proposition  mais surtout un pôle suport

'''
import os

shunk = ''
file_num = 0
temp_files = []
write_file = None
FileIsEmpty = False
my_list = []
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# STEP 1: SPLITING
with open('data.txt') as f:
    shunk = f.read(512)
    while len(shunk) > 0:
        file_name = 'split{0}.txt'.format(file_num)
        temp_files.append(file_name)
        write_file = open(file_name, 'w')
        write_file.write(shunk)
        write_file.close()
        shunk = f.read(512)
        file_num += 1
        print(file_num)

print("we're done spliting, let's sort'em all !!")
print("====================================================================================================================================================================================")
print("----------------------------------------------          THIS PART IS THE SORTING PART          -------------------------------------------------------------------------------------")
print("====================================================================================================================================================================================")


# STEP 2: SORTING
for k in range(0, len(temp_files)):
    with open('split{}.txt'.format(k), 'r+') as f:
        char = f.read(1)
        my_list = []
        while len(char) > 0:
            my_list.append(char)
            char = f.read(1)
        my_list.sort()
        list_size = len(my_list) - 1
        print(my_list)
        for k in range(0,list_size+1):
            f.seek(k)
            lettre = my_list[k]
            f.write(lettre)

print("====================================================================================================================================================================================")
print("----------------------------------------------          THIS PART IS THE MERGING PART          -------------------------------------------------------------------------------------")
print("====================================================================================================================================================================================")


# STEP 3 & 4: MERGING

while len(temp_files)>1:
	# If the spliting files are pair
	merged_files = []
	if len(temp_files)%2 == 0:

		for k in range(int(len(temp_files)/2)):
			# Opening the 2 fiels to lerge 
			# + creating the output file
			file1 = open(temp_files[2*k], 'r')
			file2 = open(temp_files[2*k+1], 'r')
			file_name = 'merged{}.txt'.format(k)
			merged_files.append(file_name)
			output = open(file_name, 'w')
			seeker = 0
			list1 = []
			list2 = []

	        #Turn file1 into a list
			char1 = file1.read(1)
			while len(char1) > 0:
			    list1.append(char1)
			    char1 = file1.read(1)
			#Turn file2 into a list
			char2 = file2.read(1)
			while len(char2) > 0:
			    list2.append(char2)
			    char2 = file2.read(1)

			for k in range (len(alphabet)):
				char = alphabet[k]
				var1 = list1.count(char)
				var2 = list2.count(char)
				if var2!=0:
					for m in range(var2):
						list1.insert(seeker, char)
				seeker += var1 + var2
			# print (list1)
			print (len(list1))
			for p in range(0,len(list1)):
				output.seek(p)
				lettre = list1[p]
				output.write(lettre)
			file1.close()
			file2.close()
			output.close()
		for i in range (len(temp_files)):
			os.remove('split{}.txt'.format(i))

		#If the splitting files are not pair
	else:
		for k in range(int(len(temp_files)/2)):
			# Opening the 2 fiels to lerge 
			# + creating the output file
			file1 = open(temp_files[2*k], 'r')
			file2 = open(temp_files[2*k+1], 'r')
			file_name = 'merged{}.txt'.format(k)
			merged_files.append(file_name)
			output = open(file_name, 'w')
			seeker = 0
			list1 = []
			list2 = []

	        #Turn file1 into a list
			char1 = file1.read(1)
			while len(char1) > 0:
			    list1.append(char1)
			    char1 = file1.read(1)
			#Turn file2 into a list
			char2 = file2.read(1)
			while len(char2) > 0:
			    list2.append(char2)
			    char2 = file2.read(1)

			for k in range (len(alphabet)):
				char = alphabet[k]
				var1 = list1.count(char)
				var2 = list2.count(char)
				if var2!=0:
					for m in range(var2):
						list1.insert(seeker, char)
				seeker += var1 + var2
			# print (list1)
			print (len(list1))
			for p in range(0,len(list1)):
				output.seek(p)
				lettre = list1[p]
				output.write(lettre)
			file1.close()
			file2.close()
			output.close()
		print(len(merged_files))
		os.rename(temp_files[-1], 'merged{}.txt'.format(len(merged_files)))
		merged_files.append('merged{}.txt'.format(len(merged_files)))
		for i in range (len(temp_files)-1):
			os.remove('split{}.txt'.format(i))
	temp_files = merged_files[:]
	print(temp_files)
	if len(temp_files)<2:
		break

	merged_files = []

	if len(temp_files)%2 == 0:

		for k in range(int(len(temp_files)/2)):
			# Opening the 2 fiels to lerge 
			# + creating the output file
			file1 = open(temp_files[2*k], 'r')
			file2 = open(temp_files[2*k+1], 'r')
			file_name = 'split{}.txt'.format(k)
			merged_files.append(file_name)
			output = open(file_name, 'w')
			seeker = 0
			list1 = []
			list2 = []

	        #Turn file1 into a list
			char1 = file1.read(1)
			while len(char1) > 0:
			    list1.append(char1)
			    char1 = file1.read(1)
			#Turn file2 into a list
			char2 = file2.read(1)
			while len(char2) > 0:
			    list2.append(char2)
			    char2 = file2.read(1)

			for k in range (len(alphabet)):
				char = alphabet[k]
				var1 = list1.count(char)
				var2 = list2.count(char)
				if var2!=0:
					for m in range(var2):
						list1.insert(seeker, char)
				seeker += var1 + var2
			# print (list1)
			print (len(list1))
			for p in range(0,len(list1)):
				output.seek(p)
				lettre = list1[p]
				output.write(lettre)
			file1.close()
			file2.close()
			output.close()
		for i in range (len(temp_files)):
			os.remove('merged{}.txt'.format(i))

		#If the splitting files are not pair
	else:
		for k in range(int((len(temp_files)/2))):
			# Opening the 2 fiels to lerge 
			# + creating the output file
			file1 = open(temp_files[2*k], 'r')
			file2 = open(temp_files[2*k+1], 'r')
			file_name = 'split{}.txt'.format(k)
			merged_files.append(file_name)
			print(merged_files)
			output = open(file_name, 'w')
			seeker = 0
			list1 = []
			list2 = []

	        #Turn file1 into a list
			char1 = file1.read(1)
			while len(char1) > 0:
			    list1.append(char1)
			    char1 = file1.read(1)
			#Turn file2 into a list
			char2 = file2.read(1)
			while len(char2) > 0:
			    list2.append(char2)
			    char2 = file2.read(1)

			for k in range (len(alphabet)):
				char = alphabet[k]
				var1 = list1.count(char)
				var2 = list2.count(char)
				if var2!=0:
					for m in range(var2):
						list1.insert(seeker, char)
				seeker += var1 + var2
			# print (list1)
			print (len(list1))
			for p in range(0,len(list1)):
				output.seek(p)
				lettre = list1[p]
				output.write(lettre)
			file1.close()
			file2.close()
			output.close()
		print (len(temp_files))
		print(temp_files[-1])
		print(len(merged_files))
		os.rename(temp_files[-1], 'split{}.txt'.format(len(merged_files)))
		merged_files.append('split{}.txt'.format(len(merged_files)))
		for i in range (len(temp_files)-1):
			os.remove('merged{}.txt'.format(i))
	temp_files = merged_files[:]
	print(temp_files)


if os.path.exists('split0.txt'):
	last_file = open('split0.txt', 'r')
	main_file = open('data.txt', 'w')
	char1 = last_file.read(1)
	while len(char1) > 0:
		main_file.write(char1)
		char1 = last_file.read(1)
	main_file.close()
	last_file.close()
	os.remove('split0.txt')
else:
	last_file = open('merged0.txt', 'r')
	main_file = open('data.txt', 'w')
	char1 = last_file.read(1)
	while len(char1) > 0:
		main_file.write(char1)
		char1 = last_file.read(1)
	main_file.close()
	last_file.close()
	os.remove('merged0.txt')




'''
for i in range (513):
    for j in range (513):
        if file2[i]>file1[j]:


If files2[char]

'''


