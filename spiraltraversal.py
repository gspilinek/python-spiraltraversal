#written by gerald spilinek
#last updated 09/25/2021

#input rows, cols, matrix
#output a spiral traversal of said input matrix

def main():
    r=5 #rows
    c=20 #cols
    matrix = [ [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],
            [41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60], 
            [61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
            [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100] ]
    
    maxprints = r*c #num of items to print
    
    x = 0   #row index var 
    y = 0   #col index var
    
    rend = r-1  #where our end of row is
    rstart = 0  #where our start of row is
    cend = c-1  #where our end of col is
    cstart = 0  #where our start of col is
    
    counter = 0

    print(matrix[x][y],end=" ")
    counter +=1
    while counter < maxprints:
  
        while y < cend:#right
            y+=1
            print(matrix[x][y],end=" ")
            counter+=1
        
        rstart+=1  
        
        if counter >= maxprints:
            break
        
        while x < rend: #down
            x+=1
            print(matrix[x][y],end=" ")
            counter+=1  
            
        cend-=1
        
        if counter >= maxprints:
            break
        
        while y > cstart :#left
            y-=1
            print(matrix[x][y],end=" ")
            counter+=1
        
        rend-=1
        
        if counter >= maxprints:
            break
        
        while x > rstart: # up
            x-=1
            print(matrix[x][y],end=" ")
            counter+=1
       
        cstart+=1

    print()    

if __name__ == '__main__':
    main()
    
