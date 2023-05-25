# RaichuChessGame
Raichu is a popular childhood game played on an n × n grid (where n ≥ 8 is an even number) with three kinds of pieces (Pichus, Pikachus, and Raichus) of two different colors (black and white).

### Approach:
The approach that we have used for this problem is to min-max algorithm where we can set the depth to which the tree should be implemented such that the motive is to optimise the values for our minmax as well as reduce the time taken for execution in each code. The min-max algorithm returns the best value for our alpha and beta values using alpha beta pruning.

### Execution:
We have initialized the code by writing 3 functions. 1 for pichu, 1 for pichu and another for raichu. In pichu we are looking at the opponent players who can be attacked diagonally in the forward direction, One step at a time. The code reference was from an arranged pichus in which we had implemented to move the pichu in the diagonally forward direction. 

### Implementation part1:
1) Here, the pichu acts as the bishop in the chess game. For implementing the pichu, we look at the available opponent pichu nodes which can be captured. 
2) If there is a pichu of the opponent we jump over the pichu of the opponent and replace the opponent pichu with a “ . ” and move one step ahead. We are doing this by checking each next node in the diagonal direction and looking out for the opponent variables. 
3) In the code we have defined the player and the opponent variables. 

In Pikachu we have set the moves to move in a forward, left and right direction, where the Pikachu will decide which direction to move in depending on the pichus or pikachus of the opponent in the board. The pikachu can move one step or 2 step in the forward, right or left directions respectively.

### Implementation part2:
1) In Pikachu, it can eliminate the pichu and the pikachu of the opponent. Since it can move like an elephant in the chess board game, we will check for the opponent nodes in the left, right and forward direction. 
2) The pikachu can jump over a pichu or a pikachu of the opponent by moving 2 or 3 nodes in case if it finds an opponent. It will replace the opponent node with a “ . “ and move one step ahead.

A Raichu is created when a Pichu or Pikachu reaches the opposite side of the board and when this happens, the Pichu or Pikachu is removed from the board and substituted with a Raichu  In Raichu, which can move in the 8 directions that is in the upward, downward, right, left and in the 4 diagonal directions. The raichu can capture the pichu, pikachu and raichu of the opponent.

### Implementation part3:
1) This was the toughest to implement as we have to look for all the pieces of the opponent in all the eight directions which I have defined in my code as North, south, east, west, northeast, northwest, southeast and southwest. 
2) We are returning 2 parameters from each direction that is moves and kill_moves which will return the moves done by the player (thats us) and the number of the pieces of the opponent thats replaced by “ . “.

### The minmax algorithm:
The minmax algorithm in our case is considering a bestvalue, alpha and beta as some high negative number while checking if the node is a maximizing node and the is being assigned with the max value between the bestvalue and the value which we get by considering our node as the maximizing player. Similarly, we are doing while minimizing the node for the opponent.
