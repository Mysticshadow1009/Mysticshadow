'''WELCOME TO MATRIX SOLVER 2.0'''
#getting number of rows and columns [positive numbers]
def row_col(name):
    while True:
        try:
            name=int(input(f"enter number of {name}(positive number) : "))        
            if(name<=0):
                raise ValueError('input should be positive number')
            return name
        except ValueError:
            print('invalid input, please enter a positive number')
#initialying the matrix 
def initialize_matrix(rows,columns):
    mat=[]
    for r in range(rows):
        v=[0]*columns
        mat.append(v)
    return mat        
#getting the value integers
def get_input_int(state):
    while True:
        try:
            v=int(input(state))
            return v
        except:
            print('invalid input, please enter integer ')
#filling the matrix with integers
def getting_matrix(mat,rows,columns):
    for r in range(rows):
        for c in range(columns):
            v=get_input_int(f"enter the value(integer) for position[{r}][{c}] : ")
            mat[r][c]=v
    return mat
#printing the matrix
def print_matrix(mat):
    for i in mat:
        print(i)    
#matrix addition
def matadd():
    row,col='row','col'

    row=row_col(row)
    col=row_col(col)
    
    mat1=initialize_matrix(row,col)    
    print('matrix 1  : ')
    mat1=getting_matrix(mat1,row,col) 
    print_matrix(mat1)
    
    mat2=initialize_matrix(row,col)
    print('matrix 2  : ') 
    mat2=getting_matrix(mat2,row,col)
    print_matrix(mat2)
       
    mat3=initialize_matrix(row,col)
    for r in range(row):
        for c in range(col):
            v=mat1[r][c]+mat2[r][c]
            mat3[r][c]=v
    print('resultant matrix after addition  : \n')
    print_matrix(mat3)
#matrix substraction
def matsub():
    row,col='row','col'
    row=row_col(row)
    col=row_col(col)
    
    mat1=initialize_matrix(row,col)
    print('matrix 1  : ')
    mat1=getting_matrix(mat1,row,col)
    print_matrix(mat1)

    mat2=initialize_matrix(row,col)
    print('matrix 2  : ')
    mat2=getting_matrix(mat2,row,col)
    print_matrix(mat2)
       
    mat3=initialize_matrix(row,col)
    for r in range(row):
        for c in range(col):
            v=mat1[r][c]-mat2[r][c]
            mat3[r][c]=v
    print('resultant matrix after addition  : \n')
    print_matrix(mat3)
#matrix multiplication   
def matmultiply():
    row = row_col("rows in matrix 1")
    rc = row_col("columns in matrix 1 or rows in matrix 2")
    col = row_col("columns in matrix 2")
    
    mat1=initialize_matrix(row,rc)
    mat2=initialize_matrix(rc,col)
    mat3=initialize_matrix(row,col)
    
    print('matrix 1  : ')   
    mat1=getting_matrix(mat1,row,rc)
    print_matrix(mat1)
    
    print('matrix 2  : ')   
    mat2=getting_matrix(mat2,rc,col)
    print_matrix(mat2)
           
    print(' matrix 3  : ')   
    for r in range(row):
        for c in range(col):
            for k in range(rc):
                mat3[r][c]+=mat1[r][k]*mat2[k][c]        
    print('resultant matrix after multiplication : ')
    print_matrix(mat3)

#main program
print("let us code mmmmmmmmmmmmmm...............")
print("       matrix solver version 2.0")

solving=True

while solving:
    print('''         
press 1 to add matrix
press 2 to subtract matrix
press 3 to multiplyn matrix
press x to exit
''')
    choice=input('enter your choice : ')
    if(choice=='1'):
        matadd()
    elif(choice=='2'):
        matsub()        
    elif(choice=='3'):
        matmultiply()    
    elif(choice.lower()=='x'):
        print('Exiting...')
        break
    else:
        print('invalid input . please try again')

    

    