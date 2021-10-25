from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import *
import json
import random

@csrf_exempt
def authorization_admin(request):
    admin = Admin.objects.all()
    login = request.POST['login']
    password = request.POST['password']
    for value in admin:
        if (value.login == login  and value.password == password):
            request.session['login_admin'] = login
            return JsonResponse({"result": "{0} вошли".format(request.session['login_admin'])})
            break
        elif (admin[len(admin) - 1].id == value.id):
            return JsonResponse({"result": "вы не вошли, неправильно введен логин или пароль"})


@csrf_exempt
def add_survey_admin(request):
    if(request.session['login_admin'] == None):
        name = request.POST['name']
        start = request.POST['start']
        end = request.POST['end']
        description = request.POST['description']
        Survey.objects.create(name=name,start=start,end=end,description=description)
        return JsonResponse({"result": "успех "})
    else:
        return redirect("http://127.0.0.1:8000/authorization")


@csrf_exempt
def change_survey_admin(request):
    if (request.session['login_admin'] == None):
        name_filter = request.POST['name_filter']
        name = request.POST['name']
        start = request.POST['start']
        end = request.POST['end']
        description = request.POST['description']
        Survey.objects.filter(name=name_filter).update(name=name, start=start, end=end, description=description)
        return JsonResponse({"result": "успех "})
    else:
        return redirect("http://127.0.0.1:8000/authorization")


@csrf_exempt
def delete_survey_admin(request):
    if(request.session['login_admin'] == None):
        name_filter = request.POST['name_filter']
        Survey.objects.filter(name=name_filter).delete()
        return JsonResponse({"result": "успех "})
    else:
        return redirect("http://127.0.0.1:8000/authorization")

@csrf_exempt
def add_questions_admin(request):
    if (request.session['login_admin'] == None):
        name_survey = request.POST['name_survey']
        survey = Survey.objects.filter(name=name_survey)
        question = request.POST['question']
        type = request.POST['type']
        survey.questions_set.create(question=question,type=type)
        return JsonResponse({"result": "успех "})
    else:
        return redirect("http://127.0.0.1:8000/authorization")

@csrf_exempt
def change_questions_admin(request):
    if (request.session['login_admin'] == None):
        name_survey = request.POST['name_survey']
        id_filter = request.POST['id_filter']
        question = request.POST['question']
        type = request.POST['type']
        survey = Survey.objects.filter(name=name_survey)
        survey.questions_set.filter(id=id).update(question=question,type=type)
        return JsonResponse({"result": "успех "})
    else:
        return redirect("http://127.0.0.1:8000/authorization")

@csrf_exempt
def delete_questions_admin(request):
    if(request.session['login_admin'] == None):
        name_filter = request.POST['name_filter']
        id = request.POST['id']
        survey = Survey.objects.filter(name=name_filter).delete
        return JsonResponse({"result": "успех "})
    else:
        return redirect("http://127.0.0.1:8000/authorization")

@csrf_exempt
def create_answers_admin(request):
    if (request.session['login_admin'] == None):
        name_survey = request.POST['name_survey']
        id_filter = request.POST['id_filter']
        value = request.POST["value"]
        survey = Survey.objects.filter(name=name_survey)
        questions =  survey.questions_set.filter(id=id_filter)
        if (value == 1):
            answer1 = request.POST['answer1']
            questions.answers_set.get(answer1=answer1)
            return JsonResponse({"result": "успех "})
        if (value == 2):
            answer1 = request.POST['answer1']
            answer2 = request.POST['answer2']
            questions.answers_set.get(answer1=answer1,answer2=answer2)
            return JsonResponse({"result": "успех "})

    else:
        return redirect("http://127.0.0.1:8000/authorization")

@csrf_exempt
def get_survey(request):
    arr = []
    data = request.POST['data']
    survey = Survey.objects.all()
    for value in survey:
        if(survey.start < data and survey.end > data):
            arr.append(value)
    result_arr = serialize('json', arr)
    return JsonResponse({"all": result_arr})


@csrf_exempt
def start_survey(request):
    survey = request.POST['survey']
    obj = Survey.objects.filter(id=survey)
    question = obj.questions_set.all()
    answers = Answers.object.filter(id_survey=survey)
    result_arr = serialize('json', question)
    result_arr1 = serialize('json', answers)
    return JsonResponse({"question": result_arr,"answers": result_arr1})

@csrf_exempt
def ready_data(request):
    body = request.body.decode('utf-8')
    result = json.loads(body)
    ran = random.randint(1,1000)
    id = Id.objects.create(id_user=ran)
    for value in result:
        id.answers_users_set.create(answer=value['answer'],name_survey=value['name_survey'],id_question=value['id_question'])
    return JsonResponse({"result": "успех "})

@csrf_exempt
def all_data(request):
    id = request.POST['id']
    user = Id.objects.filter(id=id)
    answer = user.answers_users_set.all()
    result_arr = serialize('json', answer)
    survey = Survey.objects.filter(name=answer[0].name_survey)
    questions = survey.questions_set.all()
    result_arr1 = serialize('json', questions)
    return JsonResponse({"answer": result_arr, "questions": result_arr1})




















