file = open("./The.Notebook.2004.720p.BrRip.x264.YIFY.en.srt")
temp = file.read().split('\n')
data = list()
def list_of_lines():
    for line in temp:
        string = ''
        for char in line:
            if char.isspace() or char.isalpha() :
                string = ''.join([string, char.replace('\n',' ').replace('\r','')])
        data.append(string.strip())
    return data
sen = open('sen.txt','w')
for i in list_of_lines():
    sen.writelines(i+'\n')
sen.close()
