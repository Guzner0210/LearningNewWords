import sqlite3
import random

def main():
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
        oo = input("Do you want to insert more words? [Y/n] ").lower().strip()
        if oo == "y" or oo == "yes":
            continue
        else:
            switch = False
            print("Goodbye")

def take_a_quiz():
    score = 0
    number_of_question = 0
    switc = True
    while switc:
        spawn_a_question()
        your_answer_is = input("The word is: ")
        if your_answer_is == the_answer_is:
            score += 1
            number_of_question += 1
            print("That's correct!")
        else:
            number_of_question += 1
            print("Sorry, you're wrong!")

        iii = input("Do you want to keep continue? [Y/n] ").lower().strip()
        if iii == "y" or iii == "yes":
            continue
        else:
            break

    print("Your score is: " + str((score/number_of_question)*100) +"%")


def spawn_a_question():
    db = sqlite3.connect("db'.sqlite3")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM new_words')
    all_rows = cursor.fetchall()
    all_meanings = []
    all_words = []
    for row in all_rows:
        index, word, meaning = row
        all_meanings.append(meaning)
        all_words.append(word)

    a_rando = random.randint(0, len(all_meanings) - 1)
    global the_answer_is
    the_answer_is = all_words[a_rando]
    print(all_meanings[a_rando])


if __name__ == "__main__":
    main()
