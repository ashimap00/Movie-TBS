choice=0
loc=0
st=0
no=0
a=0
b=0
m=0
print("           A TICKET INTO THE REEL WORLD IN BANGALORE")
l=["1. HINDI","2. ENGLISH","3. TAMIL","4. KANNADA","5. TELEGU"]
l2=["1. KORAMANGALA- FORUM MALL","2. MARATHALLI- INNOVATIVE MULTIPLEX","3. WHITEFIELD- CINEPOLIS","4. BANNERGHATTA ROAD- GOPALAN MALL"]
t=["1. 11am","2. 2:30pm","3. 7:30pm"]
tel=["1.RRR","2.RADHE SHYAM","3.PUSHPA"]
hin=["1. KASHMIR FILES","2. GANGUBAI KATHIAWADI","3. BACHCHAN PANDEY"]
eng=["1.THE BATMAN","2.SPIDERMAN NO WAY HOME","3. KING RICHARD"]
kan=["1.KGF","2.JAMES","3.LOVE MOCKTAIL 2"]
tal=["1.BEAST","2.VALIMAI","3.MAHAN"]
for i in l:
    print(i)
print()
lang=int(input("ENTER LANGUAGE PREFERANCE:  "))
def time(loc):
    for i in t:
        print(i)
    tt=int(input("ENTER THE PREFERRED TIMINGS:  "))
    seat(tt)
def seat(l):
    print("-----CLASSIC - Rs. 300-----")
    no=int(input("ENTER THE NUMBER OF SEATS REQUIRED"))
    a=int(input("ENTER THE NUMBER OF ADULTS"))
    b=int(input("ENTER THE NUMBER OF KIDS BELOW 5 YEARS"))
    if(no==(a+b)):
        print("CONFIRM AND PROCEED TO PAYMENT")
        print("1. YES")
        print("2. NO")
        c=int(input("ENTER TO PROCEED:  "))
        if (c==1):
            m=(a*300+b*150)
            print("AMOUNT:",m)
        else:
            print("***********THANK YOU.  HOPE TO SEE YOU SOON*************")
    else:
         print("WRONG ENTRY")
def movie(ch):
    print("LOCATIONS AVAILABLE:  ")
    for j in l2:
        print(j)
    print()
    loc=int(input(" ENTER THE PREFERRED LOCATION:  "))
    time(loc)
    print()
   
   
if(lang==1):
    print("PRESENTING YOU A SNEEK PEAK TO BOLLYWOOD LATESTS:  ")
    for i in hin:
        print (i)
    choice=int(input("ENTER THE MOVIE YOU WISH TO WATCH:  "))
    movie(choice)
    print()
elif(lang==2):
    print("PRESENTING YOU A SNEEK PEAK TO HOLLYWOOD LATESTS:  ")
    for i in eng:
        print (i)
    choice=int(input("ENTER THE MOVIE YOU WISH TO WATCH:  "))
    movie(choice)
    print()
elif(lang==3):
    print("PRESENTING YOU A SNEEK PEAK TO KOLLYWOOD LATESTS:  ")
    for i in tal:
        print (i)
    choice=int(input("ENTER THE MOVIE YOU WISH TO WATCH:  "))
    movie(choice)
    print()
elif(lang==4):
    print("PRESENTING YOU A SNEEK PEAK TO SANDALWOOD LATESTS:  ")
    for i in kan:
        print (i)
    choice=int(input("ENTER THE MOVIE YOU WISH TO WATCH:  "))
    movie(choice)
    print()
elif(lang==5):
    print("PRESENTING YOU A SNEEK PEAK TO TOLLYWOOD LATESTS:  ")
    for i in tel:
        print (i)
    choice=int(input("ENTER THE MOVIE YOU WISH TO WATCH:   "))
    movie(choice)
    print()
seats=[['a1','a2','a3'],
       ['b1','b2','b3'],
       ['c1','c2','c3']]

book=[[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

print('Seat numbering:')
for i in range(len(seats)):
    for j in range(len(seats[i])):
        print(seats[i][j], end='  ')
    print('\n')
    
while True:
    opt=int(input('''
Pick an option:
1) Book a seat
2) Cancel a booking
3) View available seats
4) Exit

'''))

    if opt==1:
        ch=input('Enter seat number to book: ')
        
        e=0
        for a in seats:
            if ch in a:
                e=1
        if e==1:
            for i in range(len(seats)):
                for j in range(len(seats[i])):
                    if ch==seats[i][j]:
                        book[i][j]=ch
                        print('\nBooking successful')
        else:
            print('\nSeat not found')
            
    elif opt==2:
        ch=input('Enter seat number to cancel: ')

        e=0
        for a in seats:
            if ch in a:
                e=1
                for a in book:
                    if ch in a:
                        e=2
                    
        if e==1:
            print('\nSeat not booked')
            
        elif e==2:
            for i in range(len(seats)):
                for j in range(len(seats[i])):
                    if ch==seats[i][j]:
                        book[i][j]=0
                        print('\nSeat cancelled')
            
        else:
            print('\nSeat not found')

    elif opt==3:
        print()
        for i in range(len(book)):
            for j in range(len(book[i])):
                if book[i][j]==seats[i][j]:
                    print(book[i][j], end=' ')
                else:
                    print(book[i][j], end='  ')
            print('\n')

    elif opt==4:
        break

    else:
        print('\nInvalid option')



