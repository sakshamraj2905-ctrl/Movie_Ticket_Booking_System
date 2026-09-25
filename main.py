booking_id = 1001
bookings = []
seats = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5",
    "D1", "D2", "D3", "D4", "D5",
    "E1", "E2", "E3", "E4", "E5",
    "F1", "F2", "F3", "F4", "F5",
    "G1", "G2", "G3", "G4", "G5",
    "H1", "H2", "H3", "H4", "H5"
]

movies = [
    {
        "name": "Spider-Man: Brand New Day",
        "language": "English",
        "price": 300,
        "format": "3D",
        "shows": ["12:00 PM", "3:00 PM", "6:00 PM"]
    },
    {
        "name": "Hanuman Ansh",
        "language": "Hindi",
        "price": 250,
        "format": "2D",
        "shows": ["11:00 AM", "2:00 PM", "7:00 PM"]
    },
    {
        "name": "The Vvaan",
        "language": "Hindi",
        "price": 250,
        "format": "2D",
        "shows": ["10:00 AM", "1:00 PM", "5:00 PM"]
    },
    {
        "name": "The Paradise",
        "language": ["Hindi", "Tamil", "Telugu"],
        "price":300,
        "format": "3D",
        "shows": ["9:00 AM", "12:30 PM", "6:30 PM"]

    },
    {
        "name": "Avengers(Endgame)",
        "language": "English",
        "price": 350,
        "format": "3D",
        "shows": ["8:00 AM", "1:30 PM", "8:00 PM"]
    }
]
      
                              
print("==============================")
print("MOVIE TICKET BOOKING SYSTEM")
print("==============================")
print("Welcome to this system!")

while True:
    print("\n1. View Movies")
    print("2. View Show Timings")
    print("3. View available seats")
    print("4. Book Ticket")
    print("5. Cancel Ticket")
    print("6. View Booking")
    print("7. Exit")

    choice = input("\nEnter your preferred choice: ")

    if choice == "1":
        print("\nAvailable Movies:")
        number = 1

        for movie in movies:
            print(str(number) + ") Movie:"+ movie["name"])
            print("Languages available:", movie["language"])
            print("Ticket price: Rs.",movie["price"])
            print("Format of movie:", movie["format"])
            print()
            print()
            number = number +1
        print("----------------------------")        
    elif choice == "2":
        print("\nShow Timings:\n")
        number = 1
        for movie in movies:
            print(str(number) + ") " + movie["name"])
            for show in movie["shows"]:
                print("    - " + show)
                print()
                print()
            number = number + 1

    elif choice == "3":
        print("\nAvailable Seats: \n")
        for seat in seats:
            print(seat, end= "  ")
            if seat[1] == "5":
                print()
                print()
    elif choice =="4":

        print("\n--- Book Ticket---" )
        name = input("Please Enter your name: ")
        print("\nWelcome,", name + "!")
        print("Let's book your movie ticket!! ")
        print("\nSelect a movie:")
        number = 1
        for movie in movies:
            print(str(number) + ") Movie: " + movie["name"])
            number = number + 1  

        movie_choice = int(input("\nEnter Movie number:"))     
        selected_movie = movies[movie_choice - 1]
        print("\nYou Selected:", selected_movie["name"]) 
        print("\nAvailable Shows:")
        number = 1
        for show in selected_movie["shows"]:
            print(str(number) + ") " + show)
            number = number + 1
        show_choice = int(input("\nPlease enter show number:"))
        selected_show = selected_movie["shows"][show_choice - 1]
        print("\nYou selected:", selected_show)

        print("\nAvailable seats: \n")
        for seat in seats:
            print(seat, end = "  ")
            if seat[1] == "5":
                print()
                print()

        number_of_tickets = int(input("\nHow many tickets do you want? "))
        print("\nSelect your seats: ")
        selected_seats = []

        for i in range(number_of_tickets):
            selected_seat = input("Enter seat " + str(i + 1) + ": ")

            if selected_seat not in seats:
                print("Sorry! This seat is not available.")
                continue

            selected_seats.append(selected_seat)

        print("\nYou selected seats:", ", ".join(selected_seats))
        print("\n=========================")
        print("   TICKET CONFIRMED     ")
        print("=========================")

        print("Name: ", name)
        print("Movie: ", selected_movie["name"])
        print("Show:", selected_show)
        print("Seats:", ", ".join(selected_seats))
        print("Price:", selected_movie["price"])
        print("Booking ID:", booking_id)
        total_price = selected_movie["price"] * number_of_tickets

        bookings.append({
            "booking_id": booking_id,
            "name": name,
            "movie": selected_movie["name"],
            "show": selected_show,
            "seats": selected_seats,
            "price": selected_movie["price"],
            "number_of_tickets": number_of_tickets,
            "total_price": total_price
        })

        for seat in selected_seats:
            if seat in seats:
                seats.remove(seat)
        booking_id += 1

        print("\nCongrats, your ticket has been booked sucessfully!!")


    elif choice == "5":
        print("\n--- Cancel Ticket ---")

        cancel_id = int(input("Enter Booking ID: "))

        found = False

        for booking in bookings[:]:
            if booking["booking_id"] == cancel_id:
                found = True

                print("\nBooking found!")
                print("Name:", booking["name"])
                print("Movie:", booking["movie"])
                print("Show:", booking["show"])
                print("Seats:", ", ".join(booking["seats"]))

                for seat in booking["seats"]:
                    if seat not in seats:
                        seats.append(seat)

                bookings.remove(booking)
                print("\nTicket cancelled successfully!")
                break

        if found == False:
            print("Booking ID not found!")

    elif choice == "6":
        print("\n--- View Booking ---")
        if len(bookings) == 0:
            print("No bookings found.")
        else:
            for booking in bookings:
                print("\n------------------------")
                print("Booking ID:", booking["booking_id"])
                print("Name:", booking["name"])
                print("Movie:", booking["movie"])
                print("Show:", booking["show"])
                print("Seats:", ", ".join(booking["seats"]))
                print("Price per ticket: Rs.", booking["price"])
                print("Number of tickets: ", booking["number_of_tickets"])
                print("Total Price: ", booking["total_price"])
                print("------------------------")
    elif choice == "7":
        print("THANK YOU FOR USING OUR SYSTEM! ")
        break
    else:
        print("Invalid Choice!! Please Try Again!!")
        