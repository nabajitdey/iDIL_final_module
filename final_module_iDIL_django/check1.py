import json

with open('resnet50json.json') as json_file:
    data = json.load(json_file)
    file1 = open("resnet50classes.txt", "w")
    for i in range(0,1000):
        print(data[str(i)][1].replace("_"," "))
        str0=""
        str0=data[str(i)][1]
        print("before")
        print(len(str0))
        print(str0)
        if str0.__contains__(" "):
            str0 = str0[:str0.rindex(" ")]
        str0= str0.replace("_"," ")
        print("after")
        print(len(str0))
        print(str0)
        file1.write(str0.replace("_"," "))
        file1.write("\n")

    file1.close()


# file1=open("food101.txt","r+")
# file2=open("food101_classes.txt","w")
#
# for f in file1.readlines():
#     print("before")
#     print(len(f))
#     print(f)
#     if f.__contains__("\n"):
#     #     print("yes")
#     # print(f[9])
#         str=f[:f.rindex("\n")]
#         str=str.replace("_"," ")
#         print("afer")
#         print(str)
#         print(len(str))
#         file2.write(str)
#         file2.write("\n")
#     else:
#         str = f[:]
#         str = str.replace("_", " ")
#         print("afer")
#         print(str)
#         print(len(str))
#         file2.write(str)
#         file2.write("\n")
#
# file1.close()
# file2.close()
#

# file1=open("categories_places365.txt", "r+")
# # print(file1.read())
# file2 = open("catagories_places365_classes.txt", "w")
# for f in file1.readlines():
#     str=f[3:]
#     if str.__contains__("/"):
#         str1=str[:str.rindex("/")]
#         str2= str[str.rindex("/")+1:str.rindex(" ")]
#         str1 = str1.replace("_", " ")
#         str2 = str2.replace("_", " ")
#         print(str1)
#         file2.write(str1)
#         file2.write("\n")
#         print(str2)
#         file2.write(str2)
#         file2.write("\n")
#     else:
#         str=str[:str.rindex(" ")]
#         str=str.replace("_"," ")
#         print(str)
#         file2.write(str)
#         file2.write("\n")
#     # print(str)
#
# file1.close()


# file1=open("categories_places365.txt", "r+")
# # print(file1.read())
# file2 = open("catagories_places365_classes.txt", "w")
# for f in file1.readlines():
#     str=f[3:]
#     if str.__contains__("/"):
#         str1=str[:str.rindex("/")]
#         str1 = str1.replace("_", " ")
#         str= str[str.rindex("/")+1:str.rindex(" ")+1]+str1
#         str = str.replace("_", " ")
#         file2.write(str1)
#         file2.write("\n")
#         file2.write(str)
#         file2.write("\n")
#     else:
#         str=str[:str.rindex(" ")]
#         str=str.replace("_"," ")
#         print(str)
#         file2.write(str)
#         file2.write("\n")
#     # print(str)
#
# file1.close()




#wheat field wind farm windmill waterfall wave water park volcano vineyard valley ocean deep underwater temple soccer stadium stadium football stadium baseball stadium soccer field shopping mall science museum rope bridge river rice paddy rainforest racecourse raceway pagoda palace ocean natural history museum music studio outdoor museum museum indoor museum mountain snowy mountain path mountain mosque medina market outdoor market indoor market lighthouse
# natural lake lake lagoon iceberg igloo hayfield football field forest broadleaf forest forest path forest road farm dam desert sand desert vegetation desert corral corn field coast cliff  church outdoor church indoor church castle cemetery catacomb canyon canal natural canal urban canal bullring burial chamber bridge boxing ring botanical garden beach bazaar archaelogical excavation amusement park amusement arcade
# army base
# art gallery
# art school
# art studio
# artists loft bamboo forest
# bazaar
# indoor bazaar
# bazaar
# outdoor bazaar
# beach
# beach house campsite candy store department store fastfood restaurant
# field
# cultivated field
# wild field
# fishpond
# flea market
# indoor flea market
# florist shop
# indoor florist shop
# football field
# forest
# broadleaf forest
# forest path
# forest road
# formal garden
# fountain
# galley
# gas station
#general store
# indoor general store
# general store
# outdoor general store
# gift shop
# glacier
# harbor
# hardware store
# hayfield
# heliport
# hospital
# hospital room
# hunting lodge
# outdoor hunting lodge
# jewelry shop
# kasbah
# lagoon
# lake
# natural lake
# market
# indoor market
# market
# outdoor market
#mausoleum
# medina
#  pet shop
# pharmacy
# phone booth
# repair shop
# river
# rock arch
# roof garden
# rope bridge
# shopping mall
# indoor shopping mall
# ski resort
# ski slope
# subway station
# platform subway station
# supermarket
# synagogue
# asia temple
# topiary garden
# tower
# toyshop
# veterinarians office
# viaduct
# village
# vineyard
# volcano
# water tower
# waterfall
# watering hole
# wave
# zen garden




#platform train station train station subway station platform subway station railroad track indoor bus station bus station airfield airplane cabin airport terminal

#
# indoor swimming pool swimming pool outdoor swimming pool swimming hole

