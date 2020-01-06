# Memorize-GRE



## About this project

When memorizing the GRE vocabulary, I believe we (as a foreigner), should understand the vocabulary by their meanings first.

This project is a unfinished version. I write this to satisfy my personal need, and this repository may not get future update.

Have a good day!



What I want: 

- [x] Take personal notes on each vocabulary
- [x] Each CSV file corresponds to a vocabulary book. Automatically fill in duplicate words when working on a new vocabulary book (inputs/B.csv). 
- [x] Merge all CSV into one final file, remove duplicate, keep notation up-to-date.
	- In this repository demo we have (you can change file name in cfg): 
			B.csv, as the vocabulary book I am reading
			C.csv, as the finished book
			A.csv, as the merged CSV of B and C in which every word occur once
- [x] Review vocabulary on cell phone (Android) & desktop (Linux / Windows) 
- [x] Switch between different config files
- [x] Simple spell check (python3 textblob, though... not accurate)



## Screenshot

Review on computer

<img src="./demo/02.png" alt="computer" />



Review on phone (Android Pydroid 3)

<img src="./demo/01.jpg" alt="phone" width="35%" />



Typing with software (see /demo/03.mp4)

<img height=320 src="./demo/03.gif" />

## Usage

### Switch between different config files

- Write you own config file
- Run main.py, it will let you choose config file (last choose will be storage in `config_main.cfg`)



### Along side with third-party vocabulary software

Need abd

You can modify Android screen coordinates in `tools.py` `adb_func(move)`

- my phone: one plus 7

- third-party vocabulary software in demo: 
  - https://www.kmf.com/static/appcenter?website=gre
  - https://play.google.com/store/apps/details?id=com.enhance.google.greapp (older version)



### Function names and Config explain

See `main.py` and `phone_rev.py` for detail information

Config example:
```
[data_utils]
col = list: ["word", "etymonline", "emeaning", "cmeaning"]  # your csv structure
# file used to check duplicate
default_name = str: All.csv  # if input a word occur in this csv, it will auto copy to your woking csv

[function]
out_name = str: Reading-GRE.csv  # the book you currently working on
use_adb = bool: False
# for back up func
back_i = int: 0
```



### Review (Computer)

- Input `rev` will return last 10 words, you can change block in `main.py`
- Input `r-number` : `r-1`(for example) will return last 60 words (can be changed in function.py, def rev_custom(self, rev_prosition, block = 60))
- Input `f-number` : `f-1`(for example) will return last 30 words in flash card (can be changed in function.py, def rev_custom(self, rev_prosition, block = 60))



### Review (Android Phone)

- Install git in `Termux`
- Run `phone_rev.py` (or other code) in `Pydroid3`
