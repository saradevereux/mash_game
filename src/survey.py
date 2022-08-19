
class SurveyMetadataSchema:
    def __init__(self) -> None:
        pass

    class MashCategory(SurveyMetadataSchema):


def choices():
    mash = {"live": ["Mansion", "Apartment", "Shack", "House"]}
# Transportation
    mash["transportation"] = []
# TQ-1
    while True:
        print("\nHow did you get to school when you were little?")
        print("A) Big yellow school bus")
        print("B) Rode your bike")
        print("C) Backseat of your mom's minivan")
        print("D) Walked...uphill..both ways...in the snow")
        trans_a = input("Answer:  ").lower()
        if trans_a == "a":
            trans_a = "Your cousin's old Honda, but it's got an aftermarket spoiler, so it's pretty sweet."
            break
        elif trans_a == "b":
            trans_a = "A Harly Davidson, you would rather die than be a cager!"
            break
        elif trans_a == "c":
            trans_a = "Subaru Forester, the safety record is simply impeccable."
            break
        elif trans_a == "d":
            trans_a = "Ford F-150. Haul stuff? No. But you could if you needed to!"
            break
        else:
            print("Please answer: A, B, C, or D")
    mash["transportation"].append(trans_a)
# TQ-2
    print("\nWhat was your dream car as a teenager? ")
    trans_b = input("Answer: ")
    trans_b += ", dreams really do come true!!"
    mash["transportation"].append(trans_b)
# TQ-3
    print("\nWhat was your first car?")
    trans_c = input("Answer:  ")
    trans_c += ", maybe you can tell people it's an antique."
    mash["transportation"].append(trans_c)
# TQ-4
    print("\nName a type of public transportation")
    trans_d = input("Answer: ")
    trans_d += ", if you put in headphones and breathe through your mouth, it's not so bad."
    mash["transportation"].append(trans_d)
# TQ-5
    while True:
        print("\nHow do you get to work?")
        print("A) Walk, when the weather allows for it")
        print("B) Drive, obviously")
        print("C) Bike, you also recycle in case anyone was wondering")
        print("D) Public transportation, putting your tax dollars to work")
        trans_e = input("Answer:  ").lower()
        if trans_e == "a":
            trans_e = "An E-bike, its great for getting around town...unless a tourist takes it thinking its part of the city bike share."
            break
        elif trans_e == "b":
            trans_e = "A luxury sedan, but it has sport mode for when you feel spunky"
            break
        elif trans_e == "c":
            trans_e = "The fixie you built from spare parts during your volunteer hours at the community Gear Hub"
            break
        elif trans_e == "d":
            trans_e = "In the age of Uber, who needs a car!"
            break
        else:
            print("Please answer: A, B, C, or D")
    mash["transportation"].append(trans_c)

# Career
    mash["career"] = []
# CQ-1
    while True:
        print("\nHow do you unwind at home?")
        print("A) Watch TV?")
        print("B) Tidying up")
        print("C) Cooking and baking")
        print("D) Crafting")
        job_a = input("Answer:  ").lower()
        if job_a == "a":
            job_a = "Showbiz, baby! Small screens, big screens you're on them all!"
            break
        elif job_a == "b":
            job_a = "Watch out Marie Kondo, you're sparking joy all around you, while building your organization empire!"
            break
        elif job_a == "c":
            job_a = "You left the corporate world to enter the wild west of restaurateuring, how hard could it be?"
            break
        elif job_a == "d":
            job_a = "Right now, you're between jobs... you're focusing your efforts more on manifesting rather than actively looking."
            break
        else:
            print("Please answer: A, B, C, or D")
    mash["career"].append(job_a)
# CQ-2
    print("\nWhat is your current job?")
    job_b = input("Answer:  ")
    job_b += ", you've always considered yourself a company man."
    mash["career"].append(job_b)
# CQ-3
    print("\nWhat did you want to be when you grew up?  ")
    job_c = input("Answer:  ")
    job_c += ", if only those bullies in middle school could see you now!"
    mash["career"].append(job_c)
# CQ-4
    print("\nWhat was the worst job you've ever had?")
    job_d = input("Answer:  ")
    job_d += ", you're just a hamster stuck on the wheel of life."
    mash["career"].append(job_d)
 # CQ-5
    print("\nIf you could be anything at all, what would you be?")
    job_e = input("Answer:  ")
    job_e += ", look Ma, you made it!"
    mash["career"].append(job_e)

# Salary
    mash["salary"] = []
    possible_salary = ["$10,000", "$15,000", "$25,000",
                       "$35,000", "$50,000", "$75,000", "$100,000", "$1,000,000"]
    print("\nTo determine possible salaries you'll need to spin \nThe Wheel.... of.... Possible Fortuuuuuuuune!!! \nYou will spin the wheel 5 times, each time a new possible salary will be added to the MASH mix")
# SQ-1
    input("\nPress ENTER to spin: ")
    salary_a = random.choice(possible_salary)
    mash["salary"].append(salary_a)
# SQ-2
    input("\nPress ENTER, to spin again!")
    salary_b = random.choice(possible_salary)
    mash["salary"].append(salary_b)
