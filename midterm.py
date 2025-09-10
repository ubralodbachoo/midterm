#1
library = [
    {"title": "მე ბებია ილიკო და ილარიონი", "author": "ნოდარ დუმაბძე", "year": 1900},
    {"title": "ჩრდილოეთის ციალი", "author": "პულმანი", "year": 1900},
    {"title": "1984", "author": "ჯორჯ ორუელი", "year": 1900},
    {"title": "კაცია ადამიანი", "author": "ილია ჭავჭავაძე", "year": 1800},
    {"title": "ასტრალის სული", "author": "ნიკოლოზ ტოტოღაშვილი", "year": 1800},
    {"title": "ქარვის ჭოგრიტი", "author": "პულმანი", "year": 1800},
    {"title": "სამოსელი პირველი", "author": "დოჩანაშვილი", "year": 1900},
    {"title": "დანაშაული და სასჯელი", "author": "დოსტოევსკი", "year": 1800},
    {"title": "გამზრდელი", "author": "აკაკი წერეთელი", "year": 1951},
    {"title": "ვეფხისტყაოსანი", "author": "შოთა რუსთველი", "year": 1232},
]

def show_menu():
    print("1. წიგნების ნახვა")
    print("2. წიგნის დამატება")
    print("3. წიგნის ძებნა სათაურით")
    print("4. წიგნის წაღება ")
    print("5. გამოსვლა")

def show_books():
    if not library:
        print("ბიბლიოთეკა ცარიელია.")
    else:
        for i, book in enumerate(library, 1):
            print(f"{i}. {book['title']} - {book['author']} ({book['year']})")

# ახალი წიგნის დამატება
def add_book():
    title = input("შეიყვანეთ წიგნის სახელი: ")
    author = input("შეიყვანეთ ავტორი: ")
    year = int(input("შეიყვანეთ გამოსვლის წელი: "))
    library.append({"title": title, "author": author, "year": year})
    print(f"'{title}' დამატებულია ბიბლიოთეკაში!")

def search_book():
    title = input("შეიყვანეთ სათაური საძიებლად: ")
    for book in library:
        if book["title"]== title:
            print(f"{book['title']} - {book['author']} ({book['year']})")
            return None
    print("ასეთი წიგნი ვერ მოიძებნა.")

#წაღება წიგნის
def borrow_book():
    show_books()
    choice = int(input("აირჩიეთ წიგნის ნომერი წასაღებად: "))
    if 1 <= choice <= len(library):
        book = library.pop(choice - 1)
        print(f"თქვენ წაიღეთ: {book['title']} ავტორი: {book['author']}")
    else:
        print("არასწორი არჩევანი!")

def main():
    while True:
        show_menu()
        choice = input("აირჩიეთ ოპცია: ")
        if choice == "1":
            show_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            break
        else:
            print("სცადეთ თავიდან.")

main()

#2
import random

