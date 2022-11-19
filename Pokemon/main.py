from cProfile import run
from re import A
from app import app
from flask import render_template
import time, sys, random, json

with open('/Users/vishvdhanraj/Documents/PokemonRepository/pokemon/pokedex.json', 'r') as pokefile:
    pokeList = json.load(pokefile)

pokemonNameToIdDict = {}
pokemonNumtoStatDict = {}
genList = [[1, 151], [152, 252], [253, 386], [387, 493], [494, 649], [650, 721], [722, 809], [810, 905], [906, 917]]


def init():
    for mon in pokeList:
        pokemonNameToIdDict[mon['name']['english']] = mon['id']
        pokemonNumtoStatDict[mon['id']] = mon
    return pokemonNameToIdDict


def getPokeName(index):
    if int(index) >= len(pokemonNameToIdDict):
        return None
    name = pokemonNumtoStatDict[index]['name']['english']
    return name

def getGen(num):
    notN = 'no'
    for i in range(0, len(genList)):
        if num >= genList[i][0] and num <= genList[i][1]:
            notN = 'yes'
            return i+1
    if notN == 'no':
        return 'n'


def printPoke(pmon):
    if len(pmon['type']) == 2:
        types = '{}/{} Type'.format(pmon['type'][0], pmon['type'][1])
    else:
        types = '{} Type'.format(pmon['type'][0])
    print(
        "\t#{}: {}\n\t {}\n\t Base Stats: \n\t\tHP: {} \n\t\tAttack: {} \n\t\tDefense: {} \n\t\tSpecial Attack: {} \n\t\tSpecial Defense: {} \n\t\tSpeed: {} \n\t\tBase Stat Total: {}".format(
            pmon["id"], pmon["name"]["english"], types,
            pmon['base']['HP'], pmon['base']['Attack'],
            pmon['base']['Defense'], pmon['base']['Sp. Attack'],
            pmon['base']['Sp. Defense'], pmon['base']['Speed'],
            pmon['base']['baseStatTotal']))


def formatByTen(mons):
    arrangement = '\n\t\t'
    count = 10
    for num in mons:
        if count <= 0:
            count = 10
            arrangement += '\n\t\t'
        dexEntry = "#{}: {}".format(num, getPokeName(num))
        spacer = 0
        for i in range(30 - len(dexEntry)):
            spacer += 1
        arrangement += dexEntry + spacer * ' '
        count -= 1
    return arrangement


def startUp():
    init()
    opt = input("What do you want to do? (Type 'o' for options).\n >>> ")
    while opt == 'o':
        print(
            "\tType [1] to find the Pokemon accosiated with the given National Dex number or find the National Dex number of a given Pokemon. \n\tType [2] to view any Generation's pokedex. \n\tType [3] to generate random Pokemon. \n\tType [4] to do a Pokedex-based quiz. \n\tType [5] to play a guessing game. \n\tType [e] to exit.")
        opt = input("What do you want to do? (Type 'o' for options). \n >>> ")

    if opt == 'e':
        exit()
    elif opt == '0':
        print(" ... Loading Secret Pokemon Index Base: Access Denied")
        startUp()
    elif opt == '1':
        findPokeData()
    elif opt == '2':
        viewDex()
    elif opt == '3':
        randomMon()
    elif opt == '4':
        Quiz()
    elif opt == '5':
        guessingGame()
    elif opt == '6':
        search()
    else:
        redirection()


def findPokeData():
    inp = ''
    while True:
        inp = input(
            "Type in any number until 917 or any Pokemon name until Quaxly to get it's stats. Make sure to capitalize the first letter of each word. \nType [e] to exit.\n >>> ")
        pmon = ''
        num = 0
        if inp in pokemonNameToIdDict or inp in pokemonNumtoStatDict or inp != 'e':
            if inp.isdigit() == True:
                pmon = getPokeName(int(inp))
                num = inp
            elif inp.isdigit() == False:
                num = pokemonNameToIdDict[inp]
                pmon = inp

            if pmon == '' and num == 0:
                print("... Sorry, Pokemon Not found ...")
                findPokeData()
            pokemon = pokemonNumtoStatDict[int(num)]
        else:
            startUp()
        printPoke(pokemon)
    startUp()


'''def findMon(num):
    return num, pokeList.get(int(num))


def findNum(n):
    # pokeName = input("Type in any Pokemon name until Quaxly to get it's corresponding National Dex number. Make sure to capitalize the first letter of each word. \nType [e] to exit.\n >>> ")
    while n != 'e':
        for num, pmon in pokeList.items():
            if pmon == n:
                # print("#{}: {}".format(num, n))
                return num
        pokeName = input(
            "Type in any Pokemon name until Quaxly to get it's corresponding National Dex number. \nType [e] to exit.\n >>> ")
    startUp()'''


