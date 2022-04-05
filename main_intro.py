# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

outside_var=5 #global var

def test_function(x):
    outside_var=1 # when assigned another value than it has as global var, then another local var is created
    y= outside_var+1
    return y

def test_global(x):
    global outside_var
    outside_var=2
    y=outside_var+1
    return y

def add_substract_mult(number_1,number_2):
    return number_1+number_2, number_1-number_2, number_1*number_2

start_number=1
second_number=2

add_num, sub_num,mul_num=add_substract_mult(start_number,second_number) #return a tuple
only_add_num,*_=add_substract_mult(start_number,second_number) # *_ ='not interested for the rest"

#print(mul_num)
#print(only_add_num)

f= open("text.txt", "w")
f.write("Sofia\n")
f.write("Iason\n")
f.close
# if you open it again with w mode everything will be deleted:
# a from append
f= open("text.txt","a")
f.write("added line")
f.close()


f= open("text.txt","r") # read file,
# prnit(f.read()) takes too much space to read and print it
#file_content=f.read() # save it as a str var.
#print(file_content)
# Another way is:
#file_line=f.readline() # reads only one line
#print(file_line)
#file_line=f.readline() # reads the line where is left at
#print(file_line)
#f.seek(0)
#f.close()

# read all the lines:
for line in f:
    print(line,end=" ")
f.close()


# context manager: dont care to close the file at the end
with open("text.txt","r") as f:
    for line in f:
        print(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    #print(mul_num)
    #print(only_add_num)
    print(test_function(1))
    print (outside_var)
    print(test_global(1))
    print(outside_var)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
