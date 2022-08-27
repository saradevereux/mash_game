import json
import json
import random


with open("mash.json") as mash_data:
    data = json.load(mash_data)
    question_bank = []
    for question in data["survey"][0]["question"]:
        print(question)

def play(mash):
    fortune = {}
    #Spiral function
    print("\nIs it a kind of wild that your entire future comes down to a randomly generated number?")
    print("That seems a little high stakes...")
    print("...anyways..")
    input("Press ENTER to determine your N.O.D. (Number of Destiny)")
    rand_num = random.randint(2, 12)
    print("\nYour N.O.D. (Number of Destiny) is:", rand_num)
    finished = False
    all_cats = list(mash.keys()) #creates list of categories
    #create pointer to move through keys and values 
    pointer = {"point_cat":0,"point_idx":0} #iterator starts at 0
    counter = rand_num - 1 #account for 0 index
    while not finished:
        pc = pointer["point_cat"] #points to key
        pi = pointer["point_idx"] #points to index of list value in key
        current_list = mash[all_cats[pc]] #current value list being iterated through
        rem = len(current_list) - pi #items remaining in list after where the pointer is pointing
        if counter < rem:
            pointer["point_idx"] += counter #move the pointer
            mash[all_cats[pc]].pop(pointer['point_idx']) #removes current category option
        #if current category has 1 item left, pop category and return to fortune dictionary
            if len(mash[all_cats[pc]]) == 1:
                fortune[all_cats[pc]] = mash[all_cats[pc]][0]
            #removes category from master list of categories
                del mash[all_cats[pc]] #removes category from mash dictionary
                all_cats.pop(pc) #removes category from list of categories
                if len(all_cats)!=0:
                    pointer['point_idx'] = 0
                    pointer['point_cat'] = modul(pc,len(all_cats))
            counter = rand_num - 1
        else: #counter >= rem
            counter -= rem
            pointer['point_cat'] = skip_cat(pc,len(all_cats))
            pointer['point_idx'] = 0
        finished = len(mash.keys()) == 0
    return fortune
#function to reset pointer when category doesnt have enough items to iterate through
def skip_cat(point_cat, total_cats):
    return (point_cat+1)%total_cats

#function to determine modulus to reset pointer at end of list
def modul(x,y):
    mod = x%y
    if mod<0:
        mod+=y
    return mod

#Game play
print("\nWelcome to the game of MASH")
print("The same game you played as a wide-eyed optimistic child has been modernized and automated so your friend Jenny doesn't screw up counting again!")
print("\nAnswer a few simple questions and all your questions about what do do with your life, \nwho is your eternal love, and \njust how filthy rich you will be, \ncan be answered!")
print("Are you ready to make the uknown, known?")
while True:   
    to_play = input("[y/N]  ").lower()
    if to_play == "y":
        print("We've gathered all the information we need....there's no turning back now. \nYour destiny is just one button push away")
        print("Press ENTER to reveal your destiny")
        destiny = play(mash)
        print("\nHere it is! Your actual True Destiny, hope its everything you ever dreamed of:")
        print("You will live in a:", destiny["live"])
        print("Your mode of transportation with be:", destiny["transportation"])
        print("Your career will be:", destiny["career"])
        print("Your yearly income will be:", destiny["salary"])
        print("You will live in:", destiny["location"])
        print("You'll marry:", destiny["partner"])
        print("For a pet, you'll have a", destiny["pet"])
        print("The number of kids you'll have:", destiny["kids"])
        print("\nDoesn't sound so hot? \nYou could always play again.")
        while True:
            play_again = input("[y/N]").lower()
            if play_again == "y":
                break
            elif play_again == "n":
                exit()
            else:
                print("Please enter a valid option: [y/N]")
    elif to_play == "n":
        exit()
    else:
        print("Please enter a valid option: [y/N]")