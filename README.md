# Matrix Puzzle [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
4 column by 4 row math problem matrix. The matrix-solver program brute forces a solution.
                    
 |   | + |   | + |   | - |   | = 31|
 |---|---|---|---|---|---|---|-----|
 | + |   | + |   | + |   | x |     |
 |   | x |   | / |   | - |   | = -3|
 | - |   | + |   | + |   | + |     |
 |   | + |   | + |   | + |   | = 42|
 | + |   | + |   | - |   | - |     |
 |   | + |   | / |   | + |   | =  8|
 | = |   | = |   | = |   | = |     |
 | 5 |   |51 |   | 35|   | 32|     |
 
 
 The matrix below is labelled exactly as you will see it in the program.
 
 | R1[i][0]  | + | R1[i][1]  | + | R1[i][2]  | - | R1[i][3]  | = 31|
 |-----------|---|-----------|---|-----------|---|-----------|-----|
 |    +      |   |      +    |   |    +      |   |         x |     |
 | R2[j][0]  | x | R2[j][1]  | / | R2[j][2]  | - | R2[j][3]  | = -3|
 | -         |   |         + |   | +         |   |         + |     |
 | R3[k][0]  | + | R3[k][1]  | + | R3[k][2]  | + | R3[k][3]  | = 42|
 | +         |   |         + |   |         - |   |         - |     |
 | R4[l][0]  | + | R4[l][1]  | / | R4[l][2]  | + | R4[l][3]  | =  8|
 | =         |   |         = |   |         = |   | =         |     |
 | 5         |   |       51  |   |         35|   |         32|     |


## ToDo
- Create recursive solution
