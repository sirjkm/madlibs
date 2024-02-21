famous_person = input("a famous person: ")
people_group1 = input("a group of people: ")
people_group2 = input("another group of people: ")
noun2 = input("an awesome thing: ")
location1 = input("a cool location: ")
noun3 = input("a terrible thing: ")
famous_family = input("a famous family: ")
noun4 = input("terrible circumstance: ")
proper_noun1 = input("a good person: ")
noun5 = input("a cool tool: ")
location2 = input("a chill spot to hang out: ")

madlib = f"""Star Wars is a movie saga by {famous_person}.
It follows the course of an intergalactic battle between the {people_group1} and the {people_group2}.
The Jedi want {noun2} in {location1}, while the Sith want {noun3}.
The story follows the {famous_family} family and the tragedies they face due to the {noun4}.
Only {proper_noun1} is powerful enough, by using the {noun5} to end the war and bring balance to {location2}.
What will happen?"""

print(madlib)