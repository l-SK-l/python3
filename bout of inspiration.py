import random

noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verb = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]
adjective = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]
preposition = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverb = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]


def generate_poem():
    noun1 = random.choice(noun)
    noun2 = random.choice(noun)
    noun3 = random.choice(noun)
    while noun1 == noun2:
        noun2 = random.choice(noun)
    while noun1 == noun3 or noun2 == noun3:
        noun3 = random.choice(noun)

    verb1 = random.choice(verb)
    verb2 = random.choice(verb)
    verb3 = random.choice(verb)
    while verb1 == verb2:
        verb2 = random.choice(verb)
    while verb1 == verb3 or verb2 == verb3:
        verb3 = random.choice(verb)

    adjective1 = random.choice(adjective)
    adjective2 = random.choice(adjective)
    adjective3 = random.choice(adjective)
    while adjective1 == adjective2:
        adjective2 = random.choice(adjective)
    while adjective1 == adjective3 or adjective2 == adjective3:
        adjective2 = random.choice(adjective)

    preposition1 = random.choice(preposition)
    preposition2 = random.choice(preposition)
    while preposition1 == preposition2:
        preposition2 = random.choice(adjective)

    adverb1 = random.choice(adverb)

    if "aeiou".find(adjective1[0]) != -1:
        article = "An"
    else:
        article = "A"

    poem = (
        f'{article} {adjective1} {noun1}\n'
        f'{article} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}\n'
        f'{adverb1}, the {noun1} {verb2}\n'
        f'the {noun2} {verb3} a {adjective3} {noun3}'
    )
    return poem


poem = generate_poem()
print(poem)
