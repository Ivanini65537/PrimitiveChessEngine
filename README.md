"# PrimitiveChessEngine" 

Chess engine working in console , implemented in 350 lines of code with chess library in Python
implemented minimax search https://en.wikipedia.org/wiki/Minimax
and position evaluation

Good base for further improvment on engine only lacks endgame tables that could be impemented in the future

command to install library: pip install chess

Lacking gui but terminal interface looks like this:

Welcome to chessy chess engine choose (W)hite or (B)lack pieces B

Play your moves so that they include coordinates of begging and ending square, for example e2e4

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
Computers turn
Computer plays e2e4
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . P . . .
. . . . . . . .
P P P P . P P P
R N B Q K B N R
Your turn to play
Play your move e7e5
You have played move e7e5
Computers turn
Computer plays g1f3
r n b q k b n r
p p p p . p p p
. . . . . . . .
. . . . p . . .
. . . . P . . .
. . . . . N . .
P P P P . P P P
R N B Q K B . R
Your turn to play
Play your move b8c6
You have played move b8c6
Computers turn
Computer plays b1c3
r . b q k b n r
p p p p . p p p
. . n . . . . .
. . . . p . . .
. . . . P . . .
. . N . . N . .
P P P P . P P P
R . B Q K B . R
Your turn to play
Play your move f1c5
illegal move try again
Your turn to play
Play your move f8c5
You have played move f8c5
Computers turn
Computer plays f1b5
r . b q k . n r
p p p p . p p p
. . n . . . . .
. B b . p . . .
. . . . P . . .
. . N . . N . .
P P P P . P P P
R . B Q K . . R
Your turn to play
