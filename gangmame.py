from random import *
while True:
    print("                   welcome player 1")
    print("1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20")
    n1p1=int(input("enter your first choise :"))
    paper=['' ,'A','B','C','D','E','F','G','H','I','J','H','I','J','A','B','C','D','E','F','G']
    shuffle(paper)
    numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    score1=0
    scores=0
    scorep=0
    firstp1=int(n1p1)
    firstp1=paper[n1p1]
    if n1p1<20:
            numbers.remove(n1p1)
            numbers.insert(n1p1,firstp1)
            print(numbers)
    paper_new=['' ,'A','B','C','D','E','F','G','H','I','J','H','I','J','A','B','C','D','E','F','G']
    shuffle(paper_new)
    numbersl=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    n2p1=int(input("enter your secound choise :"))
    scd=int(n2p1)
    scd=paper_new[n2p1]
    if n2p1<20 and n2p1!=n1p1:
            numbersl.remove(n2p1)
            numbersl.insert(n2p1,scd)
            print(numbersl)
            print("                                                                                                                                                                                                                                                                                                                                                                                                       
    for i in numbers:
       for c in paper:
           if c==i:
               scores=scores+1
               print('score player1=: ',score1)
    for b in numbersl:
        for x in paper:
           if x==b:
               scorep=scorep+1
               score=scorep+scores
               print('score player1=: ',score)
    else:
        print("                   welcome player 2")
        print("1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20")
        n1p2=int(input("enter your first choise :"))
        paper_player2=['' ,'A','B','C','D','E','F','G','H','I','J','H','I','J','A','B','C','D','E','F','G']
        shuffle(paper_player2)
        numbers_player2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        firstp2=int(n1p2)
        firstp2=paper[n1p2]
        scoreplayer2=0
        scores2=0
        scorep2=0          
        if n1p2<20:
             numbers_player2.remove(n1p1)
             numbers_player2.insert(n1p2,firstp2)
             print(numbers_player2)
        paper_new2=['' ,'A','B','C','D','E','F','G','H','I','J','H','I','J','A','B','C','D','E','F','G']
        shuffle(paper_new2)
        numbersl2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        n2p2=int(input("enter your secound choise :"))
        scd2=int(n2p1)
        scd2=paper_new2[n2p1]
        if n2p1<20 and n2p2!=n1p2:
            numbersl2.remove(n2p2)
            numbersl.insert(n2p1,scd2)
            print(numbersl2)
        for j in numbers_player2:
           for k in paper_player2:
               if k==j:
                   scores2=scores2+1
        for g in numbersl2:
            for h in paper_new2:
               if g==h:
               scorep2=scorep2+1
               scoreplayer2=scorep2+scores2
               print('score player1=: ',scoreplayer2)
#(h,g,j,k,x,b,i,c)is counters
