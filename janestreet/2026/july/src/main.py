from __future__ import annotations


"""

Up until the 18th move, knight writes down the score on 

0
3
6
9
12
15
18

After that, it write down every K moves, K \in \mathbb{N}

18 + K
18 + 2K
...

need to infer the knight's path from the scores on the board.

** restrictions **
-- knights moves are 3 dimensional
-- towers are as follows: You get one extra 1x1x1 cube on one of the squares of the pentomino or tetromino.
-- knights tour is to all TOWERS, aka the extra 1x1x1 cubes in the Z dimension.
-- it never visits the same space twice
"""
from dataclasses import dataclass

import copy
from collections import defaultdict, deque
from typing import List, Optional


# should be reasonably tractable to prune according to the three step scores .
# besides knights tours, you also have to backtrack from possible tower arrangements. 
# should keep track of checkpoints, which would be all possible admissable knights tours up to N steps. 
# this would allow for pruning of the search space.



board = [ 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 750, 0, 88, 0, 272, 1, 0],
    [0, 449, 0, 0, 16, 0, 0, 0],
    [528, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 23, 0, 138, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 37, 0, 1100],
]

targets = [x for row in board for x in row if x != 0]


sol = copy.deepcopy(board)

# 12 pentominoes, 1 tetromino

ominoes = [
    [0, 0, 0, 0, 0, 1, 1, 1],
    [2, 2, 2, 3, 3, 4, 4, 1],
    [2, 5, 2, 3, 3, 3, 4, 1],
    [6, 5, 5, 9, 9, 10, 4, 4],
    [6, 6, 5, 9, 9, 10, 10, 11], 
    [6, 7, 5, 8, 10, 10, 12, 11],
    [6, 7, 8, 8, 8, 12, 12, 11],
    [7, 7, 7, 8, 12, 12, 11, 11],
]


def possible_3_step_moves(board, ominoes, tower_locations, currscore : int):
    # should take a position, and return all possible 3 step moves.
    # firstly should be arithmetically correct given the 3 step values of the walk
    # secondly should be admissable given the tower locations.
    
    
    # get reachable next position by backtracking both on kight walks, past moves and tower locations.
    
    # cross validate next position scores with arithmetic correctness.. 
    
    # return all possible 3 step moves, to then be backtracked from.

    pass
    

@dataclass
class Position:
    i : int
    j : int
    z : int
    
@dataclass
class Tour:
    move : int
    score : int
    path : list[Position]

class Node:
    score : int
    parent : Node
    children : List[Node]
    



def main(board, visited, tower_config, curr_score, N):
    # the most abstract thing is the gemoetry of the board
    # to get all possible trajectories to neighboring tiles, you either move (2, 0) or (2, 1).
    # with the implication that 2,0 creates a tower in your trajectory. 
    # and we only really care, greedily, if the cells we are moving towards are towers.
    # inductively, by forbidding future towers in the same n-omino, we should generate a correct path
    
    # the arithmetic correctness could be a good pruning strategy to make the whole problem tractable
    # assuming that after passing checkpoints (3 moves), the # of admissable paths does not blow up.
    # this should all be backtrackable.
    
    # first, collect the possible 3 step target cells. these, unless forbidden by existing towers, can
    # be (i,j,0) or (i,j,1). (not tower or tower)
    
    # then, for each 2 tuple of (currscore, targetscore) generate all possible paths, saving a 3 tuple
    # of operators on the temp_score, assuming that path is correct.
    
    # keep a list of possible paths with associated tower additions to the problem.
    
    # remembering that the initial square you are on also could be a tower. in this case, im pretty sure it is. 
    
    # so in short, the backtracking coallesces tower structure and possible paths given that structure. 
    
    # after reaching every checkpoint, you iterate over a queue of all the admissable score processes,
    # and pray that that queue does not stack overflow
    
    # lets begin 
    # actually, I think the easiest way to get to the answer would be to first find the viable targets,
    # and then iterate on those. 
    
    
    i, j = 0, 0
    
    # k is a multiple of 7 

    # main queues to bfs from
    tour_q= deque[Tour]()
    next_position_queue = deque[Position]()
    
    # dict to keep track of ominoes that contain towers
    ominoes_with_tower : dict[int, bool] = {}
    towers_visited = 0
    
    # list of known scores every 3 and K moves
    targets = [x for row in board for x in row if x != 0]
    
    # the least blow-uppy heuristic I can think of is go through all the 
    # implied tower positions given the possibleops return and work from 
    # there
    
    
    score = 0
    n = 1

    
    def bfs(board : list[list[int]], visited : set, tower_config : list[list[int]], curr_score : int, move : int):  
        pass
        
        
        
    
    # while towers_visited < 16:
        
    #     for t in targets:
    #     ops, _  = possible_ops(score, n, )
        
        
    
    
    
    
    
    
    



def possible_ops(curr_score: int, n: int, target: int, num_moves: int = 3):
    # enumerate op sequences for moves n, n+1, ..., n+num_moves-1 that turn
    # curr_score into target. ops per move N: '+' (flat, +N), '*' (up, xN),
    # '/' (down, /N, only when evenly divisible).
    # returns a list of (ops, trace) where ops is e.g. ('+3', '*4', '/5')
    # and trace holds the intermediate scores after each move.
    results = []

    def rec(score, move, ops, trace):
        if move == n + num_moves:
            if score == target:
                results.append((tuple(ops), list(trace)))
            return
        rec(score + move, move + 1, ops + [f"+{move}"], trace + [score + move])
        rec(score * move, move + 1, ops + [f"*{move}"], trace + [score * move])
        if score % move == 0:
            rec(score // move, move + 1, ops + [f"/{move}"], trace + [score // move])

    rec(curr_score, n, [], [])
    return results

   

target_times = [3, 6, 9, 12, 15, 18, 25, 32, 39, 46, 53]

# Mainly for manual excursion of knight, not useful for algorithmic sol
def print_viable_score_processes_intracheckpoint():
    

    curr = 0
    target = 0
    
    for n in target_times:
        print("--------------------------------")
        
        
        k = 3 if n < 19 else 7
        print(f"Looking at steps {n - k}-{n}")

        for tscore in targets: 

            paths = possible_ops(curr, n - k + 1, tscore, k)

            if paths:
                ops, trace = paths[0]
                print(f"Found a path to target cell {tscore}")
                target = tscore
                print(ops, trace)
                
        curr = target
                

if __name__ == "__main__":
    print_viable_score_processes_intracheckpoint()