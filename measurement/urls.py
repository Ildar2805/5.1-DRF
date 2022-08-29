from django.urls import path

from measurement.views import SensorsView, InfoView, MeasurementsView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', InfoView.as_view()),
    path('measurements/', MeasurementsView.as_view())
]
