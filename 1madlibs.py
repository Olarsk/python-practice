# MADLIBS
# Mad Libs is a phrasal template word game created by Leonard Stern
# and Roger Price. It consists of one player prompting others for a
# list of words to substitute for blanks in a story before reading aloud.
# The game is frequently played as a party game or as a pastime.

# madlib variables
name1 = input("Dragon Ball in Japanese: ")
name2 = input("Production studio: ")
name3 = input("Author of Dragon ball: ")
name4 = input("What type of manga is Dragon Ball: ")
num1 = int(input("How many manga chapters are there in Dragon Ball: "))
num2 = input("How many episodes were in OG Dragon Ball: ")

# madlib text
madlib = f"Dragon Ball(Japanese: {name1}) is a Japanese anime television series\
    produced by {name2}. It is an adaptation of the first {num1} \
    chapters of the manga of the same name created by {name3}, which were\
    published in Weekly {name4} Jump from 1984 to 1995. The anime is composed\
    of {num2} episodes that were broadcast on Fuji TV from February \
    1986 to April 1989. It was broadcast in 81 countries worldwide.\
    It is part of the Dragon Ball media franchise.[4]"

print(madlib)
noun1 = input("Human name: ")
noun2 = input("Profession: ")
noun3 = input("Family name: ")
noun4 = input("School name: ")
noun5 = input("Villain name: ")
noun6 = input("Friend name: ")
noun7 = input("Friend name: ")
adj1 = input("Adjective: ")
pronoun1 = input("Pronoun: ")

madlib2 = f"The series follows the life of a boy named {noun1} Potter. \
In the first book, {noun1} Potter and the {noun2}'s Stone, {noun1}\
lives in a cupboard under the stairs in the house of the {noun3}, \
his aunt, uncle and cousin. The {noun3} consider themselves perfectly\
normal, but at the age of eleven, {noun1} discovers that he is a wizard.\
He meets a half-giant named Hagrid who invites {pronoun1} to attend {noun4}\
School of Witchcraft and Wizardry. {noun1} learns that as a baby, his parents\
were murdered by the dark wizard Lord {noun5}. When {noun5} attempted\
to kill {noun1}, his curse rebounded and {noun1} survived with a \
lightning-shaped scar on his forehead.\
{noun1} becomes a student at {noun4} and is sorted into Gryffindor House. \
He gains the friendship of {noun6}, a member of a large but poor \
wizarding family, and {noun7}, a witch of non-magical, or \
Muggle, parentage. {noun1} encounters the school's potions master, \
Severus Snape, who displays a dislike for {pronoun1}; the rich pure-blood \
Draco Malfoy whom he develops an enmity with; and the Defence Against the \
Dark Arts teacher, Quirinus Quirrell, who turns out to be allied with \
Lord {noun5}. The first book concludes with {noun1}'s confrontation with \
{noun5}, who, in his quest to regain a body, yearns to gain the power of \
the {noun2}'s Stone, a substance that bestows everlasting life."

print(madlib2)
