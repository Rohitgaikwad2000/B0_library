"""
URL configuration for Bookslab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Book.views import Welcome, Create_book, Edit_book, Delete_book, show_Deleted_books, Restore_book


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Welcome, name = "home"),
    path('add-book/', Create_book, name = "add_book"),
    path('edit-book/<int:id>', Edit_book, name = "edit_book"),
    path('delete-book/<int:id>', Delete_book, name = "delete_book"),
    path('deleted-books/', show_Deleted_books, name = "deleted_book"),
    path('restore-book/<int:id>', Restore_book, name = "restore_book"),



    path('user/', include('user_app.urls')),    # include all the url forms user_app


] 