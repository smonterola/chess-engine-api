#!/usr/bin/env python3
from openingBook import opening_book

def fixFen(fen: str):
    return fen.translate(str.maketrans("|_/ ", "/ |_"))

def lenBook():
    return len(opening_book)
    #json.dumps(opening_book, indent=4)

def hasBook(fenArgs):
    for fen in fenArgs:
        if fen in opening_book:
            return opening_book[fen]
    return False

def bookArgs(fen: str):
    brokenFen = fen.split(" ")[:-2]
    args = [" ".join(brokenFen)]
    if brokenFen[-1] != "-":
        args.append(" ".join(brokenFen[:-1])+" -")
    return args

