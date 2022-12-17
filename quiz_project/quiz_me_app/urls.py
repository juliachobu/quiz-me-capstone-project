from django.urls import path
from .views import GetQuestions, QuestionDetail, ResultDetail, get_results




# urlpatterns = [
#     path('questions/', getQuestion , name='questions'),
#     # path('questions/', GetQuestions.as_view() , name='questions'),
#     # path('details/', QuestionDetail.as_view() , name='details'),
#     # path('results/', ResultDetail.as_view() , name='results'),
#     path('results/', get_results, name='get_results')
# ]

urlpatterns = [
    path('questions/', GetQuestions.as_view() , name='questions'),
    path('details/', QuestionDetail.as_view() , name='details'),
    path('results/', ResultDetail.as_view() , name='results'),
    path('get_results/', get_results, name='get_results')
]
