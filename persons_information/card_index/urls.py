from django.urls import path

from card_index import views
from card_index.views import persons

urlpatterns = [
    path('', persons),
    path('detail/<int:pk>', views.PersonView.as_view(), name='person-detail'),
]
