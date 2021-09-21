# Project 1

### This is an example project, used for demonstration purposes. 

I wrote this project because my kids have a toy that has a set of cipher codes. They wanted to code their own messages and decipher them, so I wrote this program to take a message and spit out an encoded message that they needed to decipher. 

To run this program, make sure that Python3 is installed and working. You can validate this by running in your command prompt on Windows or Linux:

```bash
python --version
```

If using Linux, you may need to specify Python3
```bash
python3 --version
```

Now, from the it3038c-scripts directory, run the program using Python

```bash
python project1/mc2code/encoder-ring.py
```

First, you'll be asked to select a key that is silver (s), red(r), black(b), or purple(p):
Then you'll enter your secret message.

Hello this is my secret message

Example Output: 
```bash
it3038c-scripts> python project1/mc2code/encoder-ring.py
Enter key ("'s' for silver, 'r' for red, 'b' for black, 'p' for purple ")
s
Enter secret message (letters and spaces only, please)
Hello this is my secret message
SVOOL GSRH RH NB HVXIVG NVHHZTV
```
Now send this message to a friend and have them [use the decoder sheet here to decipher](https://ajbotheweb.s3.us-east-2.amazonaws.com/projects/mc2code/keycode.jpg) your secret message!

