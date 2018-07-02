#Contributors - Samuel Ciocca
#Lab Section 'LE'

#"Cracker Barrel Game"
#RULES  TO THE GAME
#1. You must jump each peg over another peg, but only if there is an open space where it lands
#2. Each peg you jump over must be removed.
#3. You win if only one peg is left at the end of the game
#http://www.instructables.com/id/How-to-solve-the-Triangle-Peg-Game/ is the source for the rules

#Notes:
#Game can be solved with different pegs than the one left at the end of my program,
#but I could not figure out how to write a program that would solve the game in all possible ways
#due to the way in which I wrote this code.


#https://gist.github.com/jakepusateri/3a68487a7f9afc8ba42b is a version of the game which has solutions
#for more than one starting point if you are interested. (Credit to Jake Pusateri)

#The algorithm used is essentially a depth-first search, used originally to solve mazes.
#The program starts from the starting point, and trys all possible moves until it wins
#If a move is incorrect it will go backwards and try another move



def Drawgame(game):
  peg = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for n in range(1,16):
    peg[n] = '.'
	#when pegs are not activated they are denoted with "."
    if n in game:
		#alive pegs are denoted as follows
      peg[n] = "%X" % n
  print ("     %s" % (peg[1]))
  print ("    %s %s" % (peg[2],peg[3]))
  print ("   %s %s %s" % (peg[4],peg[5],peg[6]))
  print ("  %s %s %s %s" % (peg[7],peg[8],peg[9],peg[10]))
  print (" %s %s %s %s %s" % (peg[11],peg[12],peg[13],peg[14],peg[15]))

#Triangle with ASCII characters

#Left Side is Number, Right side is representation in ASCII
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 4
# 5 = 5
# 6 = 6
# 7 = 7
# 8 = 8
# 9 = 9
# 10 = A
# 11 = B
# 12 = C
# 13 = D
# 14 = E
# 15 = F

 
#     1
#    2 3
#   4 5 6
#  7 8 9 A
# B C D E F

#A-F is used as double digit numbers would make the triangle look stupid.


def RemovePeg(game,n):
#remove peg(n) from game
  game.remove(n)
 

def AddPeg(game,n):
#Add peg(n) on game
  game.append(n)
 

def PegExist(game,n):
# return true if peg(n) exists
  return n in game
 
# A dictionary of valid jump moves
# format PEG[(Peg which is jumped over, Peg which is landed on)]

AllowedJumpMoves = {
1: [(2,4),(3,6)],
#1: jump over 2 to land on 4, jump over 3 to land on 6
2: [(4,7),(5,9)],
#2: jump over 4 to land on 7, jump over 5 to land on 9 
3: [(5,8),(6,10)],
#3: jump over 5 to land on 8, jump over 6 to land on A
4: [(2,1),(5,6),(7,11),(8,13)],
#4: jump over 2 to land on 1, jump over 5 to land on 6, jump over 7 to land on B, jump over 8 to land on D 
5: [(8,12),(9,14)],
#5: jump over 8 to land on C, jump over 9 to land over E
6: [(3,1),(5,4),(9,13),(10,15)],
#6: jump over 3 to land on 1, jump over 5 to land on 4, jump over 9 to land on D, jump over 10 to land on F
7: [(4,2),(8,9)],
#7: jump over 4 to land on 2, jump over 8 to land on 9
8: [(5,3),(9,10)],
#8: jump over 5 to land on 3, jump over 9 to land on A
9: [(5,2),(8,7)],
#9: jump over 5 to land on 2, jump over 8 to land on 7
10: [(9,8)],
#10: jump over 9 to land on 8
11: [(12,13)],
#11: jump over C to land on D
12: [(8,5),(13,14)],
#12: jump over 8 to land on 5, jump over D to land on E
13: [(8,4),(9,6),(12,11),(14,15)],
#13: jump over 8 to land on 4, jump over 9 to land on 6, jump over C to land on B, jump over E to land on F
14: [ (9,5),(13,12)],
#14: jump over 9 to land on 5, jump over D to land on C
15: [ (10,6),(14,13)]
#15: jump over A to land on 6, jump over E to land on D
}
 
Solution = []
#Solution is used to house the correct moves used to complete the puzzle
#



def solve(game):
  #Drawgame(game)
  if len(game) == 1:
    return game 
  # Solved one peg left
  # try a move for each peg on the game
  for peg in range(1,16): # try in numeric order not game order
    if PegExist(game,peg):
	#peg is alive
      movelist = AllowedJumpMoves[peg]
      for JumpOver,LandingPeg in movelist:
	  #2nd and 3rd numbers in dictionary
        if PegExist(game,JumpOver) and not PegExist(game,LandingPeg):
		#the landing peg must exist or the move in invalid
          savegame = game[:] 
		  # for back tracking
          RemovePeg(game,peg)
          RemovePeg(game,JumpOver)
		  #remove jumped over peg 
          AddPeg(game,LandingPeg) 
		  # game order changes!
 
          Solution.append((peg,JumpOver,LandingPeg))
		  #adds the move as it is in "AllowedJumpMoves" to the solution
 
          game = solve(game)
		  #recursion
          if len(game) == 1:
            return game
          # undo move and back track if move was incorrect
          game = savegame[:] 
		  # back track
          del Solution[-1] 
		  # remove last move from Solution
  return game
 
#
# Remove one peg and start solving
#

def InitialSolve(empty):
  game = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  RemovePeg(game,empty_start)
  #This removes the inital peg
  #in the cracker barrel game you choose to remove one peg at the beggining
  solve(game)
 

print ('~~~CRACKER BARREL GAME~~~')
print ('')
 
  
empty_start = 1
InitialSolve(empty_start)
 
game = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
RemovePeg(game,empty_start)
for peg,JumpOver,LandingPeg in Solution:
#for moves added to Solution 
  RemovePeg(game,peg)
  RemovePeg(game,JumpOver)
  #remove the peg that was jumped over
  AddPeg(game,LandingPeg) 
  #add the peg which is landed on
  #game order changes!
  Drawgame(game)
  #draws picture
  print ("Peg %s jumped over %s to land on %s\n" % (peg,JumpOver,LandingPeg))
  #prints out the move added to solution