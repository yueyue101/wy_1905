from django.shortcuts import render

# Create your views here.
def index(request):

    print("创建主页，修改bug")
    return "主页"