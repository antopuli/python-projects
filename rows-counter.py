
# defining 'count_rows' function with a parameter named 'text'
def count_rows(text):
    
    # create a list containing all the characters of the given argument
    tList = list(text) 
    
    # create a list that will contain all the text's rows
    rows = []
    
    # create a string that will contain a row to append to rows
    row = ''

    # the for loop navigate from 0 to tList's length
    
    # if the element of tList with a index of 'i' is equal to '\n' or 
    # 'i' is the last index of tList then the 'row' variable will be append to
    # the 'rows' one as a list and it will be initialized as an empty string
    
    # else the element of tList with a index of 'i' will be concatenated to
    # the 'row' existing string
    
    for i in range(len(tList)):
        if tList[i] == '\n' or i == (len(tList)-1):
            rows.append(list(row))
            row = ''
        else:
            row += tList[i]

    # the for loop navigate from 0 to the number of empty lists contained in the
    # 'rows' variable
    
    # remove from the 'rows' list the empyt ones
    
    for i in range(rows.count([])): rows.remove([])
    
    # return the number of rows
    return len(rows)
    

dante = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura, 
che la diritta via era smarrita. 

Ahi quanto a dir qual era è cosa dura, 
esta selva selvaggia e aspra e forte, 
che nel pensier rinnova la parola."""


print(f'Text contains {count_rows(dante)} rows.')