# SQ-3
    input("\nCOME ON BIG MONEY! press ENTER")
    salary_c = random.choice(possible_salary)
    mash["salary"].append(salary_c)
# SQ-4
    input("\nKeep on spinning! press ENTER")
    salary_d = random.choice(possible_salary)
    mash["salary"].append(salary_d)
# SQ-5
    input("\nOne more, spin the wheel! press ENTER")
    salary_e = random.choice(possible_salary)
    mash["salary"].append(salary_e)

# Location
    mash["location"] = []
# LQ-1
    print("\nWhat city and state where you born in?")
    loc_a = input("Answer:  ")
    loc_a += ", born and raised."
    mash["location"].append(loc_a)
# LQ-2
    print("\nWhere was your favorite vacation?")
    loc_b = input("Answer:  ")
    loc_b += ", just another day in paradise!"
    mash["location"].append(loc_b)
# LQ-3
    print("\nName a state and capital")
    loc_c = input("Answer:  ")
    loc_c += ", you like to be close to the power."
    mash["location"].append(loc_c)
# LQ-4
    print("\nIf you could travel anywhere, where would you go?")
    loc_d = input("Answer:  ")
    loc_d += ", not a bad place to call home."
    mash["location"].append(loc_d)
# LQ-5
    print("\nWhere was the last place you lived?")
    loc_e = input("Answer:  ")
    loc_e += ", how did you wind up back here!?!"
    mash["location"].append(loc_e)

# Partner
    mash["partner"] = []
# PaQ-1
    print("\nWho is your celebrity crush?")
    part_a = input("Answer:  ")
    part_a += ", you're always red carpet ready."
    mash["partner"].append(part_a)
# PaQ-2
    print("\nWho did you think was a dreamboat in middle school?")
    part_b = input("Answer:  ")
    part_b += ", it was always meant to be!"
    mash["partner"].append(part_b)
# PaQ-3
    print("\nWho was your least favorite teacher?")
    part_c = input("Answer:  ")
    part_c += ", gross!"
    mash["partner"].append(part_c)
# PaQ-4
    print("\nName a politician")
    part_d = input("Answer:  ")
    part_d += ", you always were drawn to power."
    mash["partner"].append(part_d)
# PaQ-5
    print("\nWhat is your next door neighbor's name?")
    part_e = input("Answer:  ")
    part_e += ", sometimes love is right around the corner."
    mash["partner"].append(part_e)

# Pet
    mash["pet"] = []
# PeQ-1
    while True:
        print("\nWhich do you find the creepiest?")
        print("A) Tarantula")
        print("B) Oppossum")
        print("C) Hissing Cockroach")
        print("D) Centipede")
        pet_a = input("Answer:  ").lower()
        if pet_a == "a":
            pet_a = "a tarantula, it only got out a couple of times."
            break
        elif pet_a == "b":
            pet_a = "an oppossum, if you squint it's kind of cute."
            break
        elif pet_a == "c":
            pet_a = "a hissing cockroach, they're just misunderstood."
            break
        elif pet_a == "d":
            pet_a = "a centipede, it was in your shower one day and the rest is history!"
            break
        else:
            print("Please answer: A, B, C, or D")
    mash["pet"].append(pet_a)
# PeQ-2
    while True:
        print("\nWhich do you think is the smartest?")
        print("A) Robot")
        print("B) Golden Retriever")
        print("C) Potbelly Pig")
        print("D) Octopus")
        pet_b = input("Answer:  ").lower()
        if pet_b == "a":
            pet_b = "a robot, you've programmed it to bring you toilet paper when you run out."
            break
        elif pet_b == "b":
            pet_b = "a golden retriever, you have matching outfits."
            break
        elif pet_b == "c":
            pet_b = "potbelly pig, when you bought it, the lady said it would stay small!"
            break
        elif pet_b == "d":
            pet_b = "an octopus, it's unclear who is whose pet at this point."
            break
        else:
            print("Please answer: A, B, C, or D")
    mash["pet"].append(pet_b)
# PeQ-3
    print("\nWhat animal do you think is the cutest?")
    pet_c = input("Answer:  ")
    pet_c += ", all other pets pale in comparison!"
    mash["pet"].append(pet_c)
# PeQ-4
    print("\nWhat type of pet did you have growing up?")
    pet_d = input("Answer:  ")
    pet_d += ", it's a classic."
    mash["pet"].append(pet_d)

# Kids
    mash["kids"] = []
    print("\nKids are the future...are they in yours?")
    input("Press ENTER to conitue...")
    kid_a = "Twins, their names are Cindy and Mindy, you're not sure if they're plotting aginst you..."
    mash["kids"].append(kid_a)
    kid_b = "Only child, you're more like best friends though"
    mash["kids"].append(kid_b)
    kid_c = "A boy and a girl, you've called them by the first letter of their name so much you forgot what their names actually are"
    mash["kids"].append(kid_c)
    kid_d = "10 kids, you think you remeber all of their names"
    mash["kids"].append(kid_d)
    kid_e = "0, your time is your own"
    mash["kids"].append(kid_e)

    return mash
