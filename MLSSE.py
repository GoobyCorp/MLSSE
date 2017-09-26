#!/usr/bin/python3

from io import BytesIO
from os.path import isfile
from struct import pack, unpack
from argparse import ArgumentParser
from binascii import hexlify as _hexlify

MARIO_BLOB_START = 0x00
MARIO_BLOB_LEN = 0x28
MARIO_XP_LOC = 0x00  #int32

LUIGI_BLOB_START = 0x28
LUIGI_BLOB_LEN = 0x28
LUIGI_XP_LOC = 0x28  #int32

GOLD_LOC = 0x50  #int32

#int8's
ITEM_START = 0x54
ITEM_LEN = 0x12

#int8's
BEAN_START = 0x130
BEAN_LEN = 4

def hexlify(b: (bytes, bytearray)) -> str:
    return str(_hexlify(b), "utf8")

if __name__ == "__main__":
    parser = ArgumentParser(description="A save editor for Mario and Luigi Superstar Saga for 3DS")

    #I/O
    parser.add_argument("-i", "--in-file", type=str, default="ML1_001.sav", help="The input save file")
    parser.add_argument("-o", "--out-file", type=str, default="ML1_001_modded.sav", help="The output save file")

    #modifications
    #experience
    parser.add_argument("--mario-xp", type=int, help="The amount of XP you want Mario to have")
    parser.add_argument("--luigi-xp", type=int, help="The amount of XP you want Luigi to have")

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

    #max all
    parser.add_argument("--max-gold", action="store_true", help="Set gold to 999999")
    parser.add_argument("--max-xp", action="store_true", help="Set Mario and Luigi's XP to 999999")
    parser.add_argument("--max-beans", action="store_true", help="Set all beans to 99")
    parser.add_argument("--max-items", action="store_true", help="Set all items to 99")
    parser.add_argument("--max-all", action="store_true", help="Max gold, XP, beans, and items")

    #listing
    parser.add_argument("--list-mario-xp", action="store_true", help="List Mario's current XP")
    parser.add_argument("--list-luigi-xp", action="store_true", help="List Luigi's current XP")
    parser.add_argument("--list-gold", action="store_true", help="List your current gold")
    parser.add_argument("--list-items", action="store_true", help="List all items")
    parser.add_argument("--list-beans", action="store_true", help="List all beans")

    args = parser.parse_args()

    assert isfile(args.in_file), "Save file not found!"

    save_data = open(args.in_file, "rb").read()
    bio = BytesIO(save_data)

    #listing
    #mario xp
    if args.list_mario_xp:
        bio.seek(MARIO_XP_LOC)
        print("Mario XP: %s" % (unpack("<i", bio.read(4))[0]))

    #luigi xp
    if args.list_luigi_xp:
        bio.seek(LUIGI_XP_LOC)
        print("Luigi XP: %s" % (unpack("<i", bio.read(4))[0]))

    #gold
    if args.list_gold:
        print("Gold: %s" % (unpack("<i", bio.read(4))[0]))

    #items
    if args.list_items:
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
    if args.list_beans:
        bio.seek(BEAN_START)
        print("Woo Beans:     %s" % (bio.read(1)[0]))
        print("Hoo Beans:     %s" % (bio.read(1)[0]))
        print("Chuckle Beans: %s" % (bio.read(1)[0]))
        print("Hee Beans:     %s" % (bio.read(1)[0]))

    #modifications
    #max xp
    if args.max_xp or args.max_all:
        bio.seek(MARIO_XP_LOC)
        bio.write(pack("<i", 9999999))
        bio.seek(LUIGI_XP_LOC)
        bio.write(pack("<i", 9999999))
    else:  #set xp
        #mario xp
        if args.mario_xp is not None and 0 <= args.mario_xp <= 9999999:
            bio.seek(MARIO_XP_LOC)
            bio.write(pack("<i", args.mario_xp))
        #luigi xp
        if args.luigi_xp is not None and 0 <= args.luigi_xp <= 9999999:
            bio.seek(LUIGI_XP_LOC)
            bio.write(pack("<i", args.luigi_xp))

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

    open(args.out_file, "wb").write(out_data)