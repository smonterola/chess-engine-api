#!/usr/bin/env python3
import json

def main():
    opening_book: dict = {}
    openings_file = "openings_raw.txt"
    opening_string = ""
    with open(openings_file, "r") as file:
        opening_string = file.read().strip()
    opening_boards = opening_string.split("pos ")[1:]
    for opening in opening_boards:
        opening = opening.strip()
        opening_data = opening.split("\n")
        fen_opening = opening_data.pop(0)
        moves_list = []
        moves_frequencies = []
        for line in opening_data:
            line_segment = line.split(" ")
            move = line_segment[0]
            frequency = int(line_segment[1])
            moves_list.append(move)
            moves_frequencies.append(frequency)
        opening_book[fen_opening] = [moves_list, moves_frequencies]
    #print(json.dumps(opening_book))
    #print(len(opening_book))
    opening_book_json_file = open("openingBook.py", "w")
    opening_book_json_file.write("opening_book = ")
    opening_book_json_file.write(json.dumps(opening_book, indent=4))

if __name__ == "__main__":
    main()