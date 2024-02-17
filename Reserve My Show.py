import datetime  
global f
f = 0

def t_movie():
    global f
    f = f+1
    print("Select the Movie that you Prefer to Watch?")
    print("To Watch the Movie 'Jailer' - Press 1")
    print("To Watch the Movie 'Varisu' - Press 2")
    print("To Watch the Movie 'Thunivu' - Press 3")
    print("To Go back to the Previous Menu - Press 4 ")
    movie = int(input("Choose your Movie: "))
    print("______________________________________________________________________________________")
    if movie == 4:
        center()
        date()
        return 0
    if f == 1:
        date()
    else:
        print("Choose any of the movie from the above List")
        print("???????????????????????????????????????????????????????????????????????????????????????")
        t_movie()
    
def date():
    Date=input("Type the  Date on which you are intrested to watch the Movie? (in DD/MM/YYYY) ")  
    Moviedate=datetime.datetime.strptime(Date,"%d/%m/%Y").date()  
    print("Your Show date is "+Moviedate.strftime('%d/%B/%Y'))
    print("_________________________________________________________________________________________")
    theater()
    
def theater():
    print("which screen do you want to watch movie: ")
    print("To Watch Movie On SCREEN 1(RGB Laser Technology) - Press 1")
    print("To Watch Movie On SCREEN 2(4K Dolby Atmos) - Press 2")
    print("To Watch Movie On SCREEN 3(Dolby Atmos) - Press 3")
    a = int(input("choose your screen: "))
    print("______________________________________________________________________________________")
    timing(a)


    
def Seat():
    print("'A'- 'D' belongs to Platinum.")
    print("'E'- 'L' belongs to Diamaond.")
    print("'M'- 'O' belongs to Gold.")
    print("'P'- 'Q' belongs to Silver.")
    Seat_row=(input("Choose a Seat row  From 'A' to 'Q':"))
    Seat=Seat_row.upper()
    if Seat=='A':
        print("Price of Per Ticket in Row A is '₹ 200'")
    elif Seat=='B':
        print("Price of Per Ticket in Row B is '₹ 200'")
    elif Seat=='C':
        print("Price of Per Ticket in Row C is '₹ 200'")
    elif Seat=='D':
        print("Price of Per Ticket in Row D is '₹ 200'")
    elif Seat=='M':
        print("Price of Per Ticket in Row M is '₹ 150'")
    elif Seat=='N':
        print("Price of Per Ticket in Row N is '₹ 150'")
    elif Seat=='O':
        print("Price of Per Ticket in Row O is '₹ 150'")
    elif Seat == 'P':
        print("Price of Per Ticket in Row P is '₹120'")
    elif Seat == 'Q':
        print("Price of Per Ticket in Row Q is '₹120'")
    elif Seat == 'E':
        print("Price of Per Ticket in Row E is '₹ 180'")
    elif Seat == 'F':
        print("Price of Per Ticket in Row F is '₹ 180'")
    elif Seat == 'G':
        print("Price of Per Ticket in Row G is '₹ 180'")
    elif Seat == 'H':
        print("Price of Per Ticket in Row H is '₹ 180'")
    elif Seat == 'I':
        print("Price of Per Ticket in Row I is '₹ 180'")
    elif Seat == 'J':
        print("Price of Per Ticket in Row J is '₹ 180'")
    elif Seat == 'K':
        print("Price of Per Ticket in Row K is '₹ 180'")
    elif Seat == 'L':
        print("Price of Per Ticket in Row L is '₹ 180'")
    else:
        print("Enter a Row between A-Q")
        print("???????????????????????????????????????????????????????????????????????????????????????")
        Seat()
    print("______________________________________________________________________________________")
    ticket()
def ticket():    
    ticket = int(input("Enter the required Number of Tickets: "))
    print("______________________________________________________________________________________")
    confirmation(Mobile_Number,Email_id)
def timing(a):
    time1 = {"1": "10.00-1.00","2": "1.10-4.10","3": "4.20-7.20","4": "7.30-10.30"}
    time2 = {"1": "10.15-1.15","2": "1.25-4.25","3": "4.35-7.35","4": "7.45-10.45"}
    time3 = {"1": "10.30-1.30","2": "1.40-4.40","3": "4.50-7.50","4": "8.00-10.45"}
    if a == 1:
        print("choose your time:")
        print("Timing 1.",time1["1"])
        print("Timing 2.",time1["2"])
        print("Timing 3.",time1["3"])
        print("Timing 4.",time1["4"])
        t = input("select your time:")
        print("______________________________________________________________________________________")
    elif a == 2:
        print("choose your time:")
        print("Timing 1.",time2["1"])
        print("Timing 2.",time2["2"])
        print("Timing 3.",time2["3"])
        print("Timing 4.",time2["4"])
        t = input("select your time:")
        print("______________________________________________________________________________________")
    elif a == 3:
        print("choose your time:")
        print("Timing 1.",time3["1"])
        print("Timing 2.",time3["2"])
        print("Timing 3.",time3["3"])
        print("Timing 4.",time3["4"])
        t = input("select your time:")
        print("______________________________________________________________________________________")
    Seat()
    return 0


def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("Choose any of the Screen Only from the above list")
        print("???????????????????????????????????????????????????????????????????????????????????????")

def center():
    print("Select The Theatre in Which You are interested to watch the Movie")
    print("To Watch in PVR Cinemas -Press 1")
    print("To Watch in Carnival Cinemas- Press 2")
    print("To Watch in INOX- Press 3")
    print("To Go Back to the Previous Menu- Press 4")
    a = int(input("choose your option: "))
    print("______________________________________________________________________________________")
    movie(a)
    return 0

def city():

    print("Select your Locality:")
    print("For Chennai - Press 1")
    print("For Coimbatore - Press 2")
    print("For Dindigul - Press 3")
    place = int(input("choose your option: "))
    if place == 1:
        print("______________________________________________________________________________________")
        center()
    elif place == 2:
        print("______________________________________________________________________________________")
        center()
    elif place == 3:
        print("______________________________________________________________________________________")
        center()
    else:
        print("Choose a city only from the above mentioned list")
        print("???????????????????????????????????????????????????????????????????????????????????????")
        city() 
def first():
    city()
def confirmation(Mobile_Number,Email_id):
    print("The Prefered Seat is found and Reserved for you")
    print("______________________________________________________________________________________")
    print("The confirmation of your Ticket is sent to your Mobile (",Mobile_Number, ")")
    print("and to your Mail ID(",Email_id,")")
    print('Thank you for Using "Reserve My Show" Service for Booking your Movie Ticket.')
    print("Vist us again ")
    print("______________________________________________________________________________________")
    final()
def final():
    print("To Continue - Press 1")
    print("To Exit -Press 2")
    final=int(input())
    if final == 1:
        print("")
        print("")
        print("______________________________________________________________________________________")
        print("")
        print("")
        first()

print("'Reserve My Show' Gladly Welcomes You for booking" )
Mobile_Number=int(input("Enter Your Mobile Number:"))
Email_id=input("Enter your Email Id:")
first()


