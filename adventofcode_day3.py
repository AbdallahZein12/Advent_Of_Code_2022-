
with open('day1.in','r') as file:
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
      

    
      
      


  
  

  

  
    