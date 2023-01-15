# from flask_app import app
# from flask import render_template
# import pandas as pd
# from flask_app import app
# from flask_app.forms import SurveyForm
# #from flask_app.models import Anketa
# #import pretty_html_table
import pandas as pd
from flask_app import app,db
from flask import render_template, redirect
from flask_app.forms import SurveyForm
from flask_app.models import Anketa, User
import pretty_html_table
import matplotlib.pyplot as plt
@app.route("/")
def main():
    return render_template('main.html')
#@app.route("/anketa")
#def opros():
#    return render_template('tmp_opros_result.html', title='Опрос', text_info='Здесь будет опрос.')
# @app.route("/result")
# def result():
#     return render_template('tmp_opros_result.html', title='Результаты', text_info='Здесь будут результаты опроса.')
# @app.route("/anketa")
# def opros():
#     return render_template('opros.html')


@app.route('/anketa', methods=['POST', 'GET'])
def opros():
    form = SurveyForm()
    if form.validate_on_submit():
        # print('Has DATA')
        new_anketa = Anketa(
            quest1 = form.quest1.data,
            quest2=form.quest2.data,
            quest3=form.quest3.data,
            quest4=form.quest4.data,
            quest5=form.quest5.data,
            quest6=form.quest6.data,
            comment=form.comment.data
        )
        new_user = User(
            username=form.username.data,
            age=form.age.data,
            gender=form.gender.data,
            activity=', '.join(form.activity.data),
            city=form.city.data
        )
        db.session.add(new_anketa)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('opros2.html', form=form)

@app.route('/result')
def result():
    all_ankets = Anketa.query.all()
    all_users = User.query.all()
    all_ankets = [(v.quest1,v.quest2,v.quest3,v.quest4,v.quest5,v.quest6, v.comment)
                  for v in all_ankets]
    all_users = [(v.username, v.age, v.gender, v.activity, v.city)
                  for v in all_users]
    all_ankets_tb = pd.DataFrame(all_ankets,
                              columns=['Вопрос 1',
                                       'Вопрос 2','Вопрос 3','Вопрос 4','Вопрос 5','Вопрос 6','Комментарий']
                              )

    all_users_tb = pd.DataFrame(all_users,
                              columns=['Имя', 'Возраст', 'Гендер', 'Род деятельности', 'Город проживания']
                              )
    all_ankets = pretty_html_table.build_table(all_ankets_tb, 'blue_light')
    all_users = pretty_html_table.build_table(all_users_tb, 'blue_light')
    #return render_template('result2.html', html_table=all_ankets)
#например, сколько человек прошло опрос, какой максимальный, минимальный и средний возраст информантов
#какую-нибудь статистику по вопросам анкеты (например, медиана рейтинга каждого стимульного предложения)
    with open('flask_app/templates/result2.html', 'r', encoding='utf-8') as f:
        html_code = f.read()
    html_code = html_code.replace('{{ html_table }}', all_ankets)
    html_code = html_code.replace('{{ html_table1 }}', all_users)
    html_code = html_code.replace('{{ total_count }}', str(all_ankets_tb.shape[0]))
    html_code = html_code.replace('{{ quest1ans1 }}', str(int(all_ankets_tb[all_ankets_tb['Вопрос 1']=='снизилась незначительно'].count()[1])/all_ankets_tb.shape[0]))
    html_code = html_code.replace('{{ quest1ans2 }}', str(int(
        all_ankets_tb[all_ankets_tb['Вопрос 1'] == 'заметно снизилась'].count()[1]) / all_ankets_tb.shape[0]))
    html_code = html_code.replace('{{ quest1ans3 }}', str(int(
        all_ankets_tb[all_ankets_tb['Вопрос 1'] == 'явно упала'].count()[1]) / all_ankets_tb.shape[0]))
    html_code = html_code.replace('{{ quest1ans4 }}', str(int(
        all_ankets_tb[all_ankets_tb['Вопрос 1'] == 'резко понизилась'].count()[1]) / all_ankets_tb.shape[0]))
    return html_code