from django.urls import path
from .views import BookmarkListView, BookmarkCreateView

urlpatterns =[
    # http://127.0.0.1/bookmark/???
    # ???
    path('', BookmarkListView.as_view(), name='list'), # class 형 뷰일 때 .as_view()
    path("add/", BookmarkCreateView.as_view(), name='add'),
]