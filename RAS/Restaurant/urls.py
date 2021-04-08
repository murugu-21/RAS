from django.conf.urls import url 
from Restaurant import views 
 
urlpatterns = [ 
    url('loginCheck', views.loginCheck),
    url('getUsers', views.get_users),
    url('createUser', views.create_user),
    url('ForgotPassword', views.ForgotPassword),
    url('OtpValidation', views.OtpValidation),
    url('ChangePassword', views.ChangePassword),
    url('deleteUsers', views.deleteUsers),
    url('CreatePdf', views.Create_Pdf),
    url('retreive_pdf', views.retreive_pdf),
    url('GetSalesGraph', views.get_chart),
    url('CreateExcel', views.CreateExcel),
    url('CreateCsv', views.CreateCsv),
    url('UpdatePrice', views.update_price),
    url('GetFoodsForClerk', views.GetFoodsForClerk),
    url('GetFoods', views.get_foods),
    url('AddIngredients', views.add_ingredients),
    url('GetIngredients', views.getingredient_list),
    url('AddFoodItems', views.add_food),
    url('BillGenerator', views.bill_generator),
    url('GenerateInvoice',views.get_Invoice),
    url('GetComplement', views.get_complement),
    url('GetPurchaseList', views.get_purchase_list),
    url('image',views.get_Image),
    url('DeleteFood',views.delete_food)
]