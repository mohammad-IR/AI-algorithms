# inputs and outputs
1. first input
### input
''
2
3 0 2 1
1 2 3 0
''
### output
''
6
D L U R D
''
2. Second input and out put
### input
''
4
2 3 4 8 1 5 7 12 9 6 10 0 13 14 11 15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0
''
### output
''
11
U U L L L D R D R D R
''

3. third input and out put
### input
''
2
3 0 1 2
1 2 3 0
''
### output
''
11
no solution found
''

4. forth input and out put
### input
''
3
1 2 3 4 5 6 7 0 8
1 2 3 4 5 6 7 8 0
''
### output
''
1
R
''

# Descriptions
this algorithm similar to A* but there is a difference and is 
the huristic function of A* is `f(n) = g(n) + h(n)` 
but weighted A* algorithm have a weighted and not admisible but find 
better answer by lower expand node Than A* and cost compute by  `f(n) = g(n) + h(n)`.
this algorthim result in this part is lower expand and accuracy in this inputs is 100% but not for ever and my by path is mistake but number of expand node alway is lowwer 
you can Compare this output  by another out but in A* 
in address [https://github.com/mohammad-IR/AI-algorithms/tree/master/A](A*).


