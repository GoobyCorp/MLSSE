#!/usr/bin/python3

from io import BytesIO
from os.path import isfile
from struct import pack, unpack
from argparse import ArgumentParser

MARIO_BLOB_START = 0x00
MARIO_BLOB_LEN = 0x28

MARIO_XP_LOC = 0x1C  #int32
MARIO_HP_LOC = 0x00  #int16
MARIO_BP_LOC = 0x02  #int16

#Mario bonus HP, BP, POW, DEF, SPEED, and STACHE
MARIO_BONUS_HP_LOC =     0x06  #int16
MARIO_BONUS_BP_LOC =     0x0A  #int16
MARIO_BONUS_POW_LOC =    0x0E  #int16
MARIO_BONUS_DEF_LOC =    0x12  #int16
MARIO_BONUS_SPEED_LOC =  0x16  #int16
MARIO_BONUS_STACHE_LOC = 0x1A  #int16

LUIGI_BLOB_START = 0x28
LUIGI_BLOB_LEN = 0x28

LUIGI_XP_LOC = 0x44  #int32
LUIGI_HP_LOC = 0x28  #int16
LUIGI_BP_LOC = 0x2A  #int16

#Luigi bonus HP, BP, POW, DEF, SPEED, and STACHE
LUIGI_BONUS_HP_LOC =     0x2E  #int16
LUIGI_BONUS_BP_LOC =     0x32  #int16
LUIGI_BONUS_POW_LOC =    0x36  #int16
LUIGI_BONUS_DEF_LOC =    0x3A  #int16
LUIGI_BONUS_SPEED_LOC =  0x3E  #int16
LUIGI_BONUS_STACHE_LOC = 0x42  #int16

GOLD_LOC = 0x50  #int32

#int8's
ITEM_START = 0x54
ITEM_LEN = 0x12

#int8's
BEAN_START = 0x130
BEAN_LEN = 0x04

MARIO_LEVELS = {
    1: 0,
    2: 7,
    3: 32,
    4: 68,
    5: 108,
    6: 218,
    7: 336,
    8: 470,
    9: 694,
    10: 962,
    11: 1254,
    12: 1578,
    13: 1924,
    14: 2306,
    15: 2756,
    16: 3256,
    17: 3830,
    18: 4480,
    19: 5195,
    20: 5975,
    21: 6845,
    22: 7805,
    23: 8805,
    24: 9845,
    25: 10925,
    26: 12025,
    27: 13225,
    28: 14575,
    29: 16085,
    30: 17765,
    31: 19625,
    32: 21685,
    33: 23965,
    34: 26485,
    35: 29265,
    36: 32325,
    37: 35685,
    38: 39365,
    39: 43385,
    40: 47805,
    41: 52805,
    42: 58305,
    43: 64405,
    44: 71905,
    45: 79705,
    46: 87805,
    47: 96205,
    48: 104905,
    49: 113905,
    50: 123205,
    51: 132805,
    52: 142705,
    53: 152905,
    54: 163405,
    55: 174205,
    56: 185305,
    57: 196705,
    58: 208405,
    59: 220405,
    60: 232705,
    61: 245305,
    62: 258205,
    63: 271405,
    64: 284905,
    65: 298705,
    66: 312805,
    67: 327205,
    68: 341905,
    69: 356905,
    70: 372205,
    71: 387805,
    72: 403705,
    73: 419905,
    74: 436405,
    75: 453205,
    76: 470305,
    77: 487705,
    78: 505405,
    79: 523405,
    80: 541705,
    81: 560305,
    82: 579205,
    83: 598405,
    84: 617905,
    85: 637705,
    86: 657805,
    87: 678205,
    88: 698905,
    89: 719905,
    90: 741205,
    91: 762805,
    92: 784705,
    93: 806905,
    94: 829405,
    95: 852205,
    96: 875305,
    97: 898705,
    98: 922405,
    99: 946395  #946405
}

