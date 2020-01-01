v 0.80

# Git

https://www.runoob.com/w3cnote/git-five-minutes-tutorial.html

https://git-scm.com/docs

https://www.runoob.com/git/git-tutorial.html

https://www.liaoxuefeng.com/wiki/896043488029600

```
git commit -a -m "Changed some files"
git push https://github.com/rfcpdq/Jupyter-Note
git config credential.helper store
```

## LF and CRLF
https://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important

```
git config core.autocrlf true
git config --global core.autocrlf true
```



# TODO

## Next step

- [x] Let's start with single csv data import, split the code first
- [x] Then config file
- [x] Then write one merge into one database code
  - [ ] Enhance merge Func to maintain (not rewrite) 
- [x] Spell checker
- [ ] Edit Func
- [ ] Searching Func
- [x] Separate load / sav function !!!
- [x] Flash card review
- [ ] 思考等价词咋搞（800词是词对），可能需要一个Add的功能




## Function

- [ ] 一个删除mistyping的code，将其加入缓存区
- [x] 将code分散在几个不同的python文件里，方便查找
- [x] 加一个批量复习，如rev6对应xxx部分的内容，自动识别
  - [x] 'rev_i' and then input numbers
  - [x] number of each cycle (100 / 120 for example) is in cfg file
- [x] 一个生词库(after merge)
- [ ] Add column function (忘记次数、词汇来源csv、遗忘曲线信息等)
- [ ] Color for can't remember words
- [ ] Auto fill in (win and linux are different)
- [ ] Random Greeting Function - pending
- [x] Requirement.txt


# The Project Goal

## Let's start with single csv data import

I have plenty csv files to edit: 大3000 / 800词 / 生词 etc.

When edit, I want to check whether the vocabulary exit in any signle database (the vocabulary may exist in many csv files => have order A.csv > B.csv) or not

And I will choose which one is the output (C.csv for example)


## Full database

One single data base, contain all vocabulary I need


## Review

直接看CSV给我一种想不起意思的感觉

libreoffice可以检查拼写错误（快速扫一眼，不当作复习来做），但是复习还是用code来复习快一些
