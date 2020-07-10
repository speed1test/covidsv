from django.urls import path
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from . import views

urlpatterns = [
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	    #Reestablecimiento de password
	path('reset/password_reset', PasswordResetView.as_view(template_name='users/password_reset_form.html', email_template_name="users/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html') , name = 'password_reset_complete'),
	
]