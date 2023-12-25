from django.urls import path
from .views import elektron,reg,kirish,chiq,tavarlar,save_add,save_x,add,post_delet,tavar_i,div_addd
urlpatterns = [
    path('',elektron,name='elktr'),
    path('royhat/',reg,name='register'),
    path('kirish/',kirish,name='kirish'),
    path('chiq/',chiq,name='chiqsh'),
    path('tavarlar/',tavarlar,name='tavarlar'),
    path('saved_add/<int:id>',save_add,name='save_add'),
    path('save_x/<int:id>',save_x,name='save_x'),
    path('add/',add,name='add'),
    path('post_d/<int:id>',post_delet,name='p_d'),
    path('tavar_i/',tavar_i,name='tv_i'),
    path('tavar_i/div_addd/',div_addd,name='div_addd')
]