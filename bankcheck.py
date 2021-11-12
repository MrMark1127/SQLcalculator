import csv

with open('bank.txt', encoding='utf-8-sig') as csv_file: #Opening the text file
    csv_reader = csv.reader(csv_file, delimiter=',') #Assigning a reader to the text file, started as CSV | Unsure if this is needed
    line_count = 1                                     #Starting a count, has to be 1 to work with code below idfk why. 0 won't work
    bank_account = []                                #Creating an empty table to manipulate
    total = 0                                           #Initalizing a total variable
    for row in csv_reader:                              #For loop that will count through the text file via the csv_reader
        if line_count >= 1:                             #Has to be 1, 0 won't work idfk why
            bank_account.append(int(row[0]))            #Adding new table insertions for every line in the file
            line_count += 1                             #When it passes one line, it will add a line to the total lines
    print(f'Processed {line_count} lines.')             #Print to say lines cause meme

    elements = 0
    for ele in bank_account:                            #Adding the total amount
        if elements != len(bank_account):               #Checking if we double'd over any calculation, number of items in element can't equal the length of the table and continue
            total = total + ele                             #Resetting the total amount to be equal to the total + whatever the element is
            elements += 1                                   #Adding one element count for every pass
            total_final = "${:,.2f}".format(total)          #Formatting cause boujee
        else:
            break
    print("There is " + total_final + " in the server") #Total Print

    textfile = open("banklist.txt", "w")                #Writing the split data to a new file
    for element in bank_account:
        textfile.write(str(element) + "\n")
    textfile.close()