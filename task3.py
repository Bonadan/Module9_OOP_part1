class Stadium:
    stadiums_list = []

    def __init__(self, name, date_of_opening, country, city, seating_capacity):
        self.name = name
        self.date_of_opening = date_of_opening
        self.country = country
        self.city = city
        self.seating_capacity = seating_capacity
        Stadium.stadiums_list.append(self)

    @classmethod
    def input_data(cls):
        name = input("Enter stadium's name: ")
        date_of_opening = input("Enter date of opening (YYYY-MM-DD): ")
        country = input("Enter country: ")
        city = input("Enter city: ")
        seating_capacity = int(input("Enter seating capacity: "))
        return cls(name, date_of_opening, country, city, seating_capacity)

    @classmethod
    def output_data(cls):
        print("Stadiums:")
        for stadium in cls.stadiums_list:
            print(f"Name: {stadium.name}, Date of opening: {stadium.date_of_opening}, Country: {stadium.country}, City: {stadium.city}, Seating capacity: {stadium.seating_capacity}")

stadium1 = Stadium.input_data()
stadium2 = Stadium.input_data()

Stadium.output_data()