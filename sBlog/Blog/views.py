from django.shortcuts import render , HttpResponseRedirect , redirect
from . forms import SignupForm,LoginForm, PostForm,ContactForm
from django.contrib  import messages
from django.contrib.auth import authenticate, login, logout
from . models import Post
from django.contrib.auth.models import Group


# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'Blog/Home.html', {'posts':posts})


def About(request):
    return render(request, 'Blog/about.html') 



def Contact(request):

    if request.method =="POST":
        form  =  ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , " We will contact you soon !")
        else:
            messages.error(request, "Please fill correct information")

    return render(request, 'Blog/contact.html')
    


def Dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'Blog/dashboard.html',{'posts':posts, 'fullname':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')  

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm (request.POST)
        if fm.is_valid():
            messages.success(request, 'YOUR FORM SUMITTED SUCCESSFULLY')
            user = fm.save()
            group = Group.objects.get(name= 'Author')
            user.groups.add(group)
    
    else:
        fm = SignupForm()
    return render(request, 'Blog/signup.html', {'form':fm})




def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            
                fm = LoginForm (request=request, data=request.POST)
                if fm.is_valid():
                    uname=fm.cleaned_data['username']
                    upass = fm.cleaned_data['password']

                    user = authenticate(username =uname,password=upass)
                    if user is not None :
                        login(request, user)
                        messages.success(request,'Login Successfully' )
                        return HttpResponseRedirect('/dashboard/')
            
        else:
            fm = LoginForm()
        return render(request, 'Blog/login.html',{'form':fm})

    else:
        return HttpResponseRedirect('/dashboard/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
                tittle = fm.cleaned_data['tittle']
                desc = fm.cleaned_data['desc']
                pst= Post(tittle=tittle , desc=desc)
                pst.save()
                fm = PostForm()
        else:
            fm = PostForm()
        return render(request, 'blog/addpost.html',{'form':fm} )

    else:
        return HttpResponseRedirect('/login/')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST, instance=pi)
            fm.save()
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)
        return render(request, 'blog/update.html',{'form':fm})

    else:
        return HttpResponseRedirect('/login/')


def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Post.objects.get(pk=id)
            pi.delete()

        return HttpResponseRedirect('/dashboard/')

    else:
        return HttpResponseRedirect('/login/')














