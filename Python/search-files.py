import os

def files_path06(*args):
    l = []
    for item in args:
        for p, _, files in os.walk(os.path.abspath(item)):
            l.append([p, files])
    return l


pegaArr = files_path06('./TXTs/')[0][1]
arr = []
for verTxt in pegaArr:
    loc = './TXTs/' + verTxt
    string1 = 'gustavovieiradeoliveira@gmail.com'
    file1 = open(loc, "r", errors = 'ignore')
    readfile = file1.read()
    if string1 in readfile:
        arr.append(loc)
    file1.close() 
print(arr)