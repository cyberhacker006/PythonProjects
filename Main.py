flag = True
stop_words = ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
        'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
        'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
        'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
        'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
        'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
        'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
        'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
        'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
        'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
        'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
        'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
        'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
        'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
        'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
        'consequently', 'consider', 'considering', 'contain', 'containing',
        'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
        'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
        'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
        'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
        'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
        'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
        'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
        'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
        'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
        'following', 'follows', 'for', 'forever', 'former', 'formerly',
        'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
        'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
        'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
        'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
        'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
        'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
        'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
        'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
        'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
        'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
        'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
        'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
        'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
        'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
        'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
        'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
        'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
        'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
        'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
        'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
        'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
        'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
        'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
        'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
        'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
        'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
        'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
        'overall', 'own', 'particular', 'particularly', 'past', 'per',
        'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
        'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
        'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
        'regardless', 'regards', 'relatively', 'respectively', 'right',
        'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
        'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
        'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
        'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
        'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
        'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
        'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
        'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
        'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
        'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
        'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
        'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
        'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
        'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
        'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
        'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
        'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
        'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
        'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
        'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
        'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
        'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
        'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
        'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
        'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
        'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
        'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
        'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
        'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
        'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
        'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'whens',
        'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
        'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
        'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
        'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
        'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
        'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
        'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
        'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
        'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
        'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
        'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
        'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
        'importance', 'important', 'index', 'information', 'invention', 'itd',
        'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
        'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
        'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
        'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
        'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
        'readily', 'ref', 'refs', 'related', 'research', 'resulted',
        'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
        'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
        'similar', 'similarly', 'slightly', 'somethan', 'specifically',
        'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
        'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
        'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
        'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
        'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
        'world', 'youd', 'youre']


def Word_Order_Frequency_One_Book(numberofwords, first_filename, output_filename):
      files = 1
      first_file(numberofwords, first_filename, files, output_filename)
      if numberofwords > 2:
          print("Please enter 1 single word or two. ")
          return
           
def Word_Order_Frequency_Two_Book(numberofwords, first_filename, second_filename, output_filename):
      files = 2
      first_file2(numberofwords, first_filename, second_filename, files, output_filename)
      if numberofwords > 2:
          print("Please enter 1 single word or two. ")
          return

# this is for the word order sequence two book part 
def first_file2(numberofwords, first_filename, second_filename, files, output_filename):
    firstfile = open(first_filename, 'r', encoding = 'utf-8')
    splitline = [] # this helps to get word in the text
    for line in firstfile:          
        line = line.lower() # clearing the puntuational words
        line = line.replace('-', ' ')
        line = line.replace('“', '')
        line = line.replace('”', '')
        line = line.replace('’', '')
        line = line.replace('—', ' ')
        line = line.replace('‘', '')
        # clearing the puntuational words
        for i in range(33, 65):
            variable = chr(i)
            line = line.replace(variable, '')
        for i in range(91,97):
            variable = chr(i)
            line = line.replace(variable, '')
        for i in range(123,256):
            variable = chr(i)
            line = line.replace(variable,'')            
        splitstop = [] #deleting stop words
        for i in range(0,len(stop_words)):
            splitstop.append(" " + stop_words[i] + " ")
        for i in range(0, len(line)):
              line = line.replace(splitstop[i], ' ')   
                       
        for i in line: # clearing the spaces
            line = line.replace('\n', '')
        splitline.extend(line.split(' '))   #i extend the splitline list with lines in text
    if files == 2: # this helps if its two file or one
    # this is for second file for arranging 
       second_file(splitline, numberofwords, second_filename, output_filename)
    firstfile.close()
    
# this is for the word order sequence one book part
def first_file(numberofwords, first_filename, files, output_filename):
    firstfile = open(first_filename, 'r', encoding = 'utf-8')
    splitline = []  #this helps to get word in the text
    for line in firstfile:          
        line = line.lower()
        line = line.replace('-', ' ') # clearing the puntuational words
        line = line.replace('“', '')
        line = line.replace('”', '')
        line = line.replace('’', '')
        line = line.replace('—', ' ')
        line = line.replace('‘', '')
        for i in range(33, 65): # clearing the puntuational words
            variable = chr(i)
            line = line.replace(variable, '')
        for i in range(91,97):
            variable = chr(i)
            line = line.replace(variable, '')
        for i in range(123,256):
            variable = chr(i)
            line = line.replace(variable,'')             
        splitstop = [] #deleting stop words
        for i in range(0,len(stop_words)):
            splitstop.append(' ' + stop_words[i] + ' ')
            line = line.replace(splitstop[i], ' ')                 
        for i in line:
            line = line.replace('\n', '')
        splitline.extend(line.split(' ')) #i extend the splitline list with lines in text
    print(len(splitline))
    if files == 1:                        # this helps if its two file or one
       #this function can convert the text to list and it can count the words 
       #according to two words or one word order
       text_frequency(splitline, numberofwords, output_filename)
