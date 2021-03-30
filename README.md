# gittools
チームでの開発では日々誰かが新しいmaster branchを更新している。しかし、それらのパッケージは数が多くなり、更新(pull)することなどが手間になる。このパッケージはそれらを楽にする機能を提供する。(現状ではcatkin_ws/src上のパッケージのみ対応)

## How to use
~/catkin_ws上にこのパッケージを配置
### git pull
```
python3 main_pro.py -p [--pull] all
```
allは自分のpullしたいパッケージを空白区切りで書くことも可

## other option
### if you want to see log
```
python3 main_pro.py -l [--log] -p all
```
エラーやログを見たいときはオプションで-l(--log)を機能オプション(-p)の前につける

### if you want to see help
```
python3 main_pro.py -h [--help]
```
