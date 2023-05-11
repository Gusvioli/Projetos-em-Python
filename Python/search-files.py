# import os

# def file_search(name, path):
#     def files_path06(*args):
#         l = []
#         for item in args:
#             for p, _, files in os.walk(os.path.abspath(item)):
#                 l.append([p, files])
#         return l

#     def files_path():
#         arr = []
#         for verTxt in files_path06(path)[0][1]:
#             loc = path + verTxt
#             string1 = name
#             file1 = open(loc, "r", errors = 'ignore')
#             readfile = file1.read()
#             if string1 in readfile:
#                 arr.append(loc)
#             file1.close() 
#         return arr
    
#     return files_path()

# ChatGPT: Código acima foi melhorado com GPT-3
import os

def file_search(name, path):
    arr = []
    for filename in os.listdir(path):
        fullpath = os.path.join(path, filename)
        if os.path.isfile(fullpath) and name in open(fullpath, errors='ignore').read():
            arr.append(fullpath)
    return arr


print(file_search('Mission', './'))