# this is for the word order sequence two book parts second book
def second_file(splitline, numberofwords, second_filename, output_filename):
    secondfile = open(second_filename, 'r', encoding = 'utf-8')
    splitline2 = []                   #this helps to get word in the text
    for line in secondfile:       
        line = line.lower() 
        line = line.replace('-', ' ') # clearing the puntuational words
        line = line.replace('“', '')
        line = line.replace('”', '')
        line = line.replace('’', '')
        line = line.replace('—', ' ')
        line = line.replace('‘', '')
        for i in range(33, 65):      # clearing the puntuational words
            variable = chr(i)
            line = line.replace(variable, '')
        for i in range(91,97):
            variable = chr(i)
            line = line.replace(variable, '')
        for i in range(123,256):
            variable = chr(i)
            line = line.replace(variable,'')  
            
        splitstop = []  #deleting stop words
        for i in range(0,len(stop_words)):
            splitstop.append(" " + stop_words[i] + " ")
        for i in range(0, len(line)):
              line = line.replace(splitstop[i], ' ')
              
        for i in line:
            line = line.replace('\n', '')            
        splitline2.extend(line.split(' ')) #i extend the splitline list with lines in text
       #this function can convert the text to list and it can count the words 
       #according to two words or one word order
    text2_frequency(splitline2, splitline, numberofwords, output_filename)    
    secondfile.close()
              
#this function can convert the text to list and it can count the words according to two words or one word order
def text_frequency(splitline, numberofwords, output_filename): 
    counter = 0
    counterstr = []                          # this is for containing the number of words 
    changing = []
    if numberofwords == 2:                   # if its one word sequence
        twosplitwords = []                   # this is for containing the words with pairs
        for i in range(0, len(splitline)):   # this loop for to appending the pairs word in the null list
           if i < len(splitline) and (i + 1) != len(splitline):
               if splitline[i] != ' ' and splitline[i] != '': # if its space it won't append
                   twosplitwords.append(splitline[i] + ' ' + splitline[i + 1])
        twosplitwords.sort()
        for i in range(0, len(twosplitwords)):                # this part for to counting the words 
             if (i + 1) == len(twosplitwords):
                 break
             if twosplitwords[i] == twosplitwords[i + 1]:  
                 counter += 1
             if twosplitwords[i] != twosplitwords[i + 1]:
                 changing.append(twosplitwords[i])
                 counterstr.append(str(counter))
                 counter = 1
        splitline.clear()                                   # its clears the list before updating it a new list
        splitline.extend(changing)      
        output_file(splitline, counterstr, output_filename) # this is for printing the words and numbers in text file
    elif numberofwords == 1:                                # if its two word sequence
        splitline.sort()
        for i in range(0, len(splitline)):                 # this for part is counting words in the text
             if (i + 1) == len(splitline):                 
                 break                                     
             if splitline[i] == splitline[i + 1]:               
                 counter += 1   
             if splitline[i] != splitline[i + 1]:
                 changing.append(splitline[i])
                 counterstr.append(str(counter))
                 counter = 1                
        splitline.clear()
        splitline.extend(changing)
      
        output_file(splitline, counterstr, output_filename) # this is for printing the words and numbers in text file
#this function can convert the text to list and it can count the words according to two words or one word order   
def text2_frequency(splitline2, splitline, numberofwords, output_filename): 
    counter = 0
    if numberofwords == 1:          # if its one word sequence
        counterstr2 = []            # this is for containing the number of words for text 1
        counterstr = []             # this is for containing the number of words for text 2
        changing = []               # its helps to contain words in a list
        splitline.sort()
        for i in range(0, len(splitline)): # this for part is counting words in the text
             if (i + 1) == len(splitline): 
                                           
                 break
             if splitline[i] == splitline[i + 1]:               
                 counter += 1   
             if splitline[i] != splitline[i + 1]:
                 changing.append(splitline[i])
                 counterstr.append(str(counter))
                 counter = 1                
        splitline.clear()
        splitline.extend(changing)
        
        changing.clear()  # clearing list for the other text
        
        splitline2.sort()
        for i in range(0, len(splitline2)):             # this for part is counting words in the text
             if (i + 1) == len(splitline2):             
                 break                                  
             if splitline2[i] == splitline2[i + 1]:               
                 counter += 1   
             if splitline2[i] != splitline2[i + 1]:
                 changing.append(splitline2[i])
                 counterstr2.append(str(counter))
                 counter = 1                
        splitline2.clear()
        splitline2.extend(changing)
        

        output_file2(splitline, counterstr, counterstr2, splitline2, output_filename) # this is for printing the words and numbers in text file
    elif numberofwords == 2:             # if its two word sequence
        twosplitwords = []               # this is for containing the words with pairs for text1
        twosplitwords2 = []              # this is for containing the words with pairs for text2
        counterstr = []                  # this is for containing the number of words for text 1
        counterstr2 = []                 # this is for containing the number of words for text 2
        changing = []                    # its helps to contain words in a list
        for i in range(0, len(splitline)):        # this loop for to appending the pairs word in the null list
           if i < len(splitline) and (i + 1) != len(splitline) and splitline[i] != '' and splitline != ' ':
               twosplitwords.append(splitline[i] + ' ' + splitline[i + 1])
        twosplitwords.sort()
        for i in range(0, len(twosplitwords)):                # this part for to counting the words 
             if (i + 1) == len(twosplitwords):
                 break
             if twosplitwords[i] == twosplitwords[i + 1]:  
                 counter += 1
             if twosplitwords[i] != twosplitwords[i + 1]:
                 changing.append(twosplitwords[i])
                 counterstr.append(str(counter))
                 counter = 1
        splitline.clear()                                   # its clears the list before updating it a new list
        splitline.extend(changing)         # its clears the list before updating it a new list
        
        changing.clear()                    #clearing lis for other text
        
        for i in range(0, len(splitline2)):    # this loop for to appending the pairs word in the null list
           if i < len(splitline2) and (i + 1) != len(splitline2):
               twosplitwords2.append(splitline2[i] + ' ' + splitline2[i + 1])
        twosplitwords2.sort()
        for i in range(0, len(twosplitwords2)):                # this part for to counting the words 
             if (i + 1) == len(twosplitwords2):
                 break
             if twosplitwords2[i] == twosplitwords2[i + 1]:  
                 counter += 1
             if twosplitwords2[i] != twosplitwords2[i + 1]:
                 changing.append(twosplitwords2[i])
                 counterstr2.append(str(counter))
                 counter = 1
        splitline2.clear()                                   # its clears the list before updating it a new list
        splitline2.extend(changing) 
        output_file2(splitline, counterstr, counterstr2, splitline2, output_filename) # this is for printing the words and numbers in text file                
