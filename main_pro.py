#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,os,sys
import pexpect as pex
from getpass import getpass
current_directory=os.path.expanduser("~/catkin_ws/gittools")

#引数設定
def get_args():
    # 準備
    parser = argparse.ArgumentParser()
    #parser.add_argument("pkg",type=str,help="all or you want to run pkg"
    parser.add_argument("-p","--pull", help="Run 'git pull'. --pull {all or want pkg}",nargs='*')
    parser.add_argument("-s","--push", help="Run 'git push'. --push {all or want pkg}",nargs='*')
    # 結果を受ける
    args = parser.parse_args()

    return(args)

def rungit(cmd):
    git_username=input("git username:")
    git_password=getpass("git password:")
    user_pattern="Username .*"
    pass_pattern="Password .*"
    branch_select="which branch or make branch:"
    commit_name="commit name:"
    expect_list=[user_pattern,pass_pattern,branch_select,commit_name,
                pex.EOF]
    git_cmd = pex.spawn(cmd)
    git_cmd.logfile_read=sys.stdout.buffer

    if git_cmd.isalive():
        while 1:
            e_num=git_cmd.expect(expect_list)
            if e_num==0:
                git_cmd.sendline(git_username)
                #print(expect_list[e_num]+"******入力しました")
            elif e_num==1:
                git_cmd.sendline(git_password)
                #print(expect_list[e_num]+"******入力しました")
            elif e_num==2:
                branch_name=input()
                git_cmd.sendline(branch_name)
            if e_num==3:
                commit=input()
                git_cmd.sendline(commit)
            if e_num==len(expect_list)-1:
                break

    else:
        print("not alive")
    git_cmd.close()



def main():
    args = get_args()
    if args.pull:
        git_arg="python3 "+current_directory +"/git_tools.py " + "--pull " + ' '.join(args.pull)
        print(git_arg)
        rungit(git_arg)
    if args.push:
        git_arg="python3 "+current_directory +"/git_tools.py " + "--push " + ' '.join(args.push)
        rungit(git_arg)

if __name__ == '__main__':
    main()
