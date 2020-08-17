from .models import *
from cv2 import cv2
import numpy as np
from .forms import *
import glob

from image_detection_algorithms.Engine import Engine
import os


class Sorting:

    def sort_and_db_upload(self):

        #food101
        recipies_group=Group(name="recipies")
        print(recipies_group.name)
        recipies_group.save()

        file1 = open(r"C:\Users\nabaj\source\repos\final_module_iDIL_django\food101_classes.txt","r+")
        for f in file1.readlines():
            print("before")
            print(len(f))
            f=f[:len(f)-1]
            print("after")
            print(len(f))
            recipie=Object(name=f)
            print(recipie.name)
            recipie.save()
            recipies_group.object_name.add(recipie.pk)
            recipies_group.save()
            print(len(recipie.name))

        file1.close()

        #resnet50
        amenities_group=Group(name="amenities")
        print(amenities_group.name)
        amenities_group.save()

        file2 = open(r"C:\Users\nabaj\source\repos\final_module_iDIL_django\resnet50classes.txt","r+")
        for f in file2.readlines():
            f = f[:len(f) - 1]
            amenity=Object(name=f)
            print(amenity.name)
            amenity.save()
            amenities_group.object_name.add(amenity.pk)
            amenities_group.save()

        file2.close()

        #catagories_places365
        facilities_group=Group(name="facilities")
        landmarks_group=Group(name="landmarks")
        essential_places_group=Group(name="essential places")
        transportations_group=Group(name="transportations")
        swimming_pools_group=Group(name="swimming pools")

        print(facilities_group.name)
        print(landmarks_group.name)
        print(essential_places_group.name)
        print(transportations_group.name)
        print(swimming_pools_group.name)

        facilities_group.save()
        landmarks_group.save()
        essential_places_group.save()
        transportations_group.save()
        swimming_pools_group.save()

        l_list = [
            "wheat field",
            "wind farm",
            "windmill",
            "waterfall",
            "wave",
            "water park",
            "volcano",
            "vineyard",
            "valley",
            "ocean",
            "deep underwater",
            "temple",
            "soccer stadium",
            "stadium",
            "football stadium",
            "baseball stadium",
            "soccer field",
            "shopping mall",
            "science museum",
            "rope bridge",
            "river",
            "rice paddy",
            "rainforest",
            "racecourse",
            "raceway",
            "pagoda",
            "palace",
            "natural history museum",
            "music studio",
            "outdoor museum",
            "museum",
            "indoor museum",
            "mountain",
            "mountain snowy",
            "mountain path",
            "mosque",
            "medina",
            "market outdoor",
            "market indoor",
            "market lighthouse",
            "natural lake",
            "lake",
            "lagoon",
            "iceberg",
            "igloo",
            "hayfield",
            "football field",
            "forest",
            "broadleaf forest",
            "forest path",
            "forest road",
            "farm",
            "dam",
            "desert",
            "sand desert",
            "vegetation desert",
            "corral",
            "corn field",
            "coast",
            "cliff",
            "church outdoor",
            "church indoor",
            "church",
            "castle",
            "cemetery",
            "catacomb",
            "canyon",
            "canal",
            "natural canal",
            "urban canal",
            "bullring",
            "burial chamber",
            "bridge",
            "boxing ring",
            "botanical garden",
            "beach",
            "bazaar",
            "archaelogical excavation",
            "amusement park",
            "amusement arcade",
            "army base",
            "art gallery",
            "art school",
            "art studio",
            "artists loft",
            "bamboo forest",
            "beach house",
            "campsite",
            "wild field",
            "fishpond",
            "flea market",
            "indoor flea market",
            "broadleaf forest",
            "formal garden",
            "fountain",
            "galley",
            "glacier",
            "harbor",
            "hunting lodge",
            "outdoor hunting lodge",
            "kasbah",
            "lake",
            "natural lake",
            "mausoleum",
            "rock arch",
            "roof garden",
            "rope bridge",
            "ski resort",
            "ski slope",
            "synagogue",
            "asia temple",
            "topiary garden",
            "village",
            "waterfall",
            "watering hole",
            "zen garden",
            "library",
            "indoor library",
            "outdoor library"
        ]

        e_p_list = [
            "candy store",
            "department store",
            "fastfood restaurant",
            "gas station",
            "general store",
            "indoor general store",
            "outdoor general store",
            "gift shop",
            "hardware store",
            "hospital",
            "hospital room",
            "jewelry shop",
            "market",
            "indoor market",
            "outdoor market",
            "pet shop",
            "pharmacy",
            "phone booth",
            "repair shop",
            "shopping mall",
            "indoor shopping mall",
            "supermarket",
            "toyshop",
            "veterinarians office",
        ]

        t_list = [
            "platform subway station",
            "subway station",
            "platform train station",
            "train station",
            "railroad track",
            "indoor bus station",
            "bus station",
            "airfield",
            "airplane cabin",
            "airport terminal"
        ]

        s_p_list = [
            "indoor swimming pool",
            "swimming pool",
            "outdoor swimming pool",
            "swimming hole"
        ]

        file3 = open(r"C:\Users\nabaj\source\repos\final_module_iDIL_django\catagories_places365_classes.txt","r+")

        for f in file3.readlines():
            f=f[:len(f)-1]
            str=f

            if str in s_p_list:
                c_p_object=Object(name=f)
                print(c_p_object.name)
                c_p_object.save()
                swimming_pools_group.object_name.add(c_p_object.pk)
                swimming_pools_group.save()
                facilities_group.object_name.add(c_p_object.pk)
                facilities_group.save()

            elif str in t_list:
                c_p_object = Object(name=f)
                print(c_p_object.name)
                c_p_object.save()
                transportations_group.object_name.add(c_p_object.pk)
                transportations_group.save()

            elif str in e_p_list:
                c_p_object = Object(name=f)
                print(c_p_object.name)
                c_p_object.save()
                essential_places_group.object_name.add(c_p_object.pk)
                essential_places_group.save()

            elif str in l_list:
                c_p_object = Object(name=f)
                print(c_p_object.name)
                c_p_object.save()
                landmarks_group.object_name.add(c_p_object.pk)
                landmarks_group.save()

            else:
                c_p_object = Object(name=f)
                print(c_p_object.name)
                c_p_object.save()
                facilities_group.object_name.add(c_p_object.pk)
                facilities_group.save()

        file3.close()

    def image_upload(self):
        impath = r"C:\Users\nabaj\Pictures\hugsy7.jpg"
        img = cv2.imread(impath)
        # print(img)
        # form = ImageForm(open(impath))
        imw=Image(image=impath)
        imw.save()
        # if form.is_valid():
        #     form.save()
        #     print("yas")

    def image_detect(self):
        engine=Engine()
        final_objects=set()
        images_path = glob.glob(r"C:\Users\nabaj\Pictures\test101\*.jpg")
        hotel=Hotel.objects.get(pk=1)
        print(hotel.name)
        for img_path in images_path:
            indiv_list=[]
            indiv_list.append(engine.StartEngine(img_path))
            print("in view")
            print(indiv_list)
            if indiv_list:
                print("in if")
                image_object=Image(image=img_path)
                image_object.save()
                for i in indiv_list[0]:
                    str0=""
                    str0=str(i)
                    print(str0)
                    if str0.__contains__("/"):
                        str1=str0[:str0.rindex("/")]
                        str1 = str1.replace("_", " ")
                        str0= str0[str0.rindex("/")+1:len(str0)]+" "+str1
                        str0 = str0.replace("_", " ")
                        print(str0)
                        print(str1)
                        try:
                            object_detected1=Object.objects.get(name=str1)
                            if object_detected1:
                                object_detected1.images.add(image_object.pk)
                                object_detected1.save()
                                print("a*")
                                final_objects.add(str1)

                            object_detected2= Object.objects.get(name=str0)
                            if object_detected2:
                                object_detected2.images.add(image_object.pk)
                                object_detected2.save()
                                print("b*")
                                final_objects.add(str0)
                        except Object.DoesNotExist:
                            print("object not in DB")


                    else:
                        # str0=str0[:str0.rindex(" ")]
                        str0=str0.replace("_"," ")
                        print(str0)
                        print(len(str0))
                        # o=Object.objects.get(pk=5758)
                        # print(o.name)
                        # print(len(o.name))
                        try:
                            object_detected=Object.objects.get(name=str0)
                            print(len(object_detected.name))
                            if object_detected:
                                print("c*")
                                print(object_detected.name)
                                object_detected.images.add(image_object.pk)
                                object_detected.save()
                                final_objects.add(str0)
                        except Object.DoesNotExist:
                            print("object not in DB")

        if final_objects:
            for f in final_objects:
                print(final_objects)
                object_detected=Object.objects.get(name=f)
                object_detected.hotels.add(hotel.pk)
                object_detected.save()


    def image_upload_and_detect(self):
        print(Image.objects.latest('id').image)
        image_object=Image.objects.latest('id')
        hotel = Hotel.objects.get(pk=1)
        final_objects = set()
        indiv_list = []
        engine = Engine()
        base_path=r"C:\Users\nabaj\source\repos\final_module_iDIL_django\media"
        path=os.path.join(base_path,str(image_object.image))
        indiv_list.append(engine.StartEngine(path))
        print("in view")
        print(indiv_list)
        if indiv_list:
            print("in if")
            for i in indiv_list[0]:
                str0 = ""
                str0 = str(i)
                print(str0)
                if str0.__contains__("/"):
                    str1 = str0[:str0.rindex("/")]
                    str1 = str1.replace("_", " ")
                    str0 = str0[str0.rindex("/") + 1:len(str0)] + " " + str1
                    str0 = str0.replace("_", " ")
                    print(str0)
                    print(str1)
                    try:
                        object_detected1 = Object.objects.get(name=str1)
                        if object_detected1:
                            object_detected1.images.add(image_object.pk)
                            object_detected1.save()
                            print("a*")
                            final_objects.add(str1)

                        object_detected2 = Object.objects.get(name=str0)
                        if object_detected2:
                            object_detected2.images.add(image_object.pk)
                            object_detected2.save()
                            print("b*")
                            final_objects.add(str0)
                    except Object.DoesNotExist:
                        print("object not in DB")


                else:
                    # str0=str0[:str0.rindex(" ")]
                    str0 = str0.replace("_", " ")
                    print(str0)
                    print(len(str0))
                    # o=Object.objects.get(pk=5758)
                    # print(o.name)
                    # print(len(o.name))
                    try:
                        object_detected = Object.objects.get(name=str0)
                        print(len(object_detected.name))
                        if object_detected:
                            print("c*")
                            print(object_detected.name)
                            object_detected.images.add(image_object.pk)
                            object_detected.save()
                            final_objects.add(str0)
                    except Object.DoesNotExist:
                        print("object not in DB")

        if final_objects:
            for f in final_objects:
                print(final_objects)
                object_detected = Object.objects.get(name=f)
                object_detected.hotels.add(hotel.pk)
                object_detected.save()
