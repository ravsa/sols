import os
import datetime
import random
import glob
files = list()
for _file_name in glob.glob("*"):
    files.append(_file_name)
random.shuffle(files)
files = zip(files[::2], files[1::2])
start_date = 'sudo date +%Y%m%d -s "20161216"'
os.system(start_date)
for f1, f2 in files:
    delta = datetime.timedelta(days=1)
    date = str(datetime.datetime.now() + delta)
    cur_date = '"' + ''.join(date.split()[0].split('-')) + '"'
    setdate_cmd = 'sudo date +%Y%m%d -s ' + cur_date
    print setdate_cmd
    os.system(setdate_cmd)

    git_add = 'git add ' + f1
    if f1.endswith("py"):
        git_commit = 'git commit -am "python ' + f1 + '"'
    if f1.endswith("cpp"):
        git_commit = 'git commit -am "g++ ' + f1 + ' && ./.a.out"'
    if f1.endswith("c"):
        git_commit = 'git commit -am "gcc ' + f1 + ' && ./.a.out"'
    if f1.endswith("java"):
        git_commit = 'git commit -am "javac ' + \
            f1 + ' && java ' + f1.split('.')[0] + '"'
    print git_add
    os.system(git_add)
    print git_commit
    os.system(git_commit)

    git_add = 'git add ' + f2
    if f2.endswith("py"):
        git_commit = 'git commit -am "python ' + f2 + '"'
    if f2.endswith("cpp"):
        git_commit = 'git commit -am "g++ ' + f2 + ' && ./.a.out"'
    if f2.endswith("c"):
        git_commit = 'git commit -am "gcc ' + f2 + ' && ./.a.out"'
    if f2.endswith("java"):
        git_commit = 'git commit -am "javac ' + \
            f2 + ' && java ' + f2.split('.')[0] + '"'
    print git_add
    os.system(git_add)
    print git_commit
    os.system(git_commit)
