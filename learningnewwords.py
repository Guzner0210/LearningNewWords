import sqlite3

def main_board():
    print("You have 2 options: \n")
    print("1.) Add a new word \n")
    print("2.) Take a quiz \n")
    answer = input("Choose: \n")

    if answer == "1":
        new_word()
    elif answer == "2":
        take_a_quiz()
    else:
        print("Sorry, I don't understand what you want.")

def new_word():
    switch = True

    while(switch):
        db = sqlite3.connect("db'.sqlite3")
        cursor = db.cursor()

        create_new_word = input("New word: ").strip()

        its_meaning = input("Its meaning: ").strip()

        # cursor.execute('''CREATE TABLE IF NOT EXISTS new_words(
        #                 id integer PRIMARY KEY,
        #                 new_word text NOT NULL UNIQUE,
        #                 its_meaning text NOT NULL);''')
        cursor.execute('''INSERT INTO new_words(new_word, its_meaning)
                    VALUES(?,?)''', (create_new_word, its_meaning))
        db.commit()
        db.close()
        oo = input("Do you want to insert more words? [Y/n] ").lower()
        if oo == "y" or oo == "yes":
            continue
        else:
            switch = False
            print("Goodbye")

def take_a_quiz():
    pass

if __name__ == "__main__":
    main_board()
