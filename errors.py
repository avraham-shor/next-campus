

def read_file(file_name):
    output = "__CONTENT_START__\n"
    try:
        file = open(f"{file_name}","r")
        content_file = file.read()+"\n"
    except FileNotFoundError:
        output += "__NO_SUCH_FILE__\n"
    else:
        output += content_file
    finally:
        output += "__CONTENT_END__"
        return output



print(read_file("one_lined_file.txt"))
print(read_file("file_does_not_exist.txt"))








# def stop_error():
#     print("IndentationError")
#     # print("ngfnfn"
#         # print("IndentationError")
#
#     # for i,d in enumerate(dict):
#     #     print(dict.__next__)
#
#
#
# stop_error()