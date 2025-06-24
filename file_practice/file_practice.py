import  csv


def q_2(name_file):
    text_file = ["Hello world\n",
                 "It’s the first exercise in I/O)\n",
                 "That mean it is number 1\n",
                 "Not 2\n",
                 "Not three\n",
                 "It is exciting\n",
                 "And i am all 4 it\n"]
    with open(name_file,"w") as file:
        file.writelines(text_file)

def q_3(name_file):
    with open(name_file,"r") as f:
        data = f.readlines()
    for line in data:
        check = False
        for x in line:
            try:
                int(x)
                check = True
            except ValueError:
                pass
        if check:
            print(line)

def q_4(name_file):
    with open(name_file,"r") as file:
        data = file.readlines()
    count_line_odd = 0
    count_word = 0
    count_char = 0
    dict_char = {}
    for line in data:
        line = line.split()
        if not len(line) % 2:
            count_line_odd += 1
        for word in line:
            try:
                int(word)
            except ValueError:
                count_word += 1
                if word:
                    count_char += len(word)
                    for char in word:
                        if char in dict_char:
                            dict_char[char] += 1
                        else:
                            dict_char[char] = 1
    big_key = ""
    big_value = 0
    for key,value in dict_char.items():
        if value > big_value:
            big_key = key
            big_value = value
    print(dict_char)
    print(f"the count of lines is: {count_line_odd}")
    print(f"the count of words is: {count_word}")
    print(f"the count of char is: {count_char}")
    print(f"the char of show Most is: {big_key}, is show {big_value}")

def q_5(name_file):
    with open(name_file,"r") as file:
        data = file.readlines()
    data = [line[:-1]  + f" ({(len(line.split()))} word)\n"  for line in data]
    with open("summary.txt", "w") as file:
        file.writelines(data)

def q_7(name_file_csv):
    with open(name_file_csv,"r") as f:
        data = csv.DictReader(f)
        for person in data:
            if person["Gender"] == "male":
                print(f"קוראים לי:{person["GivenName"]}. אני גר ב: {person["City"]}. ועובד ב:{person["Occupation"]}")
            else:
                print(f"קוראים לי:{person["GivenName"]}. אני גרה ב: {person["City"]}. ועובדת ב:{person["Occupation"]}")

def q_8(name_file_csv):
    GivenName = "yossi"
    Gender = "male"
    Title = "Mr"
    Occupation = "Speech writer"
    City = "Netanya"
    new_row = [GivenName,Gender,Title,Occupation,City]
    with open(name_file_csv,"a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_row)

def q_9(name_file_csv):
    dict_data = {}
    with open(name_file_csv,"r") as f:
        data = csv.DictReader(f)
        for person in data:
            if person["City"] in dict_data:
                if person["Title"] in dict_data[person["City"]]:
                    dict_data[person["City"]][person["Title"]] += 1
                else:
                    dict_data[person["City"]][person["Title"]] = 1
            else:
                dict_data[person["City"]] = {person["Title"]: 1}
    with open("city_summary.csv", "w", newline="") as f:
        fieldnames = ["City", "Title", "Count"]
        writer = csv.DictWriter(f, fieldnames= fieldnames)
        writer.writeheader()
        for name,dict in dict_data.items():
            for key,value in dict.items():
                writer.writerow({"City":name,"Title":key,"Count":value})



name_file = "my_text.txt"
name_file_csv = "sample_names.csv"
# q_2(name_file)
# q_3(name_file)
# q_4(name_file)
# q_5(name_file)
# q_7(name_file_csv)
# q_8(name_file_csv)
q_9(name_file_csv)