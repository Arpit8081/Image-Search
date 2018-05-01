import csv
import jellyfish
keywords=['scenenumbers','helicopter','hotairballoon','cloud','sun','lightning', 'rain','rocket','airplane','bouncy','slide','sandbox', 'grill','swing','tent','table','pinetree','oaktree', 'appletree','boy','girl','bear','cat','dog','duck','owl', 'snake','baseballcap','crown','chefhat', 'piratehat','wintercap','bennie','wizardhat','vikinghat', 'purpleglasses','sunglasses','pie','pizza','hotdog','ketchup', 'mustard','hamburger','soda','baseball','pail','beachball', 'basketball','soccerball','tennisball','football', 'frisbee','baseballbat','balloons','baseballglove','shovel', 'tennisracket','kite','fire']
hierarchy=['','sky','gloomy','wet','fourlegs','ground','sit','white','head','kitchen','circular','tasty','crusty','play','nets','grandslam']
with open('image_tags.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    i=59
    j=500
    twodimensional = [[0 for x in range(i)] for y in range(j)]
    p=0
    for row in readCSV:
        for i in range (0,59):
            twodimensional[p][i] = (row[i])

        p=p+1
csvfile.close()

list_constant =[0 for x in range(59)]
list_variable =[0 for x in range(59)]
position=[0 for y in range(500)]
counter=[0 for y in range(500)]
print(" enter the postion of image to be queried")
ans = int(input ('10 for 301_0 93 for 309_3 '))
for column in range(0,59):
    list_constant[column]= twodimensional[ans][column]
print("\n *******list of characters in the image******")
print(list_constant)
for row in range(0,500):
    for column in range(0,59):
        list_variable[column]=twodimensional[row][column]
        if list_constant[column]==list_variable[column]==" 1":
            counter[row]=counter[row]+1

print("unsorted match count:")
print(counter)

for longlist in range(0,len(counter)):
    for i in range(longlist):
        if counter[i] < counter[i+1]:
            r=twodimensional[i][0]
            temp = counter[i]
            twodimensional[i][0]=twodimensional[i+1][0]
            counter[i] = counter[i+1]
            twodimensional[i+1][0]=r
            counter[i+1] = temp
print("************20 of the most similar images :***********")
for i in range(0,20):
    print(" position", i+1," ", end='')
    print(" ",twodimensional[i][0])