# Memorize-GRE



## About this project

When memorizing the GRE vocabulary, I believe we (as a foreigner), should understand the vocabulary by their meanings first.

This project is a unfinished version. I write this to satisfy my personal need, and this repository may not get future update.

Have a good day!



What I want: 

- [x] Take personal notes on each vocabulary 

- [x] Each CSV file corresponds to a vocabulary book(in this repository we only have inputs/C.csv). Automatically fill in duplicate words when working on a new vocabulary book (inputs/B.csv). 

- [x] Review vocabulary on cell phone (Android) & desktop (Linux / Windows) 

- [x] Merge all CSV into one final file 

- [x] Simple spell check (python3 textblob, though... not accurate)



## Screenshot

Review on computer

<img src="./demo/02.png" alt="computer" />



Review on phone (Android Pydroid 3)

<img src="./demo/01.jpg" alt="phone" style="zoom:33%;" />



Typing with software (see /demo/03.mp4)

<img height=320 src="./demo/03.gif" />

## Usage

### Along side with third-party vocabulary software

Need abd

See screen coordinates in tools.py def adb_func(move), 

- my phone: one plus 7, 

- third-party vocabulary software: 
  - https://www.kmf.com/static/appcenter?website=gre
  - https://play.google.com/store/apps/details?id=com.enhance.google.greapp (older version)



### Function names and Config

**Still in progress**

See `main.py` and `phone_rev.py` for detailed information.

Input will be storage in `inputs/B.csv`. If the vocabulary you insert is in `inputs/C.csv`, it will automatically fill in (see /demo/03.mp4).



### Review (Computer)

Input `rev` will return last 10 words

Input `r-number` : `r-1`(for example) will return last 60 words (can be changed in function.py, def rev_custom(self, rev_prosition, block = 60))

Input `f-number` : `f-1`(for example) will return last 30 words in flash card (can be changed in function.py, def rev_custom(self, rev_prosition, block = 60))



### Review (Android Phone)

- Install git in `Termux`
- Run `phone_rev.py` (or other code) in `Pydroid3`