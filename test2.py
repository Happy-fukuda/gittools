#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import pexpect as pex
import subprocess
from getpass import getpass
def rungit(cmd:str):
    git_username=input("git username:")
    git_password=getpass("git password:")
    user_pattern="test+"
    pass_pattern="Password for 'https://df@github.com':"
    expect_list=[user_pattern,pass_pattern,pass_pattern,pex.EOF]
    git_cmd = pex.spawn(cmd)

    e_num=git_cmd.expect(expect_list)
    print(e_num)
    if e_num==0:
        git_cmd.sendline(git_username)
    if e_num==1:
        git_cmd.sendline(git_password)
    if e_num==2:
        pass
    else:
        print("error")



rungit("cat")
'''
#!/usr/bin/env python
import pexpect

p = pexpect.spawn("/bin/cat")

p.send("123456789\n")

p.expect(r"(345)..(.)")  # match against terminal echo
print ("Match1: " + p.before.decode() + '"' + p.after.decode() + '"')
print (p.match.groups())

p.expect(r"(345)..(.)")  # match against cat's output
print ("Match2: " + p.before.decode() + '"' + p.after.decode() + '"')
print (p.match.groups())

p.expect(r".*")   # match with the remaining string
print ("Match3: " + p.before.decode() + '"' + p.after.decode() + '"')

p.terminate()
p.expect(pexpect.EOF)
