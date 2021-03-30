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
    parser.add_argument("-l","--log", help="You can see log. if you use it,you must before other option",action="store_true")
    ''''
    parser.add_argument("",)
    parser.add_argument("--alert", help="optional", action="store_true")
    '''
    # 結果を受ける
    args = parser.parse_args()

    return(args)

def rungit(cmd,log):
    git_username=input("git username:")
    git_password=getpass("git password:")
    user_pattern="Username .*"
    pass_pattern="Password .*"
    error_pattern="pull failed"
    expect_list=[user_pattern,pass_pattern,pex.EOF,error_pattern]
    if log:
        git_cmd = pex.spawn(cmd,logfile=sys.stdout.buffer)
    else:
        git_cmd = pex.spawn(cmd)
    if git_cmd.isalive():
        while 1:
            e_num=git_cmd.expect(expect_list)
            if e_num==0:
                git_cmd.sendline(git_username)
                #print(expect_list[e_num]+"******入力しました")
            if e_num==1:
                git_cmd.sendline(git_password)
                #print(expect_list[e_num]+"******入力しました")
            if e_num==2:
                print("pull完了")
                break
            if e_num==3:
                print("pull失敗,usernameとpasswordを入力し直してみてください")
                break
    else:
        print("not alive")
    git_cmd.close()



def main():
    args = get_args()
    if args.pull:
        git_arg="python3 "+current_directory +"/git_tools.py " + "--pull " + ' '.join(args.pull)
        rungit(git_arg,args.log)


if __name__ == '__main__':
    main()
