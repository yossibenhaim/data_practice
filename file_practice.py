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

name_file = "my_text.txt"
q_2(name_file)
q_3(name_file)
