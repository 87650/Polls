# Polls
Чтобы запустить этот проект достаточно иметь python и базу данных MSQL.
С помощью  /authorization происходит авторизация администратора,
 admin/add_survey - добавление опроса, admin/update_survey - обновление опроса, admin/delete_survey - удаление опроса
 admin/add_questions - добавление вопроса в опрос, admin/change_questions - обновление вопроса. admin/delete_questions - удаление вопроса,
admin/create_answers - создание ответов, нужно для того чтобы можно было выбрать несколько или один ответ, 
get_survey - показ опросов (только тех что попадают в определённый промежуток дат),
start_survey - получение вопросов по опросу, ready_data - загрузка ответов пользователя, all_data - вывод своих ответов и ответов других пользователей.
