from django import forms
from .models import Mentor, Group, Student, Post

class MentorCreateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ["full_name", "birth_date", "specification", "level", "phone", "email", "address", "salary"]


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["specification", "block", "time", "language", "name", "mentor", "student_qty", "status"] 


# class StudentCreateForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ["full_name", "birth_date", "specification", "level", "phone", "email", "address", "salary"]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "date"] 