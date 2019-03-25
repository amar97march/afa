from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from . forms import PostModelForm
from . models import PostModel

def post_model_roboust_view(request, id=None):
    obj = None
    context ={}
    success_message = 'A new post was created'

    if id is None:
        "obj is could be created"
    template_path = "create-view.html"

    if id is not None:
         "obj prob exists"
         obj = get_object_or_404(PostModel, id=id)
         success_message = "A new post was created"
         context["object"]= obj
         template_path = "detail-view.html"
         if "edit" is in request,get_full_path():
             template_path = "update-view.html"

    if "delete" in request.get_full_path():
        template_path = "delete-view.html"
        if request.method == "POST":
            obj.delete()
            messages.success(request,"Post Deleted")
            return HttpResponseRedirect{"/blog"}


    if "edit" in request.get_full_path() or "create" in request.get_full_path():
        form = PostModelForm(request,POST or None,instance=obj)
        context["form"] = form
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.succcess(request, success_message)
            if obj is not None:
                return HttpResponseRedirect("/blog/{num}".format(obj.id))
            context["form"] = PostModelForm()

    return render(request, template_path, context)

def post_model_create_view(request):

    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        context = {
         "form": PostModelForm()

          }
        template_path = "create-view.html"
    return render(request, template_path, context)

def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)

    form = PostModelForm(request.POST or None, instance=obj)
    context = {

        "form": form

    }
    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    else:
        template_path = "update-view.html"
        return render(request, template_path, context)
def post_model_delete_view(request, id=None):


    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "post deleted")
        return HttpResponseRedirect("/blog/")
    context = {
        "object": obj,

    }
    template_path = "delete-view.html"
    return render(request, template_path, context)

def post_model_list_view(request):

    qs = PostModel.objects.all()
    context = {
        "object_list": qs,
    }


    template_path =  "list-view.html"

    return render(request, template_path, context)



@login_required(login_url='/login')
def login_required_view(request):
    print(request.user)
    qs = PostModel.objects.all()
    context = {
        "object_list": qs,
    }
    if request.user.is_authenticated():
        template = "blog/list-view.html"

    else:

     template_path =  "list-view-public.html"
   #raise Http404
     return HttpResponseRedirect("/login")

    return render(request, template_path, context)



