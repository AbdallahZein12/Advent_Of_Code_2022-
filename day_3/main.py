
with open('part1.in','r') as file:
  count = 0
  lines = file.readlines()
  dict = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52}

  half1 = []
  half2 = [] 

  # for line in lines:
  #   length = len(line)
  #   half1.append(line[0:(length//2)-1])
  #   half2.append(line[(length//2)-1:])
  #   for i in range(len(half1)):
  #     for char1 in half1[i]:
  #       for char2 in half2[i]:
  #         if char1 == char2:
  #          count += dict[char1]

  for line in lines:
    length = len(line)
    half1 = set(line[0:(length//2)])
    half2 = set(line[(length//2):])
    
    for i in half1:
      for j in half2:
        if i == j:
          count += dict[i]


  # list1 = []
  # list2 = []

  # for element in half1:
  #   for char in element:
  #     list1.append(char)

  # for element in half2:
  #   for char in element:
  #     list2.append(char)


  # for element in list1:
  #   for element1 in list2:
  #     if element == element1:
  #       count += dict[element]
    


    

  

  # for i in range(len(half1) - 1):
  #   for char1 in half1[i]:
  #       for char2 in half2[i]:
  #         if char1 == char2:
  #          count += dict[char1]
      

  print(count)

  
  
  #---------------------PART 2-------------------------------------------------------

with open('part2.in','r') as file2:
  dict = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52}
  lines2 = file2.readlines()
  count2= 0
  l3 = ['','','']
  
  list_ = lines2
  counter3 = 3
  counter4 = 0
  def program(cc1,cc2):
    global counter3
    global counter4
    global count2
    l4 = []
    for i in range(cc1, len(list_), cc2):
    # do something with the next three items
      l3[0] = list_[i] 
      l3[1] = list_[i+1]
      l3[2] = list_[i+2]
      for char in l3[0]:
        l4.append(char)
      l4.remove('\n')
  
  
  
    
      
        
      for i in l4:
        for character in l3[1]:
          if character == i:
            real = i         
            for character1 in l3[2]:
              if character1 == real:
                count2 += dict[i]
                counter3 += 3
                counter4 += 3
                if counter3 > len(list_):
                  print(count2)
                  exit()
                else:
                  program(counter4,counter3)

    
             
        
      
        
            
        
    
      
      
    
      
    # # for item in l3[0][0]:
    # #   for item1 in l3[0][1]:
    # #     if item == item1:
    # #       count2 += dict(item)
    # #       count11 += 3 
    # #     else:
    # #       count11 += 3
        
          



  program(0,3)  
    
    
      
      
    

    
      
      


  
  

  

  
    
