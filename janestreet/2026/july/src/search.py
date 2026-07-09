
from __future__ import annotations 
from dataclasses import dataclass

import copy
from typing import List, Optional
import collections

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

@dataclass
class Node:
    p : Position
    score : int
    move : int
    parent : Optional[Node]
    children : List[Node]
    tower_path : List[int]
    visited_squares : List[Position]

legal_moves = [
    # intraplanar moves
    (2, 0, 1), (2, 0, -1), (-2, 0, 1), (-2, 0, -1),
    (0, 2, 1), (0, 2, -1), (0, -2, 1), (0, -2, -1),
    # inter planar moves
    (2, 1, 0), (2, -1, 0), (-2, 1, 0), (-2, -1, 0),
    (1, 2, 0), (1, -2, 0), (-1, 2, 0), (-1, -2, 0),
]

relative_positions = [Position(*m) for m in legal_moves]    

def make_move(p : Position, m : Position):
    p.i += m.i
    p.j += m.j
    p.z += m.z
    
    return p

def inbounds(p : Position):  
    return  (0 <= p.i < 8)and (0 <= p.j < 8) and (0 <= p.z < 2)

def one_step_inbounds(p : Position) -> List[Position]:
    one_step_lookahead = []
    for m in relative_positions:
        np = make_move(p, m)
        if inbounds(np):
            one_step_lookahead.append(np)
            
            
    return one_step_lookahead


def reverse_