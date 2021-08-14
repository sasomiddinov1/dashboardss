from django.shortcuts import redirect, render
from .models import Mentor, Group, Post
from .forms import MentorCreateForm, GroupCreateForm, PostCreateForm

# Create your views here.

def dashboard(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "mainapp/index.html", context)



def createPost(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("dashboard")
    else:
        form = PostCreateForm()

    context = {
        "form" : form
    }
    return render(request, "mainapp/create_post.html", context)










# def add_mentor(request):
#     if request.method == 'POST':
#         form = MentorRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = MentorRegistrationForm()

#     context = {
#         'form': form
#     }

#     return render(request, "dashboardapp/add_mentor.html", context)

def createMentor(request):
    form = MentorCreateForm()
    if request.method == "POST":
        form = MentorCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("mentors_table")
    else:
        form = MentorCreateForm()

    context = {
        "form" : form
    }
    return render(request, "mainapp/create_mentor.html", context)
    
def updateMentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    form  = MentorCreateForm(instance=mentor)
    if request.method == "POST":
        form = MentorCreateForm(request.POST, instance=mentor)
        if form.is_valid:
            form.save()
            return redirect('mentors_table')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_mentor.html", context)

def deleteMentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    if request.method == "POST":
        mentor.delete()
        return redirect('mentors_table') 
    context = {
        'mentor': mentor
    }
    return render(request, 'mainapp/delete_mentor.html', context)

def mentorsTable(request):
    mentors = Mentor.objects.all()
    context = {
        "mentors": mentors
    }
    return render(request, "mainapp/mentors_table.html", context)




def createGroup(request):
    form = GroupCreateForm()
    if request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("groups_table")
    else:
        form = GroupCreateForm()

    context = {
        "form" : form
    }
    return render(request, "mainapp/create_group.html", context)

def updateGroup(request, pk):
    group = Group.objects.get(id=pk)
    form  = GroupCreateForm(instance=group)
    if request.method == "POST":
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid:
            form.save()
            return redirect('groups_table')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_group.html", context)



def deleteGroup(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == "POST":
        group.delete()
        return redirect('groups_table') 
    context = {
        'group': group
    }
    return render(request, 'mainapp/delete_group.html', context)




def groupsTable(request):
    groups = Group.objects.all()
    context = {
        "groups": groups
    }
    return render(request, "mainapp/groups_table.html", context)