# PythonProjects


Word_Order_Frequency_One_Book (Book, Word_Order, File_Output)
Word_Order_Frequency_Two_Books (Book_1, Book_2, Word_Order, File_Output)

Book, Book_1 and Book_2: Contains the name of text file(s) that your book(s) is/are
stored in. It should be in the same directory as your program. Your function should
handle exceptions and errors related to this input if it is incorrect.

Word_Order: The number of words that will be ordered and analyzed by your function.
It must be a positive integer and you should consider only 1 (a single word) and 2
(adjacent two words). If it is given as 1, it will output single word frequency of the book
in contrast to a specific ordered sequence of word frequency.

File_Output: The name of the text file the results of this program will be saved. If the
file does not exist, you should create it and if it exists, should you override the previous
contents. It must be a string that contains a file name. Your program should not output
any results to the console, only to the file identified with this variable.

The basic algorithm of these functions are given below.
Firstly, read the given file or files.
Tokenize the words (separate them according to empty spaces)
Remove the stop words
(You can use the given file “stop_words_english.txt” for this purpose)
Remove punctuation symbols and other incorrect elements.
(You can use this site https://www.ascii-code.com/, Do not consider other punctuation
marks that are not an element of ASCII or Extended ASCII character groups)
Generate word order sequences and calculate their frequency.
Print out the results to the given text file.

The main difference between these functions are in word sequence frequency calculation
and result print out stage. For “Word_Order_Frequency_One_Book” function, the output
should look like the following.

| WORD      | WORD     |
| ORDER     | ORDER    |
| FREQUENCY | SEQUENCE |
------------------------
 <freq_bk_1>|<word_list>
 
For “Word_Order_Frequency_Two_Books” function, the output should look like the
following.
| TOTAL     | BOOK 1    | BOOK 2    | WORD     |
| ORDER     | ORDER     | ORDER     | ORDER    |
| FREQUENCY | FREQUENCY | FREQUENCY | SEQUENCE |
------------------------------------------------
<freq_total>|<freq_bk_1>|<freq_bk_2>|<word_list>

<freq_total>, <freq_bk_1> and <freq_bk_2>: The frequency values of word order
sequences.. You should order them correctly from right to left as numbers. You should
also increase the width of columns if the numbers are larger than given default size.
<word_list>: The list of words the represents the word order sequence. You should print
out the word order as a single string (e.g. “Project Gutenberg”).





