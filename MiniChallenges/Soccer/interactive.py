#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 07:44:25 2020

@author: lisacao, Laura G.F., Tina Leard

Modified on Mon Dec 5, 2022 by Jordan Swanson
"""



# libraries
import random
import pandas as pandas
import matplotlib.pyplot as plt 
from IPython.display import clear_output, display

# import data - ensure whatever CSV you're using for the hackathon is named 'data.csv'
df = pandas.read_csv("data.csv")

################################ TEXT ENCODING

def cbot(text): # blocked out grey with emoji
    cb = "\033[1;37;40m 🤖 CallystoBot: \033[1;0m" + text + "\033[1;0m"
    return cb

def task(text, check = False): # light blue with emoji option
    if check == True:
        blu = "\033[1;36m" + "✅ " + text + "\033[1;0m"
        return blu
    else:
        blu = "\033[1;36m" + text + "\033[1;0m"
        return blu

def bedazzle(text): # purple with randomized  emoji 
     sparkle = ["✨ ", "🌟 ", "🎉 ", "🥳 ", "🤩 ", "🎊 ", "🚀 ", "😎 "]
     prl = "\033[1;35m" + random.choice(sparkle) + text + "\033[1;0m"
     return prl
   
def normal(text): # plain black 
     nrl = "\033[1;0m" + text + "\033[1;0m"
     return nrl
 
def code(text): # bright green 
     grn = "\033[1;32m" + text + "\033[1;0m"
     return grn
 
def tryagain(text, exclaim = True): # red with default emoji 
    if exclaim == False:
        red = "\033[1;31m" + text + "\033[1;0m"
        return red
    else:
        red = "\033[1;31m" + "❗️ " + text + "\033[1;0m"
        return red

# positive feedback for correct answers
def correct_answer(): # random positive reinforcement
    compliment = ["Amazing work!", "Nice job!", "Right on!", "Awesome possum!", "You're out of this world!", "Great stuff!", "You rock!", "I wish I were this good!", "What a rockstar coder!", "Correct!", "Glad we have you around!", "That was great!", "You're picking up on this really well!", "Even CallystoBot is impressed!", "Keep it up!", "Impressive work!"]
    nice = print(bedazzle(random.choice(compliment)))
    return nice 

################################ USERINFO

def greet(): # get user's name
    name = input(cbot(" Heya! I guess we'll be working together from now on! What's your name? Press the 'enter' key (or 'return' on a Mac) when you're done. "))
    print(cbot(" Nice to meet you, "),name,"!")
    return name
    
def userinfo(): # get other info
    name = greet()

################################ CHALLENGE 1
# Question 1 A
def challenge1a(): # import command challenge
    print(cbot(" If we want to use commands in Python, we need to bring in a library called"), code("pandas"), normal("into the notebook using some code.\n"), task("Try to fill in the", check = True), code("import"), task("command."))
    def Q1A(): 
        ans = str(input(code("import ")))
        if ans == "pandas":
            correct_answer()
        else:
            print(tryagain("Hmm.. not quite. Try"), code("pandas"))
            Q1A()
    #execute
    Q1A()

# Question 1 B
def challenge1b(): # load in dataset challenge
    print(task("Answer the questions correctly to check your understanding.\n", check = True))
    
    def Q1B_1(): # What is the file name?
        ans1 = str(input(cbot(" The file we want to use the ") + code("read_csv() ") + normal("function on is: ")))
        if ans1 == "data.csv" or ans1 == "\"data.csv\"": 
            correct_answer()
        else: 
            print(tryagain("Try again. Make sure you spelled everything correctly and included the file extension"))
            Q1B_1()
        
    def Q1B_2(): # What is the library?
        ans2 = str(input(cbot(" The library we want to use that contains the ") + code("read_csv() ") + normal("function is: ")))
        if ans2 == "pandas":
            correct_answer()
        else: 
            print(tryagain("Try again. Remember that it is case sensitive."))
            Q1B_2()
        
    def Q1B_3(): # write read in function 
        ans3 = str(input(task("Try writing code to access the dataset for this question: ", check = True)))
        if ans3 == "pandas.read_csv(\"data.csv\")" or ans3 == "pandas.read_csv('data.csv')":
            correct_answer()
            display(pandas.read_csv("data.csv"))
            print(cbot(f" Notice there are {df.shape[1]} columns: {[col for col in df.columns]}"))
        else:
            print(tryagain("Hmm, not quite. Try following the format"), code("library.function(\"file.csv\")"), tryagain("or double check your spelling.", exclaim = False))
            Q1B_3()
    #execute
    Q1B_1()
    Q1B_2()
    Q1B_3()
    

# Question 1 C
def challenge1c(): # variables challenge 
    codeword = input(task("Enter a code word (also known as a variable name):\n", check = True) + cbot(" It can be any name! "))
    value = input(task("Now, enter a value for the variable, it can also be any name!\n ", check = True) + code(str(codeword)) + code(" = "))
    df = pandas.read_csv("data.csv") 
    def Q1C_1(): # quick variable demonstration
        code = str(input(task("Now, enter your code word again ", check = True)))
        if code == str(codeword) :
            print(value)
            correct_answer()
            print(cbot(" Notice how when you entered the variable name, it gave you the value instead? This is handy for saving time by making long pieces of code short!"))
        else:
            print(tryagain("Try typing the code word from above. Remember to make sure your spelling and capitalization are the same, too. "))
            Q1C_1()
        
            
    def Q1C_2(): # assign the dataset to a variable 
        ans = str(input(task("Now, let's try assigning the dataset as a variable! Write the code to access your dataset.\n", check = True) + code("data =  ")))
        if ans == "pandas.read_csv(\"data.csv\")" or ans == "pandas.read_csv('data.csv')":
            correct_answer()
        else:
            print(tryagain("Try library.function(\"file.csv\") from the last question to access the data!", exclaim = True))
            Q1C_2()
        
        
    def Q1C_3(): # use variable to display dataset
        ans2 = input(task("Now, type ", check = True) + code("data ") + task(" to access the data\n"))
        if ans2 == "data": 
            correct_answer()
            print(cbot(" Notice the 0 in the first row. In Python, we start counting from zero."))
        else:
            print(tryagain("Try typing ", exclaim = True) + code("data "))
            Q1C_3()
    # execute 
    Q1C_1()
    Q1C_2()
    Q1C_3()
    return df
    
    
################################ CHALLENGE 2
    
# Question 2 A
def challenge2a(): #heads and tails challenge
    def Q2A_1(): # view head
        ans = str(input(cbot(" If I only wanted to see the top of the dataset, I would write: \n") + code("data")))
        if ans == ".head()": 
            correct_answer() 
        else: 
            print(tryagain("Not quite, try "), code(".head()"))
            Q2A_1()
        clear_output(wait = True)
        return display(df.head())
    def Q2A_2(): # view tails
        ans2 = str(input(cbot(" If I only wanted to see the bottom of a dataset, I would write: \n") + code("data")))
        if ans2 == ".tail()": 
            correct_answer()
        else:
            print(tryagain("Not quite, try"), code(".tail()"))
            Q2A_2()
            return display(df.tail())       
    #execute 
    Q2A_1()
    Q2A_2()
    
    
# Question 2 B
def challenge2b(): # view data columns
    print(cbot(" First, we will need to know what columns are in the data. We can do this by either looking at the dataset again, or use "), code("data.columns"))
    def Q2B(): # view columns
        ans = str(input(task("Try filling in the command to list all the columns: \n", check = True) + code("data")))
        if ans == ".columns": 
            correct_answer() 
        else: 
            print(tryagain("Hmm, not quite. Make sure you have the right spelling!"))
            Q2B()
    #execute
    Q2B()
    return df.columns
    
# Question 2 C 
def challenge2c(): # selecting columns
    print(cbot(f" Now that we have all the column names, let's choose a couple to look at. How about the "), code(df.columns[0]), normal("column?\n"), task("Select the column using ", check = True), code("data[\"column_name\"]"))
    def Q2C(): # select name column
        ans = str(input(code("data")))
        if ans == f"['{df.columns[0]}']" or f'["{df.columns[0]}"]':
            correct_answer()
        else: 
            print(cbot(" Remember, it has to be the exact same spelling and case as in the list. Did you double check to use "), code("[ ] "), normal("instead of "), code("( )"), normal("?"))
            Q2C()
    #execute
    Q2C()
    return df[df.columns[0]]


# Question 2 D 
def challenge2d(): # finding the longest name
    print(cbot(" Take a look at the table we generated with the "), code(df.columns[0]), normal("in the data.\n"), task("Type the longest name in the list ", check = True))
    def Q2D(): # select name column
        ans = str(input(normal("The longest name is: ")))
        ans = ans.replace('Stefano', 'Stéfano')
        longest = df[df.columns[0]].sort_values(key=lambda x: x.str.len(), ascending=False).iloc[0]
        if ans == longest or ans==f"'{longest}'" or ans==f'"{longest}"':
            correct_answer()
        else: 
            print(cbot(" Almost there!"))
            Q2D()
    #execute
    Q2D()

          
################################ CHALLENGE 3

# plot example 
def challengeplotall(): # demonstrate messy plot
    print(cbot(" Before we start, we should try just plotting the data! I wonder what we will find?"))
    def QPlot(): # plot all data 
        ans = str(input(task("Try adding ", check = True) + code(".plot()") + task(" to the end of the following command\n") + code("data")))
        if ans == ".plot()": 
            df.plot()
            print(cbot(" This isn't the easiest plot to understand, there's a lot going on and it's pretty messy. Let's build our skills through these notebooks to make something we can actually understand!"))
        else: 
            print(tryagain("Make sure you type the code exactly like in the instructions!"))
            QPlot()
    #execute
    QPlot()
    
    

# Question 3 A
def challenge3a(): # get unique values 
    print(cbot(f" Now, because all the names are unique, we should try using another column of data.\nHmm, how about {df.columns[2]}? Or better yet, {df.columns[1]}!"))
    def Q3A(): # get unique values 
        ans = str(input(task(f"Fill in the command to get the unique values for {df.columns[1]}.\n", check = True) + code(f"unique = data['{df.columns[1]}']")))
        if ans == ".unique()": 
            correct_answer()
            print(cbot(f" Notice that the array below organizes the values in a row. The column of {df.columns[1]} has the unique values of \n{df.iloc[:,1].unique().tolist()}"))
        else: 
            print(tryagain("Close! Make sure you remember the period and brackets. Use "), code("data['columnname'].unique()"))
            Q3A()
    #execute
    Q3A()
    
# Question 3 B
def challenge3b(): # using basic operators 
    print(cbot(" The unique values we found in our last step are interesting, but let's see what we can do with a column that contains numbers!"))
    print(cbot(f" First, we'll need to use a basic operator on the {df.columns[-1]} column to find the ones that are greater than 4."))
    def Q3B(): # select international goals greater than 4
        ans = str(input(task("Try filling in the command\n", check = True) + code(f"data['{df.columns[-1]}'] > ")))
        if ans == "4": 
            correct_answer()
            return display(df[df.columns[-1]] >4)
        else: 
            print(tryagain(f"Try the number of {df.columns[-1]}"))
            Q3B()
    #execute 
    Q3B()
  
    # Question 3 C
def challenge3c(): # access a row using loc
    print(cbot(" Looks like there's only one row that returns "), code("False"), normal(". Can you use "), code(".loc"), normal(" to find out more?"))
    def Q3C(): # view row 17
        ans = str(input(task("Fill in the command:\n", check = True) + code("data")))
        if ans == ".loc[17]":
            correct_answer()
            return display(df.loc[17])
        elif ans == ".loc[[17]]":
            correct_answer()
            return display(df.loc[[17]])
        else:
            print(tryagain("Try using "), code(".loc[rownumber]"), tryagain(" or ", exclaim = False), code(".loc[[rownumber]]"), tryagain(", the second outputs as a row!", exclaim = False))
            Q3C()
    Q3C()
    
# Question 3 D 
def challenge3d(): # finding the player name
    print(cbot(" Take a look at the table we generated with the "), code(f"{df.columns[-1]}\n"), task(f"Type the {df.columns[0]} with less than 4 {df.columns[-1]} ", check = True))
    def Q3D(): # select name column
        ans = str(input(normal(f"The {df.columns[0]} with less than 4 {df.columns[-1]} is: ")))
        if ans == df.iloc[17][0]:
            correct_answer()
        else: 
            print(cbot(" Almost there. Check the previous answer!"))
            Q3D()
    #execute
    Q3D()

# Question 3 E
def challenge3e(): # advanced basic operators and logical operators 
    print(cbot(" Good work!! Let's try to do some other examples. Since I'm a robot from Canada, I want to see if there are any other robots like me! Can you try and find out?"))
    def Q3E_1(): # get all Canadians
        ans1 = str(input(task("Try to find all the Canadians by using the == operator.\n", check = True) + code("data.loc")))
        ans1 = ans1.replace(" ","")
        if ans1 == f'[data["{df.columns[1]}"]=="Canada"]' or ans1 == f"[data['{df.columns[1]}']=='Canada']":
            correct_answer()
            return display(df[df[df.columns[1]] == "Canada"])
        else:
            print(tryagain("Very close! Why don't you try "), code(f"[data[\'column_name\'] == \'search_term\'] "), tryagain(f"where the column is '{df.columns[1]}' and filter is 'Canada'? Remember that capitalization matters!", exclaim = False))
            Q3E_1()
        clear_output(wait = True)
 
    def Q3E_2(): # get all players with over 100 International Appearances
        ans2 = str(input(task(f" Now try to write an operator that can find all values of {df.columns[0]}s with over 100 {df.columns[-2]}!\n", check = True) + code("data.loc")))
        if ans2 == f'[data["{df.columns[-2]}"]>100]' or ans2 == f"[data['{df.columns[-2]}']>100]":
            correct_answer()
            return display(df[df[df.columns[-2]] > 100])
        elif ans2 == f'[data["{df.columns[-2]}"] > 100]' or ans2 == f"[data['{df.columns[-2]}'] > 100]":
            correct_answer()
            return display(df[df[df.columns[-2]] > 100])
        else: 
            print(tryagain("Try "), code(f"[data[\"column_name\"] > {df.columns[-2]} "), tryagain(f"where the column is {df.columns[-2]} and {df.columns[-2]} is > 100. Remember that spelling and spaces matter!", exclaim = False))
            Q3E_2()
  
    def Q3E_3(): # get all Canadians with over 100 appearances
        print(cbot(" Wow! You're really good. How about we try to do both at once? I think the format was "), code("data.loc[(operator1) & (operator2)]"))
        def Q3E_3A():# combine two operators 
            ans3 = str(input(task(f"Try to combine the two operators you wrote previously to find all Canadian {df.columns[0]}s with over 100 {df.columns[-2]}. Remember to always have matching brackets!\n", check = True) + code("data.loc")))
            # alternatively can potentially use regex to parse this?
            if ans3 == f"[(data['{df.columns[-2]}'] > 100) & (data['{df.columns[1]}'] == 'Canada')]" or ans3 == f'[(data["{df.columns[-2]}"] > 100) & (data["{df.columns[1]}"] == "Canada")]': 
                correct_answer()
                return display(df.loc[(df[df.columns[-2]] > 100) & (df[df.columns[1]] == 'Canada')])
            elif ans3 == f"[(data['{df.columns[1]}'] == 'Canada') & (data['{df.columns[-2]}'] > 100)]" or ans3 == f'[(data["{df.columns[1]}"] == "Canada") & (data["{df.columns[-2]}"] > 100)]': 
                correct_answer()
                return display(df.loc[(df[df.columns[-2]] > 100) & (df[df.columns[1]] == 'Canada')])
            elif ans3 == f"[(data['{df.columns[-2]}']>100)&(data['{df.columns[1]}']=='Canada')]" or ans3 == f'[(data["{df.columns[-2]}"]>100)&(data["{df.columns[1]}"]=="Canada")]': 
                correct_answer()
                return display(df.loc[(df[df.columns[-2]] > 100) & (df[df.columns[1]] == 'Canada')])
            elif ans3 == f"[(data['{df.columns[1]}']=='Canada') & (data['{df.columns[-2]}']>100)]" or ans3 == f'[(data["{df.columns[1]}"]=="Canada") & (data["{df.columns[-2]}"]>100)]': 
                correct_answer()
                return display(df.loc[(df[df.columns[-2]] > 100) & (df[df.columns[1]] == 'Canada')])
            else:
                print(tryagain("This one is definitely tricky! Try seeing what you may have missed by comparing your answer to this: \n"), code(f"data.loc[(data['{df.columns[-2]}'] > 100) & (data['{df.columns[1]}'] == 'Canada')] "), tryagain("\nNote that when we have 2 or more, we need to separate them by putting each one in ", exclaim = False), code("( )"))
                Q3E_3A()
        Q3E_3A()
    #execute
    Q3E_1()
    Q3E_2()
    Q3E_3()
        
    
################################ CHALLENGE 4
# Question 4 A
def challenge4a(): # sort values 
    print(cbot(" I wonder how many goals these players have scored! Should that be considered?"))
    print(task("Try filling in the command to sort values by", check = True), code(f"'{df.columns[8]}'"))
    def Q4A(): # sort by time to adoption 
        ans = str(input(code("data")))
        if ans == f".sort_values(by='{df.columns[8]}')" or ans == f'.sort_values(by="{df.columns[8]}")':
            correct_answer()
            display(df.sort_values(by=df.columns[8]))
        else: 
            print(cbot(" Better than I could have done!\n"), tryagain(f"Try .sort_values(by='{df.columns[8]}')"))
            Q4A()
    #execute
    Q4A() 

# Question 4 B
def challenge4b():
    print(cbot(" Wow! We've done so much so far. I'm really learning a lot and I can't wait until we make some graphs after these challenges are done!"))
    print(cbot(" I'm really excited to try some of those subsetting techniques though. Let's try them out together!"))
    # Modify this to match the dataset
    subset = df[df.columns[0:6]]

    def Q4B_1(): # column subset and nested sort
        ans1 = str(input(task("Try filling in this command to make a new dataframe out of the ", check = True) + code(f"{list(df.columns[0:5])}") + task(" and ") + code(f"{df.columns[5]}") + task(" columns! - In that order.\n") + code("subset = data")))
        if ans1 == f"[{list(df.columns[0:6])}]":
            correct_answer()
        else: 
            print(tryagain("Make sure it looks something like "), code(f"[{list(df.columns[0:6])}]"), tryagain("Remember that case and spacing matter!", exclaim=False))
            Q4B_1()
        
            
    def Q4B_1A(): # question to access with variable name
        ans2 = str(input(task("Now try typing ") + code('subset') + task(" to see the dataframe! :)\n")))
        if ans2 == "subset":
            correct_answer()
            display(subset)
        else: 
            print(tryagain("Try again!"))
            Q4B_1A()
        
            
    def Q4B_1B(): # sort subset dataframe by age 
        ans3 = str(input(task(f"Why don't we try sorting this data by {df.columns[3]} now? Fill in the command and let's try it!\n", check = True) + code("subset")))
        if ans3 == f".sort_values(by='{df.columns[3]}')" or ans3 == f'.sort_values(by=\"{df.columns[3]}")':
            correct_answer()
            display(subset.sort_values(by=df.columns[3]))
        else:             
            print(tryagain("Try subset"), code(f".sort_values(by='{df.columns[3]}')"))      
            Q4B_1B()
        
         
    
    #execute
    Q4B_1()
    Q4B_1A()
    Q4B_1B()
           

# Question 4 C
def challenge4c(): # slice dataframe 
    subset = df[df.columns[0:6]]
    def Q4C_1(): #slice dataframe to rows 6 - 17
        ans = str(input(task("Now, let's try getting some rows! Fill in the command and try to access rows 6 - 17! \n", check = True) + code("subset")))
        if ans == ".loc[6:17]":
            correct_answer()
            return display(df.loc[6:17])
        else: 
            print(tryagain("Try again! Remember we are using "), code(".loc[1:2]"))
            Q4C_1() 
        clear_output(wait = True)
            
    def Q4C_2(): # slice subset to rows 5 - 12
        ans2 = str(input(task("Now let's try getting rows 5-12 from the data we subsetted in the last question!\n", check = True) + code("subset")))
        if ans2 == ".loc[5:12]":
            correct_answer()
            return display(subset.loc[5:12])
        else:
            print(tryagain("Try again! Remember we are using "), code(".loc[1:2]"))
            Q4C_2()
    #execute 
    Q4C_1()
    Q4C_2()
            

# Question 4 D
def challenge4d(): # use basic statistics methods
    def Q4D_1(): # try out commands on weight column
        ans = str(input(task(F"Try out the different statistics methods on the {df.columns[-2]} column!\n", check = True) + code(f"data['{df.columns[-2]}']")))
        # case handling 
        if ans == ".max()":
            correct_answer()
            return display(df[df.columns[-2]].max()), print(cbot(" That's a lot of appearances!"))
        elif ans == ".min()":
            correct_answer()
            return display(df[df.columns[-2]].min())
        elif ans == ".mean()": 
            correct_answer()
            return display(df[df.columns[-2]].mean())
        elif ans == ".describe()": 
            correct_answer()
            return display(df[df.columns[-2]].describe())
        else: 
            print(tryagain("That doesn't seem to be a valid method!"))
            Q4D_1()  
            
    def Q4D_cont(): # recursive try agains 
        cont = input("Would you like to try another method? (y/n)")
        if cont == "y" or cont == "yes" or cont == "Yes": 
            challenge4d()
        else: 
            def Q4D_2(): # nested describe function
                ans2 = str(input(task("Try to use ", check = True) + code(".describe()") + task(" on the data now!\n") + code("data")))
                if ans2 == ".describe()": 
                    correct_answer()
                    return display(df.describe())
                else:
                    print(tryagain("Try again!"))
            Q4D_2()
    #execute 
    Q4D_1()
    Q4D_cont()
    
# Question 4 E 
def challenge4e(): # finding the weight of the heaviest animal
    print(cbot(" Take a look at the table we generated with the "), code(f"{df.columns[3]}"), normal("of the data.\n"), task(f"Type the name of the youngest {df.columns[0]}", check = True))
    def Q4E(): # select weight column
        ans = str(input(normal("The youngest player is: ")))
        if ans == df.loc[21][0]:
            correct_answer()
        else: 
            print(cbot(" Almost there. Hint, the name starts with A"))
            Q4E()
    #execute
    Q4E()


################################ CHALLENGE 5
# Question 5 A
def challenge5a(): # import matplotlib's pyplot 
    print(cbot(" Because we are using"), code(" matplotlib"), normal(", we should import it!"))
    def Q5A(): # import pyplot submodule
        ans1 = str(input(task("Fill in the command below. Because we are using only ", check = True) + code('pyplot') + task(", write ") + code("matplotlib.pyplot\nimport ")))
        if ans1 == "matplotlib.pyplot": 
            correct_answer()
            def Q5A_1(): # assign it as plot
                ans1A = input(cbot(" Did you know that you can use ") + code("as ") + normal("to assign a library to a variable? \n ") + task("Try typing ", check = True) + code("import matplotlib.pyplot as plt ") + task("below!\n"))
                if ans1A == "import matplotlib.pyplot as plt": 
                    correct_answer()
                else: 
                    print(tryagain("Try again! You will have to write the whole command from scratch for this one."))
                    Q5A_1()
            Q5A_1()
        else: 
            print(tryagain("Try again!"))
            Q5A()
    #execute
    Q5A()

# Question 5 B
def challenge5b(): # make a bar graph
    print(cbot(" Now that we've imported the package. let's try making some graphs! I'm so excited!!"))
    def Q5B_1():
        ans = str(input(task(f"Try making a bar graph of {df.columns[5]} as the x column, and {df.columns[8]} as the y column. Let's see what we find!\n", check = True) + code("plt")))
        if ans == f".bar(data['{df.columns[5]}'], data['{df.columns[8]}'])" or ans == f'.bar(data["{df.columns[5]}"], data["{df.columns[8]}"])':
            correct_answer()
            print(cbot(f" Notice that the graph visualizes into bars to see how many there are in a category. This bar graph tells us how many {df.columns[8]} each category of {df.columns[5]} has."))
            plt.bar(df[df.columns[5]], df[df.columns[8]])
            plt.title(f'{df.columns[8]} by {df.columns[5]}')
            plt.xlabel(df.columns[5])
            plt.ylabel(df.columns[8])
            plt.show()
            # # custom plotting function
            # def pltbr():
            #     pltbr = str(input(cbot("Do you want to try using different columns? (y/n)")))
            #     if pltbr == "y" or pltbr == "yes" or pltbr == "Yes": 
            #         clear_output(wait = True)
            #         xcol = str(input(task("Please enter a valid column for x: ", check = True)))
            #         ycol = str(input(task("Please enter a valid column for y: ", check = True)))
            #         pltbr = plt.bar(xcol, ycol)
            #         plt.show()
            #         #recursive try again
            #         def pltbr_retry(): 
            #             rtry = str(input("Do you want to try again? (y/n)"))
            #             if rtry == "y" or rtry == "yes" or rtry == "Yes": 
            #                 pltbr()
            #             else:
            #                 print(task("Continue to the next question", check = True))
            #         #execute
            #         pltbr_retry()
            #         clear_output(wait = True)
            #     else:
            #         print(task("Continue to the next question", check = True))
            # #execute
            # pltbr()         
        else: 
            print(tryagain("Hmm, not quite. How about trying "), code(f"plt.bar(data['{df.columns[5]}'], data['{df.columns[8]}'])"))
            Q5B_1()
    #execute
    Q5B_1()
      
################################ CHALLENGE 5     

# Challenge 5 C       
def challenge5c(): # make a histogram 
    print(cbot(" Let's try making a histogram now! "))
    def Q5C():
        import numpy as np
        ans = str(input(task(f"Let's try making a histogram now! Can you fill in this command to create a histogram of the {df.columns[1]} column? \n", check = True) + code("plt")))
        if ans == f".hist(data['{df.columns[1]}'])" or ans == f'.hist(data["{df.columns[1]}"])':
            correct_answer()
            print(cbot(f" Notice that the histogram visualizes in bars and counts how many different values for {df.columns[1]} exist in the data. There are many more from {df[df.columns[1]].value_counts().index.tolist()[0]} compared to {df[df.columns[1]].value_counts().index.tolist()[-1]}, {df[df.columns[1]].value_counts().index.tolist()[-2]}, and {df[df.columns[1]].value_counts().index.tolist()[-3]}."))
            nc = len(df[df.columns[1]].unique())
            plt.hist(df[df.columns[1]], bins=nc, rwidth=0.8)
            plt.xlabel(df.columns[1])
            plt.xticks(np.linspace(0, nc-1, 2*nc+1)[1::2])
            plt.ylabel("Count")
            plt.xticks(rotation=90)
            plt.show()
            # # make a custom histogram
            # def plthst():
            #     plthst = str(input(cbot("Do you want to try using a different column? (y/n)")))
            #     if plthst == "y" or plthst == "yes" or plthst == "Yes":
            #         clear_output(wait = True)
            #         xcol = str(input(task("Please enter a valid column for x: ", check = True)))
            #         ycol = str(input(task("Please enter a valid column for y: ", check = True)))
            #         plt.hist(xcol, ycol)
            #         plt.show()
            #         #recursive try again
            #         def plthst_retry(): 
            #             rtry = str(input("Do you want to try again? (y/n)"))
            #             if rtry == "y" or rtry == "yes" or rtry == "Yes": 
            #                 clear_output()
            #                 plthst()
            #             else:
            #                 print(task("Continue to the next question", check = True))
            #         #execute
            #         plthst_retry()
            #         clear_output(wait = True)
            #     else:
            #         print(task("Continue to the next question", check = True))
            # #execute
            # plthst()    
        else: 
            print(tryagain("Hmm, not quite. How about trying "), code(f"plt.hist(data['{df.columns[1]}'])"))
            Q5C()
    #execute
    Q5C()

# Challenge 5 D
def challenge5d(): # make a scatterplot   
    print(cbot(" Let's try making a scatterplot now! These are my favourite!"))
    def Q5D():
        ans = str(input(task(f"Can you fill in this command to create a scatterplot using '{df.columns[7]}' as the x column and '{df.columns[9]}' as the y column? \n", check = True) + code("plt")))
        if ans == f".scatter(data['{df.columns[7]}'], data['{df.columns[9]}'])" or ans == f'.scatter(data["{df.columns[7]}"], data["{df.columns[9]}"])':
            correct_answer()
            print(cbot(f" Notice that some data points are close while others are far apart. This means that the relationship between {df.columns[7]} and {df.columns[9]} looks like a positive relationship where more {df.columns[7]} means more {df.columns[9]}. Hmm, but there are two players that have significant numbers of {df.columns[9]} yet not many {df.columns[7]}. These would be what we can consider outliers."))
            plt.scatter(df[df.columns[7]], df[df.columns[9]])
            plt.xlabel(df.columns[7])
            plt.ylabel(df.columns[9])
            plt.show()
        else: 
            print(tryagain("Hmm, not quite. How about trying "), code(f"plt.scatter(data['{df.columns[7]}'], data['{df.columns[9]}'])"))
            Q5D()
    #execute
    Q5D()

    # Challenge 5 E
def challenge5e(): # make a pie chart   
    print(cbot(" Lastly, we can look at our data as a pie chart! These are popular and pretty easy to make!"))
    def Q5E():
        ans = str(input(task(f"Can you fill in this command to create a pie chart using '{df.columns[5]}'? \n", check = True) + code("plt")))
        if ans == f".pie(data['{df.columns[5]}'])" or ans == f'.pie(data["{df.columns[5]}"])':
            correct_answer()
            print(cbot(f" We have a good balance of each position in our data! This is going to be important when you select the team, as we can't have a team full of strikers!"))
            plt.pie(df[df.columns[5]].value_counts(), labels=df[df.columns[5]].value_counts().index.to_list(), autopct='%1.1f%%')
            plt.title('Percentage of each position in dataset')
            plt.show()
        else: 
            print(tryagain("Hmm, not quite. How about trying "), code(f"plt.pie(data['{df.columns[5]}'])"))
            Q5E()
    #execute
    Q5E()