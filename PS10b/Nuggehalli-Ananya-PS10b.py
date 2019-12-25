import numpy as np
def split(word):
    return [char for char in word]

def alignStrings(x, y, c_insert, c_delete, c_sub):
    #array prints flipped
    
    #x and y are 2 strings, need to split the strings into symbols
    X = split(x)
    Y = split(y)
    
    #n_x and n_y are how many symbols are in X and Y
    n_x = len(X)
    n_y = len(Y)
    
    #if x[i] = y[i], then NO OP
    
    #S = cost matrix
    #initalize s, will need to return S
    S = [[0 for yIndex in range(n_y + 1)] for xIndex in range(n_x + 1)] #S should be of size [n_x][n_y]
    S[0][0] = 0 
    
    for xIndex in range(n_x + 1):
        S[xIndex][0] = xIndex*c_insert
    for yIndex in range(n_y + 1):
        S[0][yIndex] = yIndex*c_delete
    
    x_index = 1
    while x_index < n_x + 1:
        y_index = 1
        while y_index < n_y + 1:
            if(X[x_index-1] == Y[y_index-1]):
                S[x_index][y_index] = S[x_index-1][y_index-1]
                
            else:
                S[x_index][y_index] = min((S[x_index-1][y_index-1] + c_sub, S[x_index][y_index-1] + c_delete, S[x_index-1][y_index] + c_insert))
            y_index+=1
        x_index+=1
    
    return S

x = "EXPONENTIAL"
y = "POLYNOMIAL"
cInsert = 1
cDelete = 1
cSub = 1

S = alignStrings(x, y, cInsert, cDelete, cSub)
print("Cost Matrix S:")
print(np.matrix(S))

########################################################################################################################################################################################################################################################################################


#extractAlignment
def extractAlignment(S, x, y, c_insert, c_delete, c_sub):
    X = split(x)
    Y = split(y)
    n_x = len(X)
    n_y = len(Y)
    
    #start at very end of S[n_x][n_y]
    xIndex = n_x
    yIndex = n_y
    
    #have an array to store operations
    a = []
    
    while xIndex != 0 and yIndex != 0:
        
        if (S[xIndex][yIndex] == S[xIndex - 1][yIndex - 1] and X[xIndex - 1] == Y[yIndex - 1]):
            a.append(["no-op", xIndex])
            xIndex -= 1
            yIndex -= 1
            
        elif S[xIndex][yIndex] == S[xIndex-1][yIndex-1] + c_sub:
            a.append(["sub", xIndex])
            xIndex -= 1
            yIndex -= 1
                
        elif S[xIndex][yIndex] == S[xIndex - 1][yIndex] + c_insert:
            a.append(["insert", xIndex])
            xIndex -= 1
                
        elif S[xIndex][yIndex] == S[xIndex][yIndex - 1] + c_delete:
            a.append(["delete", xIndex])
            yIndex -= 1
        
    #if xIndex != 0, then append amount of deletes that xIndex is at
    #if xIndex = 2, then append 2 deletes
    while xIndex != 0:
        a.append(["delete", xIndex])
        xIndex -= 1
        
    #if yIndex != 0, then append amount of insert that yIndex is at
    #if yIndex = 1, then append 2 insert
    while yIndex != 0:
        a.append(["insert", xIndex])
        yIndex -= 1

    return a[::-1]

print("Ops:")
a = extractAlignment(S, x, y, cInsert, cDelete, cSub)
print(a)

########################################################################################################################################################################################################################################################################################

#commonSubstrings
def ExtractOp(lst):
    return [item[0] for item in lst]
def ExtractIndex(lst):
    return [item[1] for item in lst]

def commonSubstrings(x, L, a):
    
    X = split(x)
    #list of characters
    curr = ''
    #list of subStrings 
    subStrings = []
    
    #extract operations and the x[index] into 2 seperate arrays
    Ops = ExtractOp(a)
    xIndex = ExtractIndex(a)
    
    pos = 0
    
    #iterate through Ops looking for position where it's no-op
    for pos in range(len(Ops)):
        if Ops[pos] == "no-op":
            #get the xIndex at this position
            xPos = xIndex[pos] - 1
            #get the letter of x at xPos
            curr += X[xPos]
        else:     
            if len(curr) >= L:
                subStrings.append(curr)
            curr = ''
    
    #check if curr >= L
    if len(curr) >= L:
        subStrings.append(curr)
            
    return subStrings

L = 1
print("Sub-Strings:")
SubString = commonSubstrings(x, L, a)
print(SubString)

########################################################################################################################################################################################################################################################################################


#PLAGERISM DETECTOR
f = open("Song1_Folsom_Prison.txt", "r")
if f.mode == 'r':
    x = f.read()

g = open("Song2_Crescent_City_Blues.txt", "r")
if g.mode == 'r':
    y = g.read()

cInsert = 1
cDelete = 1
cSub = 1
#call alignStrings
S = alignStrings(x, y, cInsert, cDelete, cSub)

#call extractAlignment
a = extractAlignment(S, x, y, cInsert, cDelete, cSub)

#call commonSubstrings
L = 10
print(commonSubstrings(x, L, a))