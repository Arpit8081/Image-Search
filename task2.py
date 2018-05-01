import csv
import jellyfish
image_tags=['scenenumbers','helicopter','hotairballoon','cloud','sun','lightning','rain','rocket','airplane','bouncy','slide','sandbox', 'grill','swing','tent','table','pinetree','oaktree', 'appletree','boy','girl','bear','cat','dog','duck','owl', 'snake','baseballcap','crown','chefhat', 'piratehat','wintercap','bennie','wizardhat','vikinghat', 'purpleglasses','sunglasses','pie','pizza','hotdog','ketchup', 'mustard','hamburger','soda','baseball','pail','beachball', 'basketball','soccerball','tennisball','football', 'frisbee','baseballbat','balloons','baseballglove','shovel', 'tennisracket','kite','fire']

advanced=['','sky','gloomy','wet','fourlegs','ground','sit','white','head','kitchen','circular','tasty','crusty', 'play','nets','grandslam']
with open('image_tags.csv', 'r') as myFile:
    readCSV = csv.reader(myFile, delimiter=',')
    i = 59
    j = 500
    twodimensional=[[0 for x in range(i)] for y in range(j)]
    for row in readCSV:
        for i in range (0,59):
            twodimensional[p][i] = (row[i])
        p = p+1
myFile.close()
choice = input('enter the metadata vocabulary ')

def basic(word):
    threshold=0
    vertical=0
    horizontal =0
    for vertical in range (0,59):
        threshold=jellyfish.jaro_distance(word, image_tags[vertical ])
        if threshold > .8:
            print (" ",image_tags[vertical ])
            for horizontal in range (0,500):
                if (twodimensional[horizontal ][vertical ]) == " 1":
                    print ("Image Number Is ",twodimensional[horizontal ][0])
def additional(word):
    vertical =0
    horizontal =0
    for vertical in range(0,16):
        if word == advanced[vertical ]:
            if vertical <= 3:
                print (" **********query executed search for :"+image_tags[6])
                for horizontal in range (0,500):
                    if (twodimensional[horizontal ][6]) == " 1":
                        print (twodimensional[horizontal ][0])

            elif vertical > 3 and vertical <= 6:
                print (" *******query executed search for :"+image_tags[15])
                for horizontal in range (0,500):
                    if (twodimensional[horizontal ][15]) == " 1":
                        print (twodimensional[horizontal ][0])

            elif vertical > 6 and vertical <= 9:
                print (" ***********query executed search for :"+image_tags[29])
                for horizontal in range (0,500):
                    if (twodimensional[horizontal ][29]) == " 1":
                        print (twodimensional[horizontal ][0])

            elif vertical > 9 and vertical <= 12:
                print (" ***********query executed search for :"+image_tags[38])
                for horizontal in range (0,500):
                    if (twodimensional[horizontal ][38]) == " 1":
                        print (twodimensional[horizontal ][0])

            else:
                print(" *************query executed search for :"+image_tags[56] )
                for horizontal in range (0,500):
                    if (twodimensional[horizontal ][56]) == " 1":
                        print (twodimensional[horizontal ][0])

an=choice.split(" ")
for leg in range(0,len(an)):
    basic(an[leg])
for piece in range(0,len(an)):
    additional(an[piece])