LUIGI_LEVELS = {
    1: 0,
    2: 10,
    3: 37,
    4: 77,
    5: 123,
    6: 233,
    7: 353,
    8: 493,
    9: 699,
    10: 969,
    11: 1272,
    12: 1552,
    13: 1898,
    14: 2280,
    15: 2730,
    16: 3239,
    17: 3813,
    18: 4463,
    19: 5178,
    20: 5958,
    21: 6858,
    22: 7818,
    23: 8838,
    24: 9878,
    25: 10958,
    26: 12118,
    27: 13318,
    28: 14668,
    29: 16178,
    30: 17858,
    31: 19718,
    32: 21778,
    33: 24058,
    34: 26578,
    35: 29368,
    36: 32418,
    37: 35778,
    38: 39458,
    39: 43478,
    40: 47898,
    41: 52898,
    42: 58398,
    43: 64498,
    44: 71998,
    45: 79798,
    46: 87898,
    47: 96298,
    48: 104998,
    49: 113998,
    50: 123298,
    51: 132898,
    52: 142798,
    53: 152998,
    54: 163498,
    55: 174298,
    56: 185398,
    57: 196798,
    58: 208498,
    59: 220498,
    60: 232798,
    61: 245398,
    62: 258298,
    63: 271498,
    64: 284998,
    65: 298798,
    66: 312898,
    67: 327298,
    68: 341998,
    69: 356998,
    70: 372298,
    71: 387898,
    72: 403798,
    73: 419998,
    74: 436498,
    75: 453298,
    76: 470398,
    77: 487798,
    78: 505498,
    79: 523498,
    80: 541798,
    81: 560398,
    82: 579298,
    83: 598498,
    84: 617998,
    85: 637798,
    86: 657898,
    87: 678298,
    88: 698998,
    89: 719998,
    90: 741298,
    91: 762898,
    92: 784798,
    93: 806998,
    94: 829498,
    95: 852298,
    96: 875398,
    97: 898798,
    98: 922498,
    99: 946488  #946498
}

def xp_to_level(mode: int, xp: int) -> (None, int):
    levels = None
    if mode == 0:
        levels = MARIO_LEVELS
    elif mode == 1:
        levels = LUIGI_LEVELS
    if xp > levels[99]:  #greater than max level
        return 99
    for x in range(0, len(levels)):
        if x != 0 and x != 99:
            curr_level = levels[x]
            next_level = levels[x + 1]
            if xp == curr_level:  #equal to current level
                return x
            elif xp == next_level:  #equal to next level
                return x + 1
            elif curr_level <= xp <= next_level:  #between levels
                return x

