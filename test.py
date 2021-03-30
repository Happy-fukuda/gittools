#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,os,sys
def get_args():
    # 準備
    parser = argparse.ArgumentParser()

    #parser.add_argument("pkg",type=str,help="all or you want to run pkg")
    parser.add_argument("-p","--pull", help="Run 'git pull'",nargs='*')
    ''''
    parser.add_argument("",)
    parser.add_argument("--alert", help="optional", action="store_true")
    '''
    # 結果を受ける
    args = parser.parse_args()

    return(args)

def main():
    args = get_args()
    if args.pull:
        print(' '.join(args.pull))

    else:
        print("none")


if __name__ == '__main__':
    main()
