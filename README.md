# typomorise
Terminal-based typing game for memorize Japanese vocabularies 

![usage](https://user-images.githubusercontent.com/16998540/158050929-4c6f59da-62cc-45ec-aae7-7b1a3cee15cc.gif)

# Installation
### Requirement
- Python3.8 or later
- [Curses](https://docs.python.org/3/howto/curses.html)


### Download

Clone form repo
```sh
git clone https://github.com/trangtops/typomorise.git
```
### Run a program

```sh
cd typomorise
python3 main.py
```
### Option
`-f [input_file]`  
Specify the vocabulary file. Default value is vocab.csv. Note that the file must be csv format seperate with tab

`-c`
Save a progress to vocab_checkpoint.csv when user exit program with ctrl+c. 

`-r`
Each word that user finished typing will be put back to the end of vocab list

### How to play
- Interface will consist of 2 windows. The upper window is for typing input, and below one shows list of vocabularies.
- The first row of vocabulary list is the word you have to typing.
- After finished typing, press enter to pop out the first row. Then the second row will move up.
- one row of vocabulary is consisted of 3 words. The first one is a kanji, second is a reading in hiragana, and third is a meaning in english.
- After you finished typing each word, press TAB to move to the next word
- In kanji and hiragana word,for each character you're typing, a program will automatically convert from english to hiragana.
- For kanji part, you have to typing hiragana to match the reading. If you typing correctly, it will converted to kanji when you press TAB

![type_correct](https://user-images.githubusercontent.com/16998540/158052179-b0fa97d6-e373-499b-9e90-a3c4402ecc57.gif)

- You can press backspace to delete a character and go back to previous word. Alternatively, you can press ctrl+w or ctrl+backspace to delete a whole word


![type_wrong](https://user-images.githubusercontent.com/16998540/158052257-3ba148aa-fae2-4e25-805c-7c62e335ba2c.gif)