'''def dexOpt(gen):
    if gen == 'n':
        sectNum = [0, len(pokeList)]
    elif gen == '1':
        sectNum = [0, 151]
    elif gen == '2':
        sectNum = [152, 252]
    elif gen == '3':
        sectNum = [253, 386]
    elif gen == '4':
        sectNum = [387, 493]
    elif gen == '5':
        sectNum = [494, 649]
    elif gen == '6':
        sectNum = [650, 721]
    elif gen == '7':
        sectNum = [722, 809]
    elif gen == '8':
        sectNum = [810, 905]
    elif gen == '9':
        sectNum = [906, 917]
    elif gen == '' or '\n':
        redirection()
    else:
        print("Sorry, that generation isn't registered here yet.")
        startUp()
    return sectNum
'''


def viewDex():
    gen = input(
        "Type a Generation number (1-9) to print that generation's Pokedex. Type [n] to print the National Pokedex. Press enter to use the previous generation used. \nType [e] to exit.\n >>> ")
    while gen != 'e':
        if gen == 'n':
            gen = '0'
        monList = []
        for i in range(genList[int(gen)][0], genList[int(gen)][1]):
            monList.append(i)
        print(formatByTen(monList))

        gen = input(
            "\n\nType a Generation number (1-9) to print that generation's Pokedex. Type [n] to print the National Pokedex. Press enter to use the previous generation used. \nType [e] to exit.\n >>> ")
    startUp()


def randomMon():
    opt = input("Type a Generation number (1-9) to generate a random Pokemon from that generation. Type [n] to generate a random Pokemon from the national dex. Press enter to use the last generation used. \nType [e] to exit.\n >>> ")
    while opt != 'e':
        if opt == 'n':
            sectNum = [1, 917]
        else:
            sectNum = genList[int(opt)]
        num = random.randint(sectNum[0], sectNum[1])
        mon = getPokeName(num)
        print(printPoke(mon))
        opt = input("\nType a Generation number (1-9) to generate a random Pokemon from that generation. Type [n] to generate a random Pokemon from the national dex. Press enter to use the last generation used. \nType [e] to exit.\n >>> ")
    startUp()


def Quiz(correct=0, times='', wrong=0, prev='0'):
    if times != '':
        prevUse = "Press enter to use the last option used. "
        if wrong == []:
            amountWrong = "You got no questions wrong."
        else:
            amountWrong = "You got question(s) {} wrong.".format(wrong)
        again = input("Your score is {}/{} or {}%. {} Do you want to play again (yes/no)?\n >>> ".format(correct, times,
                                                                                                         correct / times * 100,
                                                                                                         amountWrong))
        if again.lower() == 'yes':
            pass
        else:
            startUp()
    else:
        prevUse = ''

    quizOpt = input(
        "Type [1] if you want your quiz to be dex-based. Type [2] if you want your quiz to be number-based. Type [3] if you want your quiz to be name-based. {}Type [e] to exit.\n >>> ".format(
            prevUse))
    while quizOpt != 'e':
        times = input("How many questions shall I ask? Type in any number until 100. Type [e] to exit. \n >>> ")
        if times.isdigit() == False:
            Quiz()
        elif int(times) > 100:
            Quiz()

        times = int(times)
        if quizOpt == '':
            quizOpt = prev
        if quizOpt == '0':
            Quiz(correct, times, wrong, prev)
        elif quizOpt == '1':
            prev = '1'
            dexQuiz(times, prev)
        elif quizOpt == '2':
            prev = '2'
            numQuiz(times, prev)
        elif quizOpt == '3':
            prev = '3'
            nameQuiz(times, prev)

    startUp()


def dexQuiz(times, prev):
    correct = 0
    wrong = []
    for q in range(times):
        randomNum = random.randint(0, 917)
        pokemon = getPokeName(randomNum)
        count = 0
        genNum = getGen(randomNum)
        '''for gen in ListNatDex:
            count += 1
            if randomMon in gen.values():
                genNum = count
                break'''

        question = input(
            "\tWhat generation is the Pokemon, {}, from? Please type a number under 10.\n\t >>> ".format(pokemon))
        if int(question) == genNum:
            correct += 1
            print("Good job!")
        else:
            wrong.append(q + 1)
            print("The correct answer was {}.".format(genNum))
    Quiz(correct, times, wrong, prev)


def numQuiz(times, prev):
    correct = 0
    wrong = []
    for q in range(times):
        pokeNum = 0
        randint = random.randint(0, 917)
        randomMon = getPokeName(randint)

        question = input("\tWhat Pokemon is number {} in the National Dex? \n\t >>> ".format(randint))
        if question.capitalize() == randomMon:
            correct += 1
        else:
            wrong.append(q + 1)
            print("The correct answer was {}.".format(randomMon))
    Quiz(correct, times, wrong, prev)


