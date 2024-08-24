#!/usr/bin/env python3
from src.creatingBook.openingBook import opening_book
import random

def fixFen(fen: str):
    return fen.translate(str.maketrans("|_/ ", "/ |_"))

def lenBook():
    return len(opening_book)

def hasBook(fenArgs):
    for fen in fenArgs:
        if fen in opening_book:
            return opening_book[fen]
    return [[""],[1]]

def bookArgs(fen: str):
    brokenFen = fen.split(" ")[:-2]
    args = [" ".join(brokenFen)]
    if brokenFen[-1] != "-":
        args.append(" ".join(brokenFen[:-1])+" -")
    return args

def chooseMove(bookEntry):
    return random.choices(bookEntry[0], weights=bookEntry[1])[0]

