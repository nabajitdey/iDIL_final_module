from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .serializers import *
from .forms import *
from .classes_sorting import Sorting
from integrated_nlp.classify_questions import TextAnalysis

from cv2 import cv2
import numpy as np

#image upload
def hotel_image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print("ok1.1")
        if form.is_valid():
            print("okkk")
            form.save()
            sorting = Sorting()
            sorting.image_upload_and_detect()
            # print(Image.objects.latest('id').image)
            return redirect('success')
    else:
        print("notok")
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
    # return render(request, 'index.html', {})

#image upload
def success(request):
    return HttpResponse('successfully uploaded')

#uploading the classes and groups in db
class ObjectsDbUploadViewSet(generics.GenericAPIView):
    serializer_class = ObjectsSerializer

    def post(self, request, *args, **kwargs):
        sorting=Sorting()
        sorting.sort_and_db_upload()
        ob=Object.objects.get(name="beef carpaccio")
        print(ob.name)
        print(len(ob.name))
        ob = Object.objects.get(name="sashimi")
        print(ob.name)
        print(len(ob.name))
        ob = Object.objects.get(name="bathing cap")
        print(ob.name)
        print(len(ob.name))
        ob = Object.objects.get(name="bathtub")
        print(ob.name)
        print(len(ob.name))
        ob = Object.objects.get(name="apartment building")
        print(ob.name)
        print(len(ob.name))
        ob = Object.objects.get(name="arch")
        print(ob.name)
        print(len(ob.name))
        return Response({"success":"success"})

#image detection
class ImageDetectionViewSet(generics.GenericAPIView):
    serializer_class = ObjectsSerializer

    def post(self, request, *args, **kwargs):
        sorting= Sorting()
        sorting.image_detect()

        return Response({"success":"success"})

#text analysis
class TextAnalysisViewSet(generics.GenericAPIView):
    serializer_class = ObjectsSerializer

    def post(self, request, *args, **kwargs):
        t=TextAnalysis()
        result= t.textAnalysis(request.data["text"])
        return Response({
            "question type": result["question_type"],
            "answer": result["answer"],
            "group objects":result["group_objects"],
            "images": result["image_list"]
        })


class AffirmationQuestionViewSet(generics.GenericAPIView):
    serializer_class = ObjectsSerializer

    def post(self, request, *args, **kwargs):
        request_object_name=request.data["name"]
        success="failure"
        hotel=Hotel.objects.get(name="Taj Bengal")
        try:
            db_object=Object.objects.get(name=request_object_name)
            print("ok1")
            for i in db_object.hotels.all():
                if i==hotel:
                    print("ok2")
                    success="success"
        except Object.DoesNotExist:
            success="failure"

        return Response({"success":success})

class ListQuestionViewSet(generics.GenericAPIView):
    serializer_class = ObjectsSerializer

    def post(self, request, *args, **kwargs):
        request_group_name=request.data["name"]
        success="failure"
        hotel=Hotel.objects.get(name="Taj Bengal")
        print("ok0")
        try:
            db_group=Group.objects.get(name=request_group_name)
            print("ok1")
            db_group_objects=db_group.object_name.all()
            print("ok2")
            db_group_objects_set=set(db_group_objects)

            hotel_objects=hotel.object_set.all()
            hotel_objects_set=set(hotel_objects)

            if(db_group_objects_set & hotel_objects_set):
                common_objects=(db_group_objects_set & hotel_objects_set)
                print(common_objects)
            for c in common_objects:
                print(c.name)
                for i in c.images.all():
                    if i.hotel==hotel:
                        print("yas-1")
                        print(i.image)
                        print("yas")

            print("ok1")
        except Object.DoesNotExist:
            success="failure"

        return Response({"success":success})