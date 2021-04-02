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
        if len(pkg_ls)==0 or ("all" not in pkg_ls and  set(pkg_ls)-set(dirs_list)):
            print("not find pkg")
            return 0
        try:
            for dir in dirs_list:
                if dir in pkg_ls or "all" in pkg_ls:
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
        except Exception as e:
            print(e)


    def gitpush(self,pkg_ls=[]):
        if len(pkg_ls)==0 or ("all" not in pkg_ls and  set(pkg_ls)-set(dirs_list)):
            print("not find pkg")
            return 0
        try:
            for dir in dirs_list:
                if len(pkg_ls)==0 or dir in pkg_ls or "all" in pkg_ls:
                    print("git push:"+dir)
                    pass
                else:
                    continue
                dir_path=current_directory+"/"+dir
                os.chdir(dir_path)
                repo=git.Repo()
                print(repo.git.branch())
                branch_name=input("which branch or make branch:")
                if branch_name not in repo.git.branch():
                    repo.git.branch(branch_name)
                repo.git.checkout(branch_name)
                commit_name="'"+input("commit name:")+"'"
                repo.git.add('.')
                print("add all")
                repo.git.commit('-m',commit_name)
                print("commit")
                try:
                    repo.remotes.origin.push('HEAD')
                    print("finish push")
                except Exception as e:
                    print(e)
                    repo.git.reset('--soft','HEAD~')
                    print("reset --soft")


        except Exception as e:
            print(e)




def main():
    args = main_pro.get_args()
    git_tool=GitTools()
    if args.pull:
        git_tool.gitpull(pkg_ls=args.pull)
    if args.push:
        git_tool.gitpush(pkg_ls=args.push)

if __name__=='__main__':
    print("git tools")
    main()
