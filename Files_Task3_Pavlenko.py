
files = {'f1':'1.txt','f2':'2.txt','f3':'3.txt'}
unsorted_files = {}
sorted_files = {}

for f in files:
    with open(files[f], 'r', encoding = 'utf-8') as f:
        unsorted_files[f.name] = len(f.readlines())



sorted_list=sorted(unsorted_files.values())

for sorted_value in sorted_list:
    for key, value in unsorted_files.items():
        if value==sorted_value:
            sorted_files[key]=value

for f in sorted_files:
    with open(f, 'r', encoding = 'utf-8') as current_file:
        with open ('result.txt', 'a', encoding = 'utf-8') as file_result:
            file_result.write(f+'\n')
            file_result.write(str(sorted_files[f])+'\n')
            file_result.write(current_file.read()+'\n')
