from django.urls import path
from .views import *

urlpatterns = [
    path('authorization',authorization_admin),
    path('admin/add_survey', add_survey_admin),
    path('admin/update_survey', change_survey_admin),
    path('admin/delete_survey', delete_survey_admin),
    path('admin/add_questions', add_questions_admin),
    path('admin/change_questions',change_questions_admin),
    path('admin/delete_questions', delete_questions_admin),
    path('admin/create_answers', create_answers_admin),
    path('get_survey', get_survey),
    path('start_survey', start_survey),
    path('ready_data', ready_data),
    path('all_data', all_data),

]