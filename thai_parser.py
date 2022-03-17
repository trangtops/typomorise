import json

with open("eng_to_thai.json", "r") as f:
    eng_to_thai = json.load(f)


def to_thai(eng_char):
    # global eng_to_thai
    return eng_to_thai.get(eng_char, eng_char)
