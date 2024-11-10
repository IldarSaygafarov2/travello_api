from django.urls import path

from . import views

urlpatterns = [
    path('guides/<int:user_id>/', views.GuideDetailView.as_view()),
    path('guides/<int:user_id>/update/', views.GuideUpdateView.as_view()),
    path('guides/<int:user_id>/tours/create/', views.GuideTourCreateView.as_view()),
    path('guides/<int:user_id>/tours/', views.GuideToursListView.as_view())
]

# TODO: Сделать обновление данных гида
# Начать делать конструктор тура для пользователя
# Переписать авторизацию и регистрацию пользователя
# Показывать роль пользователя после авторизации

