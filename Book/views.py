from django.shortcuts import render,HttpResponse,redirect
from .models import Book
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='/user/login/')
def Welcome(request):
    Books = Book.objects.all()
    return render(request,"home.html", {"all_books": Books})


def Create_book(request):
    if request.method == "GET":
        return render(request, "create_book.html")
    elif request.method == "POST":
        data = request.POST 
        if not data.get("id"):
            Book.objects.create(title = data.get("title"), author = data.get("author"), 
                            publication_date = data.get("publication date"), price = data.get("price"))
        else:
        
                book_obj = Book.objects.get(id = (data.get("id")))
                book_obj.title = data.get("title")
                book_obj.author = data.get("author")
                book_obj.publication_date = data.get("publication date")
                book_obj.price = data.get("price")
                book_obj.save()
        return redirect("home")    


def Edit_book(request, id):
    try:    
        book_obj = Book.objects.get(id = id)
    except Book.DoesNotExist as msg:
        return HttpResponse("Book does not exit")
    else:
        return render(request,"create_book.html",  {"Book": book_obj})


def Delete_book(request, id):
    try:
        book_obj = Book.objects.get(id = id)
    except Book.DoesNotExist as msg:
        return HttpResponse("Book does not exit")
    
    else:
        if request.POST.get("type_of_delete") == "HardDelete":
            book_obj.delete()
        else:   
            book_obj.isdeleted = True                    #soft delete 
            book_obj.save()     
        return redirect("home")



def show_Deleted_books(request):
    deleted_books = Book.objects.filter(isdeleted=True)
    return render(request, "deleted_book.html", {"deleted_book":deleted_books})


def Restore_book(request,id):
    try:
        book_obj = Book.objects.get(id = id) 
    except Book.DoesNotExist:
        return HttpResponse("Book does not exit")
    else:
        book_obj.isdeleted = False
        book_obj.save()
    return redirect("home") 
    