def nameQuiz(times, prev):
    correct = 0
    wrong = []
    for q in range(times):
        randomNum = random.randint(0, 917)
        pokeMon = getPokeName(randomNum)

        question = input(
            "\tWhat number is the Pokemon, {}, in the National Dex? Please type in a number under 917.\n\t >>> ".format(
                pokeMon))
        if int(question) == randomNum:
            correct += 1
        else:
            wrong.append(q + 1)
            print("The correct answer was {}.".format(randomNum))
    Quiz(correct, times, wrong, prev)


def guessingGame():
    gameOpt = input("Type [1] if you want me to guess your Pokemon. Type [2] if you want to to guess my Pokemon. \nType [e] to exit.\n >>> ")
    if gameOpt == 'e':
        startUp()
    elif gameOpt == '1':
        compGuess()
    elif gameOpt == '2':
        userGuess()
    else:
        guessingGame()

def compGuess():
    questions = 0
    refGuessList = pokeList
    typeNum = int(input("How many types does your Pokemon have? Type in 1 or 2. \n >>> "))
    guessList=[]
    for pmon in refGuessList:
        if len(pmon['type']) == typeNum:
            guessList.append(pmon)
    refGuessList = guessList
    questions += 1

    guessList = []
    typeOne = input("What is your Pokemon's first type?\n >>> ").capitalize()
    for pmon in refGuessList:
        if pmon['type'][0] == typeOne:
            guessList.append(pmon)
    refGuessList = guessList
    questions += 1

    if typeNum == 2:
        guessList = []
        typeTwo = input("What is your Pokemon's second type? \n >>> ").capitalize()
        for pmon in refGuessList:
            if pmon['type'][1] == typeTwo:
                guessList.append(pmon)
        refGuessList = guessList
        questions += 1

    guessList = []
    genNum = input("What generation is your Pokemon from? Type in a number from 1 to 9. (If you are not sure, type in 'n') \n >>> ")
    if genNum != 'n':
        for pmon in refGuessList:
            if int(genNum) == getGen(pmon['id']):
                guessList.append(pmon)
        refGuessList = guessList
    else:
        guessList = refGuessList
    questions += 1

    if guessList == []:
        print("Sorry, there is currently no Pokemon in our database with that specific combination.\n")
        guessingGame()
    else:
        randomNum = random.randint(0, len(guessList)-1)
        randomPoke = guessList[randomNum]['name']['english']
        questions += 1
        decide = input("Was {} the Pokemon you were thinking of? Type in 'yes' or 'no'. \n >>> ".format(randomPoke)).lower()
        while decide != 'yes' and guessList != []:
            guessList.remove(guessList[randomNum])
            randomNum = random.randint(0, len(guessList) - 1)
            randomPoke = guessList[randomNum]['name']['english']
            questions += 1
            decide = input("Was {} the Pokemon you were thinking of?\n >>> ".format(randomPoke)).lower()
            if guessList == []:
                break

        again = input("Good game! I took {} questions to find your Pokemon, {}! \nWould you like to play again?\n >>> ".format(questions, randomPoke)).lower
        if again == 'yes':
            compGuess()
        else:
            guessingGame()

def userGuess():
    num = random.randint(0, len(pokemonNumtoStatDict))
    mon = getPokeName(num)
    monClues = [pokeList[mon]['type']]


def search():
    questions = 0
    refGuessList = pokeList
    typeNum = int(input("How many types does your Pokemon have? Type in 1 or 2. \n >>> "))
    guessList = []
    for pmon in refGuessList:
        if len(pmon['type']) == typeNum:
            guessList.append(pmon)
    refGuessList = guessList
    questions += 1

    guessList = []
    typeOne = input("What is your Pokemon's first type?\n >>> ").capitalize()
    for pmon in refGuessList:
        if pmon['type'][0] == typeOne:
            guessList.append(pmon)
    refGuessList = guessList
    questions += 1

    if typeNum == 2:
        guessList = []
        typeTwo = input("What is your Pokemon's second type? \n >>> ").capitalize()
        for pmon in refGuessList:
            if pmon['type'][1] == typeTwo:
                guessList.append(pmon)
        refGuessList = guessList
        questions += 1

    guessList = []
    genNum = input(
        "What generation is your Pokemon from? Type in a number from 1 to 9. (If you are not sure, type in 'n') \n >>> ")
    if genNum != 'n':
        for pmon in refGuessList:
            if int(genNum) == getGen(pmon['id']):
                guessList.append(pmon)
        refGuessList = guessList
    else:
        guessList = refGuessList
    questions += 1

    finalList = []
    for pmon in guessList:
        finalList.append(pmon['id'])
    formattedList = formatByTen(finalList)
    print(formattedList)



def redirection():
    print("Redirecting to startup...")
    startUp()


def exit():
    sure = input("Are you sure you want to exit? (yes/no) \n >>> ").lower()
    if sure == 'yes' or sure == 'e':
        print("Thanks for using the Pokedex Numerical Retrieval System. See you next time!")
        sys.exit()
    else:
        redirection()


startUp()