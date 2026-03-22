from django.urls import path
from . import views

urlpatterns = [
    # Question URLs
    path('', views.HomePage, name='home'),
    path('start-test/', views.Starttest, name='starttest'),
    path('add-question/', views.Addquestion, name='addquestion'),
    path('show-questions/', views.Showallquestions, name='showallquestions'),
    
    # Student URLs

    path('edit-question/<int:pk>/', views.Editquestion, name='editquestion'),
    path('update-question/<int:pk>/', views.Updatequestion, name='updatequestion'),
    path('add-student/', views.Addstudent, name='addstudent'),
    path('show-students/', views.Showstudents, name='showstudents'),
    path('edit-student/<int:pk>/', views.Editstudent, name='editstudent'),
    path('update-student/<int:pk>/', views.Updatestudent, name='updatestudent'),
    path('delete-student/<int:pk>/', views.Deletestudent, name='deletestudent'),
    path('login/', views.StudentLogin, name='login'),
    path('logout/', views.StudentLogout, name='logout'),
    # Add this line to your urlpatterns list
    path('calculate-result/', views.CalculateResult, name='calculate_result'),

]