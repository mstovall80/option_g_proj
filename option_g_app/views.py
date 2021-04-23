from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print(pw_hash)

    this_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
    request.session['user_id'] = this_user.id

    return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if User:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/main')
    messages.error(request, "Invalid login")
    return redirect( "/")

def main(request):
    user_id = request.session['user_id']
    context={
        "this_user": User.objects.get(id=user_id) 
        # "all_quotes": User.objects.all()
    }
    return render(request, "main.html", context)

def quotes_list(request):
    user_id = request.session['user_id']
    context = {
    "this_user": User.objects.get(id=user_id).__dict__
    }
    return render(request, "/main", context)

def add_quote(request):
    loggedin_user = User.objects.get(id=request.session["user_id"])
    Quote.objects.create(quote=request.POST["quote"], author=request.POST["author"],posted_by=loggedin_user)
    return redirect("/user_quotes")

def user_quotes(request):
    loggedin_user = User.objects.get(id=request.session["user_id"])
    context={
        "user": loggedin_user
    }
    return render(request, "user_quotes.html", context)

def edit_account(request):
    return render(request, "edit_account.html")

def logout(request):
    if "user_id" not in request.session:
        return redirect('/')
    del request.session['user_id']
    return redirect("/")

def delete_user(request):
    del request.session['user_id']
    return render(request, "main.html")