from io import BytesIO
from struct import pack, unpack
from argparse import ArgumentParser
from binascii import hexlify as _hexlify

MARIO_BLOB_START = 0x00
MARIO_BLOB_LEN = 0x28
MARIO_EXP_LOC = 0x00  #int32

LUIGI_BLOB_START = 0x28
LUIGI_BLOB_LEN = 0x28
LUIGI_EXP_LOC = 0x28  #int32

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
    save_data = open("unmodded/ML1_001.sav", "rb").read()
    bio = BytesIO(save_data)

    #Mario's stats
    print("Mario Stats:")
    mario_block = bio.read(MARIO_BLOB_LEN)
    m_bio = BytesIO(mario_block)
    #print(hexlify(mario_block))
    print("HP: %s" % (unpack("<h", m_bio.read(2))[0]))
    print("BP: %s" % (unpack("<h", m_bio.read(2))[0]))
    m_bio.seek(0x1C)
    print("XP: %s" % (unpack("<i", m_bio.read(4))[0]))

    #Luigi's stats
    print("Luigi Stats:")
    luigi_block = bio.read(LUIGI_BLOB_LEN)
    l_bio = BytesIO(luigi_block)
    #print(hexlify(luigi_block))
    print("HP: %s" % (unpack("<h", l_bio.read(2))[0]))
    print("BP: %s" % (unpack("<h", l_bio.read(2))[0]))
    l_bio.seek(0x1C)
    print("XP: %s" % (unpack("<i", l_bio.read(4))[0]))

    #Gold
    print("Gold: %s" % (unpack("<i", bio.read(4))[0]))

    #items
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
    bio.seek(BEAN_START)
    print("Woo Beans:     %s" % (bio.read(1)[0]))
    print("Hoo Beans:     %s" % (bio.read(1)[0]))
    print("Chuckle Beans: %s" % (bio.read(1)[0]))
    print("Hee Beans:     %s" % (bio.read(1)[0]))

    #modifications
    #mario xp
    m_bio.seek(0x1C)
    m_bio.write(pack("<i", 999999))

    #luigi xp
    l_bio.seek(0x1C)
    l_bio.write(pack("<i", 999999))

    #write the blobs back
    bio.seek(0x50)
    bio.write(pack("<i", 9999999))

    #max money
    bio.seek(GOLD_LOC)
    bio.write(pack("<i", 999999))

    #max items
    for x in range(ITEM_START, ITEM_START + ITEM_LEN):
        bio.seek(x)
        bio.write(bytes([99]))

    #max beans
    for x in range(BEAN_START, BEAN_START + BEAN_LEN):
        bio.seek(x)
        bio.write(bytes([99]))

    #flush the changes
    mario_block = m_bio.getvalue()
    luigi_block = l_bio.getvalue()
    bio.seek(0)
    bio.write(mario_block)
    bio.write(luigi_block)

    out_data = bio.getvalue()

    open("modded/ML1_001.sav", "wb").write(out_data)