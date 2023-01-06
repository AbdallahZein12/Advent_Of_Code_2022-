with open('day4.in') as file:
    # def ranger(min,max,list):
    #     for i in range(min,max):
    #         return list.append(i)
    
    count = 0
    count2 = 0
    lines = file.readlines()
    line_list = ['','']
    for line in lines:
        r1 = []
        r2 = []
        
        splitter = line.index(',')

        pt1 = line[:splitter]
        pt2 = line[splitter+1:]
        
        splitter_ = pt1.index('-')

        p1_ = pt1[:splitter_]
        p2_ = pt1[splitter_+1:]

        splitter__ = pt2.index('-')

        p1__ = pt2[:splitter__]
        p2__ = pt2[splitter__+1:]

    
        for i in range(int(p1_),int(p2_)+1):
            r1.append(i)
        
        for y in range(int(p1__),int(p2__)+1):
            r2.append(y)
        

        if all(x in r2 for x in r1) or all(x in r1 for x in r2):
            count += 1 
        
        for i in r2:
            if i in r1:
                count2 += 1 
                break

    # for line in lines:
    #     par2_r1 = []
    #     par2_r2 = []
        
    #     par2_splitter = line.index(',')

    #     par2_pt1 = line[:par2_splitter]
    #     par2_pt2 = line[par2_splitter+1:]
        
    #     par2_splitter_ = par2_pt1.index('-')

    #     par2_p1_ = par2_pt1[:par2_splitter_]
    #     par2_p2_ = par2_pt1[par2_splitter_+1:]

    #     par2_splitter__ = par2_pt2.index('-')

    #     par2_p1__ = par2_pt2[:par2_splitter__]
    #     par2_p2__ = par2_pt2[par2_splitter__+1:]

    
    #     for i in range(int(par2_p1_),int(par2_p2_)+1):
    #         par2_r1.append(i)
        
    #     for y in range(int(par2_p1__),int(par2_p2__)+1):
    #         par2_r2.append(y)
        

    #     for i in par2_r2:
    #         if i in par2_r1:
    #             count2 += 1

            
        



    print(count)
    print(count2)




        




        
        