# this loop for printing the word in a text file  
def output_file2(splitline, counterstr, counterstr2, splitline2, output_filename):
    spl = []                                  # its the last list to appending our words and numbers in it
    for i in range(0,len(splitline)):         # its for if a word is not in text2 but its in text1
        if splitline[i] not in splitline2 : 
            spl.append('   ' + counterstr[i].ljust(3) + '              ' + counterstr[i]  + '                '  + '0' + '          ' + splitline[i])
    for i in range(0,len(splitline2)):        # its for if a word is not in text1 but its in text2
        if splitline2[i] not in splitline : 
            spl.append('   ' + counterstr2[i].ljust(3) + '              ' + '0'  + '                '  + counterstr2[i] + '          ' + splitline2[i])
    if len(splitline2) > len(splitline):      # if the text lenghts are different each other priority
       for i in range(0,len(splitline)):      # if the word exist in both text file
           for i2 in range(0,len(splitline2)):
               if splitline[i] == splitline2[i2] and splitline[i] != '' and splitline[i] != ' 'and splitline2[i] != '' and splitline2[i] != ' ':
                    spl.append('   ' + str(int(counterstr[i]) + int(counterstr2[i2])).ljust(3) + '              ' + counterstr[i]  + '                ' + counterstr2[i2]  + '          ' + splitline[i])
      
    elif len(splitline) > len(splitline2):       # if the text lenghts are different each other priority
         for i2 in range(0,len(splitline2)):     # if the word exist in both text file
           for i in range(0,len(splitline)):
               if splitline2[i2] == splitline[i] and splitline2[i2] != '' and splitline2[i2] != ' 'and splitline[i] != '' and splitline[i] != ' ':
                    spl.append('   ' + str(int(counterstr[i]) + int(counterstr2[i2])).ljust(3) + '              ' + counterstr[i]  + '                ' + counterstr2[i2]  + '          ' + splitline2[i2])
        
    spl.sort(reverse = True) 
    outputfile = open(output_filename, 'w', encoding = 'utf-8')
    outputfile.write("  TOTAL     |     BOOK1    |     BOOK2     |     WORD   \n")
    outputfile.write("--------------------------------------------------------\n")
    outputfile.writelines(spl[0] + '\n')        # printitn gthe last list in a text file
    outputfile.writelines(" ")
    for i in range(0,len(spl)):
        for i2 in range(0,len(spl)):
            i = i2
            if spl[i - 1] != spl[i]:            # this is for preventing the print same words again and again
                outputfile.writelines(spl[i] + '\n')     
                outputfile.writelines(" ")
        break
    outputfile.close()
          
def output_file(splitline, counterstr, output_filename):
    lastlist = []                         # its the last list to appending our words and numbers in it
    for i in range(0,len(splitline)):     # updating the last list with number and its word
        if splitline[i] != '' and splitline[i] != ' ':
            lastlist.append(counterstr[i].ljust(3) + '             ' + splitline[i])
    outputfile = open(output_filename, 'w', encoding = 'utf-8')
    outputfile.write("  TOTAL    |    WORD   \n")
    outputfile.write("-----------------------\n")
    lastlist.sort(reverse=True)
    outputfile.writelines(lastlist[0] + '\n')     # printitn gthe last list in a text file
    outputfile.writelines(" ")
    for i in range(0,len(lastlist)):
        for i2 in range(0,len(lastlist)):
           i = i2          
           if lastlist[i - 1] != lastlist[i2]:    # this is for preventing the print same words again and again
             outputfile.writelines(lastlist[i2] + '\n')     
             outputfile.writelines(" ")
        break      
    outputfile.close()

          


   


   
