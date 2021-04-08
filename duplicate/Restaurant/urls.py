from django.conf.urls import url 
from Restaurant import views 
 
urlpatterns = [ 
    url(r'^api/loginCheck$', views.login_check),
    url(r'^api/getUsers$', views.get_users),
    url(r'^api/createUser$', views.create_user),
    url(r'^api/deleteUser$', views.delete_user),
    url(r'^api/ForgotPassword$', views.forgot_password),
    url(r'^api/OtpValidation$', views.otp_validation),
    url(r'^api/ChangePassword$', views.change_password),
    url(r'^api/CreatePdf$', views.create_pdf),
    url(r'^api/GetSalesGraph$', views.get_chart),
    url(r'^api/GetFoods$', views.get_foods),
    url(r'^api/UpdatePrice$', views.update_price),
    url(r'^api/GetIngredients$', views.getingredient_list),
    url(r'^api/AddFoodItems$', views.add_food),
    url(r'^api/AddIngredients$',views.add_ingredients),
]