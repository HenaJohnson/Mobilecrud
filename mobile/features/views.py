from django.shortcuts import render, redirect
from django.views.generic import View
from features.forms import Mobileform
from features.models import Mobilemodel

# Create your views here.


class MobileView(View):
    def get(self, request):
        form = Mobileform()
        return render(request, "mob.html", {"result": form})

    def post(self, request):
        form = Mobileform(request.POST)
        if form.is_valid():
            Mobilemodel.objects.create(**form.cleaned_data)
        else:
            print("get out")

        return render(request, "mob.html", {"result": form})


class MobileList(View):
    def get(self, request):
        qs = Mobilemodel.objects.all()
        return render(request, "mob_list.html", {"result": qs})

    def post(self, request):
        brand = request.POST.get("brand")
        qs = Mobilemodel.objects.filter(brand=brand)
        return render(request, "mob_list.html", {"result": qs})


class MobileDetail(View):
    def get(self, request, **kwargs):
        print(kwargs)
        id = kwargs.get("pk")  # dynamic :id=1 static data
        qs = Mobilemodel.objects.get(id=id)
        return render(request, "mob_detail.html", {"result": qs})


class Mobiledelete(View):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        Mobilemodel.objects.get(id=id).delete()
        return redirect('det')


class Mobileupdate(View):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        obj = Mobilemodel.objects.get(id=id)
        form = Mobileform(instance=obj)
        return render(request, "mob_edit.html", {"form": form})

    def post(self, request, **kwargs):
        id = kwargs.get("pk")
        obj = Mobilemodel.objects.get(id=id)
        form = Mobileform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        else:
            print("get out")

        return redirect('det')
