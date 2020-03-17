
def max_length():
    file = open("names.txt","r")
    print(max(file.read().split("\n")))



def min_length():
    file = open("names.txt","r")
    arr = file.read().split("\n")
    minimum = min(arr,key=len)
    print(*[min for min in arr if len(min) == len(minimum)],sep="\n")

def sum_words():
    file = open("names.txt","r")
    file2 = open("name_length.txt", "w")
    file2.write("\n".join([str(len(word)) for word in file.read().split("\n")]))


def new_file_lengs():
    file = open("names.txt", "r")
    print(sum([len(word) for word in file.read().split("\n")]))

def name_users_length():
    file = open("names.txt", "r")
    select_len = int(input("Enter name length: "))
    print("\n".join([w for w in file.read().split("\n") if len(w)== select_len]))

max_length()
min_length()
sum_words()
name_users_length()