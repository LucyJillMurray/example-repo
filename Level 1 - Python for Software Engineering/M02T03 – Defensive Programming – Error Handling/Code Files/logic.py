# This is meant to go from one star to five back down to two
# When it goes down it goes from five to three.
stars="*"
for i in range(0,7):
    if i < 5:
        stars1 = stars + stars * i
        print(stars1)
    else:
        stars1 = stars + stars*(7 -i)
        print(stars1)