if __name__ == "__main__":
    parser = ArgumentParser(description="A save editor for Mario and Luigi Superstar Saga for 3DS")

    #I/O
    parser.add_argument("-i", "--in-file", type=str, default="ML1_001.sav", help="The input save file")
    parser.add_argument("-o", "--out-file", type=str, help="The output save file")

    #modifications
    #experience and leveling
    parser.add_argument("--mario-level", type=int, help="The level you want Mario to have")
    parser.add_argument("--luigi-level", type=int, help="The level you want Luigi to have")

    #gold
    parser.add_argument("--gold", type=int, help="The amount of gold you want")

    #items
    #mushrooms
    parser.add_argument("--mushrooms", type=int, help="The amount of mushrooms you want")
    parser.add_argument("--super-mushrooms", type=int, help="The amount of super mushrooms you want")
    parser.add_argument("--ultra-mushrooms", type=int, help="The amount of ultra mushrooms you want")
    parser.add_argument("--max-mushrooms", type=int, help="The amount of max mushrooms you want")
    #nuts
    parser.add_argument("--nuts", type=int, help="The amount of nuts you want")
    parser.add_argument("--super-nuts", type=int, help="The amount of super nuts you want")
    parser.add_argument("--ultra-nuts", type=int, help="The amount of ultra nuts you want")
    parser.add_argument("--max-nuts", type=int, help="The amount of max nuts you want")
    #syrups
    parser.add_argument("--syrups", type=int, help="The amount of syrups you want")
    parser.add_argument("--super-syrups", type=int, help="The amount of super syrups you want")
    parser.add_argument("--ultra-syrups", type=int, help="The amount of ultra syrups you want")
    parser.add_argument("--max-syrups", type=int, help="The amount of max syrups you want")
    #1-ups
    parser.add_argument("--one-ups", type=int, help="The amount of 1-ups you want")
    parser.add_argument("--one-up-supers", type=int, help="The amount of 1-up supers you want")
    #misc
    parser.add_argument("--golden-mushrooms", type=int, help="The amount of golden mushrooms you want")
    parser.add_argument("--refreshing-herbs", type=int, help="The amount of refreshing herbs you want")
    parser.add_argument("--boo-biscuits", type=int, help="The amount of boo biscuits you want")
    parser.add_argument("--red-peppers", type=int, help="The amount of red peppers you want")
    parser.add_argument("--green-peppers", type=int, help="The amount of green peppers you want")

    #beans
    parser.add_argument("--woo-beans", type=int, help="The amount of woo beans you want")
    parser.add_argument("--hoo-beans", type=int, help="The amount of hoo beans you want")
    parser.add_argument("--chuckle-beans", type=int, help="The amount of chuckle beans you want")
    parser.add_argument("--hee-beans", type=int, help="The amount of hee beans you want")

    #maxing
    parser.add_argument("--max-gold", action="store_true", help="Set gold to 999999")
    parser.add_argument("--max-levels", action="store_true", help="Set Mario and Luigi's XP to 999999")
    parser.add_argument("--max-beans", action="store_true", help="Set all beans to 99")
    parser.add_argument("--max-items", action="store_true", help="Set all items to 99")
    parser.add_argument("--max-all", action="store_true", help="Max gold, XP, beans, and items")

    #listing
    parser.add_argument("--list-mario-xp", action="store_true", help="List Mario's current XP")
    parser.add_argument("--list-luigi-xp", action="store_true", help="List Luigi's current XP")
    parser.add_argument("--list-mario-bonuses", action="store_true", help="List Mario's bonus attributes")
    parser.add_argument("--list-luigi-bonuses", action="store_true", help="List Luigi's bonus attributes")
    parser.add_argument("--list-xp", action="store_true", help="List both Mario and Luigi's XP")
    parser.add_argument("--list-gold", action="store_true", help="List your current gold")
    parser.add_argument("--list-items", action="store_true", help="List all items")
    parser.add_argument("--list-beans", action="store_true", help="List all beans")
    #parser.
    parser.add_argument("--list-all", action="store_true", help="List everything")

    args = parser.parse_args()

    assert isfile(args.in_file), "Save file not found!"

    save_data = open(args.in_file, "rb").read()
    bio = BytesIO(save_data)

    assert len(save_data) == 0x12510, "Invalid save file size!"

    #listing
    #mario xp
    if args.list_mario_xp or args.list_xp or args.list_all:
        bio.seek(MARIO_XP_LOC)
        mario_xp = unpack("<i", bio.read(4))[0]
        print("Mario XP: %s -> Level: %s" % (mario_xp, xp_to_level(0, mario_xp)))

    #mario bonuses
    if args.list_mario_bonuses or args.list_all:
        bio.seek(MARIO_BONUS_HP_LOC)
        print("Mario Bonus HP:     %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Mario Bonus BP:     %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Mario Bonus POW:    %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Mario Bonus DEF:    %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Mario Bonus SPEED:  %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Mario Bonus STACHE: %s" % (unpack("<h", bio.read(2))[0]))

    #luigi xp
    if args.list_luigi_xp or args.list_xp or args.list_all:
        bio.seek(LUIGI_XP_LOC)
        luigi_xp = unpack("<i", bio.read(4))[0]
        print("Luigi XP: %s -> Level: %s" % (luigi_xp, xp_to_level(1, luigi_xp)))

    #luigi bonuses
    if args.list_luigi_bonuses or args.list_all:
        bio.seek(LUIGI_BONUS_HP_LOC)
        print("Luigi Bonus HP:     %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Luigi Bonus BP:     %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Luigi Bonus POW:    %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Luigi Bonus DEF:    %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Luigi Bonus SPEED:  %s" % (unpack("<h", bio.read(2))[0]))
        bio.seek(bio.tell() + 2)
        print("Luigi Bonus STACHE: %s" % (unpack("<h", bio.read(2))[0]))

    #gold
    if args.list_gold or args.list_all:
        bio.seek(GOLD_LOC)
        print("Gold: %s" % (unpack("<i", bio.read(4))[0]))

    #items
    if args.list_items or args.list_all:
        bio.seek(ITEM_START)
        print("Mushrooms:        %s" % (bio.read(1)[0]))
        print("Super Mushrooms:  %s" % (bio.read(1)[0]))
        print("Ultra Mushrooms:  %s" % (bio.read(1)[0]))
        print("Max Mushrooms:    %s" % (bio.read(1)[0]))

        print("Nuts:             %s" % (bio.read(1)[0]))
        print("Super Nuts:       %s" % (bio.read(1)[0]))
        print("Ultra Nuts:       %s" % (bio.read(1)[0]))
        print("Max Nuts:         %s" % (bio.read(1)[0]))

        print("Syrups:           %s" % (bio.read(1)[0]))
        print("Super Syrups:     %s" % (bio.read(1)[0]))
        print("Ultra Syrups:     %s" % (bio.read(1)[0]))
        print("Max Syrups:       %s" % (bio.read(1)[0]))

        print("1-Up Mushrooms    %s" % (bio.read(1)[0]))
        print("1-Up Supers:      %s" % (bio.read(1)[0]))

        print("Golden Mushrooms  %s" % (bio.read(1)[0]))
        print("Refreshing Herbs: %s" % (bio.read(1)[0]))
        print("Boo Biscuits:     %s" % (bio.read(1)[0]))
        print("Red Peppers:      %s" % (bio.read(1)[0]))
        print("Green Peppers:    %s" % (bio.read(1)[0]))

    #beans
    if args.list_beans or args.list_all:
        bio.seek(BEAN_START)
        print("Woo Beans:     %s" % (bio.read(1)[0]))
        print("Hoo Beans:     %s" % (bio.read(1)[0]))
        print("Chuckle Beans: %s" % (bio.read(1)[0]))
        print("Hee Beans:     %s" % (bio.read(1)[0]))

    #modifications
    #max levels
    if args.max_levels or args.max_all:
        bio.seek(MARIO_XP_LOC)
        bio.write(pack("<i", MARIO_LEVELS[99]))
        bio.seek(LUIGI_XP_LOC)
        bio.write(pack("<i", LUIGI_LEVELS[99]))
    else:  #set xp
        #mario level
        if args.mario_level is not None and 1 <= args.mario_level <= 99:
            bio.seek(MARIO_XP_LOC)
            bio.write(pack("<i", MARIO_LEVELS[args.mario_level]))
        #luigi level
        if args.luigi_level is not None and 1 <= args.luigi_level <= 99:
            bio.seek(LUIGI_XP_LOC)
            bio.write(pack("<i", LUIGI_LEVELS[args.luigi_level]))

    #max money
    if args.max_gold or args.max_all:
        bio.seek(GOLD_LOC)
        bio.write(pack("<i", 999999))
    elif args.gold is not None and 0 <= args.gold <= 999999:  #set gold
        bio.seek(GOLD_LOC)
        bio.write(pack("<i", args.gold))

    #max items
    if args.max_items or args.max_all:
        bio.seek(ITEM_START)
        for x in range(ITEM_LEN):
            bio.write(bytes([99]))
    else:  #set items
        bio.seek(ITEM_START)
        curr_vals = bytearray(bio.read(ITEM_LEN))
        items = [
            #mushrooms
            args.mushrooms,
            args.super_mushrooms,
            args.ultra_mushrooms,
            args.max_mushrooms,
            #nuts
            args.nuts,
            args.super_nuts,
            args.ultra_nuts,
            args.max_nuts,
            #syrups
            args.syrups,
            args.super_syrups,
            args.ultra_syrups,
            args.max_syrups,
            #one ups
            args.one_ups,
            args.one_up_supers,
            #misc
            args.golden_mushrooms,
            args.refreshing_herbs,
            args.boo_biscuits,
            args.red_peppers,
            args.green_peppers
        ]
        for x in range(len(items)):
            if items[x] is not None and 0 <= items[x] <= 99:
                curr_vals[x] = items[x]
        bio.seek(ITEM_START)
        bio.write(bytearray(curr_vals))

    #max beans
    if args.max_beans or args.max_all:
        bio.seek(BEAN_START)
        for x in range(BEAN_LEN):
            bio.write(bytes([99]))
    else:  #set beans
        bio.seek(BEAN_START)
        curr_vals = bytearray(bio.read(4))
        if args.woo_beans is not None and 0 <= args.woo_beans <= 99:
            curr_vals[0] = args.woo_beans
        if args.hoo_beans is not None and 0 <= args.hoo_beans <= 99:
            curr_vals[1] = args.hoo_beans
        if args.chuckle_beans is not None and 0 <= args.chuckle_beans <= 99:
            curr_vals[2] = args.chuckle_beans
        if args.hee_beans is not None and 0 <= args.hee_beans <= 99:
            curr_vals[3] = args.hee_beans
        bio.seek(BEAN_START)
        bio.write(bytearray(curr_vals))

    out_data = bio.getvalue()

    if args.out_file is not None:
        open(args.out_file, "wb").write(out_data)