suits = ["ყვავი", "ჯვარი", "გული", "აგური"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

# დასტის შექმნა
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

# ქულების დათვლა
def calculate_score(i):
    score = 0
    for card in i:
        score += values[card[0]]
    return score

# თამაშის მთავარი ლოგიკა
def play_game():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    computer_hand = [deck.pop(), deck.pop()]

    while True:
        player_score = calculate_score(player_hand)
        print("\nთქვენი კარტები:", player_hand, "ქულა:", player_score)
        print("კომპიუტერის პირველი კარტი:", computer_hand[0])

        if player_score > 21:
            print("თქვენ წააგეთ! გადააჭარბეთ 21-ს.")
            return

        choice = input("კარტის დამატება - 'add' თუ არ გნებავთ - 'stop'? ")
        if choice == "add":
            player_hand.append(deck.pop())
        elif choice == "stop":
            break

    while calculate_score(computer_hand) < 17:
        computer_hand.append(deck.pop())

    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    print("თქვენი კარტები:", player_hand, "ქულა:", player_score)
    print("კომპიუტერის კარტები:", computer_hand, "ქულა:", computer_score)

    # გამარჯვებული
    if computer_score > 21 or (player_score <= 21 and player_score > computer_score):
        print("თქვენ მოიგეთ!")
    elif player_score == computer_score:
        print("ფრე!")
        play_game()
    else:
        print("თქვენ წააგეთ!")


play_game()

#3

from base64 import encode
import logging
logging.basicConfig(
    filename="atm.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)
balance  = 1000
def balance_show():
    print(f"შენი ბალანის შეადგენს {balance}")
def deposit():
    global balance
    amnt = int(input("შეიტანე თანხა, თანხა არ უნდა იყოს 1000ლ ზე მეტი: "))
    if amnt > 1000:
        print("ერთად 1000ლ ზე მეტს ვერ შეიტანთ")
    else:
        balance += amnt
        print(f"თქვენ ჩაგერიცხათ {amnt} ლარი")
        logging.info(f"თქვენ ჩაგერიცხათ {amnt} ლარი")

def withdraw():
    global balance
    amount = int(input("რამდენის გატანა გსურთ? "))
    if amount > balance:
        print("თქვენს ანგარიშზე საკმარისი თანხა არ არის.")
    else:
        balance -= amount
        print(f"თქვენ ჩაგერიცხათ {amount} ლარი")
        logging.info(f"{amount} ლარი წარმატებით გაიტანეთ. ახალი ბალანსი: {balance} ლარი")

def main():
    while True:
        print("1. ბალანსის ნახვა")
        print("2. თანხის შეტანა")
        print("3. თანხის გამოტანა")
        print("4. გამოსვლა")

        choice1 = input("გააკეთე არჩევანი: ")

        if choice1 == "1":
            balance_show()
        elif choice1 == "2":
            deposit()
        elif choice1 == "3":
            withdraw()
        elif choice1 =="4":
            break
    
main()

#4
import random
import logging

logging.basicConfig(
    filename="lotto_log.txt",
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

jackpot = 5000

def play_lotto():
    computer_numbers = random.sample(range(1, 50), 6)

    player_numbers = []
    print("შეიყვანეთ 6 რიცხვი 1-დან 50-მდე:")
    for i in range(6):
        num = int(input(f"{i+1}-ე რიცხვი: "))
        player_numbers.append(num)

    # დამთხვევების დათვლა
    matches = len(set(player_numbers) & set(computer_numbers))
    prize, result_text = calculate_prize(matches)


    print("\n--- შედეგები ---")
    print(f"კომპიუტერის რიცხვები: {computer_numbers}")
    print(f"თქვენი რიცხვები:      {player_numbers}")
    print(f"დამთხვევა: {matches}/6")
    print(f"შედეგი: {result_text}")
    if prize > 0:
        print(f"მოგებული თანხა: {int(prize)} ლარი")
    else:
        print("სამწუხაროდ ვერ მოიგეთ.")

    # ლოგში ჩაწერა
    logging.info(
        f"კომპიუტერი: {computer_numbers} --- მოთამაშე: {player_numbers} | "
        f"დამთხვევა: {matches}/6 | {result_text} | მოგება: {int(prize)} ლარი"
    )

def calculate_prize(matches):
    if matches == 6:
        return jackpot, "JACKPOT"
    elif matches == 5:
        return jackpot * 0.6,
    elif matches == 4:
        return jackpot * 0.4,
    elif matches == 3:
        return jackpot * 0.2,
    else:
        return 0, 
play_lotto()

#5
user_data = {
    "email": "bachomirza@gmail.com",
    "username": "ubralodbacho",
    "password": "bachomagali1234"
}

def register_name():

    name = input("შეიყვანეთ სახელი: ")
    if name.isdigit():
        print("შემოყვანილია რიცხვითი მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")
        return
    elif all(not ch.isalnum() for ch in name):
        print("შემოყვანილია სიმბოლოები, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")
        return
    elif not all(ord(ch) < 128 for ch in name):
        print("შემოყვანილია სხვა ენა, გამოიყენეთ მხოლოდ ლათინური პატარა ასოები")
        return
    elif not name.islower():
        print("სახელი უნდა იყოს მხოლოდ პატარა ლათინური ასოებით")
        return
    user_data["name"] = name
    print("რეგისტრაცია წარმატებით დასრულდა!")
    print("მომხმარებლის მონაცემები:")
    for k, v in user_data.items():
        print(f"{k}: {v}")


register_name()


