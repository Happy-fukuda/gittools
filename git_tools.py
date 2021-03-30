#!/usr/bin/env python
# -*- coding: utf-8 -*-

#==========================
'''
description:python3でcatkin_ws/src上のgithubのmasterブランチのみ更新する.
author:Happy-fukuda
'''
#==========================
import os,git
import subprocess as sup
import main_pro

current_directory=os.path.expanduser("~/catkin_ws/src")
dirs_list = [f for f in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, f))]

class GitTools():

    def gitpull(self,pkg_ls=[]):

        try:
            for dir in dirs_list:
                if len(pkg_ls)==0 or dir in pkg_ls or "all" in pkg_ls:
                    pass
                else:
                    continue
                dir_path=current_directory+"/"+dir
                os.chdir(dir_path)
                master_branch=sup.run(["git remote show origin | grep 'HEAD branch' | awk '{print $NF}'"],
                                    stdout=sup.PIPE,shell=True)
                branch_name=master_branch.stdout.decode().split()[0]

                print("path:"+dir_path)
                print("pull branch name:"+branch_name)
                repo=git.Repo()
                repo.remotes.origin.fetch()
                if branch_name not in repo.git.branch():
                    repo.git.branch(branch_name)
                repo.git.checkout(branch_name)
                repo.git.pull()
        except:
            print("pull failed")



def main():
    args = main_pro.get_args()
    git_tool=GitTools()
    if args.pull:
        git_tool.gitpull(pkg_ls=args.pull)
if __name__=='__main__':
    print("git tools")
    main()
