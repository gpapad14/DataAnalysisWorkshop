import random
# Theloume na mas ftiaksete ena text-based game.
# To paixnidi einai to rock,paper,scissors.
# Tha thelame na ylopoihsete ena interface(text-based) sto opoia tha dinontai oi 3 epiloges kai o xrhsths tha epilegei
# O xrhsths profanws tha paizei enantion tou ypologisth tou.
# Gia ayti thn ylopoihsh tha prepei na kanete generate tyxaious arithmous apo to 0 mexri to 2
# kai na kanete assign ton kathe arithmo se ena action tou paixnidiou
# Alloi tropoi ylopoihshs tou parapanw profanws einai kalodexoumenoi
# Epishs theloume na to ftiaksete entelws functional, dhladh na xrisimopoihtai synarthseis gia oles tis energeies tou programmatos
# kai sthn main na ginontai liga pragmata
# to paixnidi tha leitourgei epanaliptika kai tha teleiwnei stis 5 nikes
# skopos aytou tou assignment einai na mathete na xrhsimopoieite control structures kai functions se ikanopoihtiko
# vathmo

def battle(usernum, pcnum, score):
    d = usernum - pcnum        # Conditions for winning or losing
    if d==-1 or d==2:
        score[1] += 1
    elif d==1 or d==-2:
        score[0] += 1
    else:
        print "It's a tie"
    return score

score = [0,0]                  # score[0] is for user and score[1] for PC
move = {0: "ROCK", 1: "PAPER", 2: "SCISSORS"}   # Dictionary
i = 1
print "New game begins"
while score[0]<5 and score[1]<5:    # as long as no one has 5 wins keep battling
    print "Round "+str(i)           # Roound counter
    print "0 stands for ROCK, 1: PAPER, 2: SCISSORS"

    num = int(raw_input("Choose your next move: "))     # user's move
    opponent = random.randint(0, 2)                     # opponent's move
    print "your " + move[num] + " vs opponent's " + move[opponent]
    score = battle(num, opponent, score)                # calculate who wins
    print "score:: YOU: "+str(score[0])+", OPPONENT: "+str(score[1])
    i+=1
    print
if score[0]==5:
    print "!!! VICTORY !!! ^_^ "
else:
    print "LOSER... :P "

