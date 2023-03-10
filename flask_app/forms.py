from flask_wtf import FlaskForm
from wtforms import (
    widgets, StringField, SubmitField, EmailField,
    IntegerField, SelectField, SelectMultipleField, TextAreaField
)
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

#имя/возраст/город проживания/гендер/род деятельности и т.п.
class SurveyForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    gender = SelectField('Гендер',
                            choices=[('Женщина', 'Женщина'), ('Мужчина', 'Мужчина'),
                                     ('Другой', 'Другой'),
                                     ]
                            )
    activity = MultiCheckboxField('Какой деятельностью Вы занимаетесь?',
                            choices=[('Учусь', 'Учусь'), ('Работаю', 'Работаю'), ('Другое', 'Другое')]
                            )
    city = SelectField('Город проживания',
                            choices=[('Москва', 'Москва'), ('Санкт-Петербург', 'Санкт-Петербург'),
                                     ('Новосибирск', 'Новосибирск'),
                                     ('Екатеринбург', 'Екатеринбург'),
                                     ('Казань', 'Казань'),
                                     ('Нижний Новгород', 'Нижний Новгород'),
                                     ('Челябинск', 'Челябинск'),
                                     ('Омск', 'Омск'),
                                     ('Ростов-на-Дону', 'Ростов-на-Дону'),
                                     ('Другой город', 'Другой город'),
                                     ]
                            )

    quest1 = SelectField('Ваша работоспособность по сравнению с обычной:',
                                  choices=[('снизилась незначительно', 'снизилась незначительно'), ('заметно снизилась', 'заметно снизилась'),
                                           ('явно упала', 'явно упала'), ('резко понизилась', 'резко понизилась')]
                                  )
    quest2 = SelectField('Вы стали уставать:',
                                  choices=[('при усиленной нагрузке', 'при усиленной нагрузке'), ('при обычной нагрузке', 'при обычной нагрузке'),
                                           ('при облегченной нагрузке', 'при облегченной нагрузке'), ('без всякой нагрузки', 'без всякой нагрузки')]
                                  )
    quest3 = SelectField('Можете ли вы волевым усилием вернуть себе прежнюю работоспособность:',
                                choices=[('могу без всякого усилия', 'могу без всякого усилия'),
                                         ('усилием воли восстанавливаю полностью', 'усилием воли восстанавливаю полностью'),
                                         ('восстанавливаю частично', 'восстанавливаю частично'),
                                         ('лишь незначительно', 'лишь незначительно')]
                                )
    quest4 = SelectField('Замечаете ли вы в себе эмоциональные сдвиги?',
                                  choices=[('временами снижение интереса к работе', 'временами снижение интереса к работе'),
                                           ('бывает неустойчивым настроение', 'бывает неустойчивым настроение'),
                                           ('стал раздражителен', 'стал раздражителен'),
                                           ('чувствую себя угнетенно, резкая раздражительность', 'чувствую себя угнетенно, резкая раздражительность')]
                                  )
    quest5 = SelectField('Изменился ли у вас сон?',
                         choices=[('трудно засыпать или просыпаться', 'трудно засыпать или просыпаться'),
                                  ('гораздо труднее стало засыпать и просыпаться', 'гораздо труднее стало засыпать и просыпаться'),
                                  ('у меня сонливость днем', 'у меня сонливость днем'),
                                  ('страдаю бессонницей',
                                   'страдаю бессонницей')]
                         )
    quest6 = SelectField('Умственные действия вам даются:',
                         choices=[('не труднее, чем обычно', 'не труднее, чем обычно'),
                                  ('с трудом сосредотачиваюсь',
                                   'с трудом сосредотачиваюсь'),
                                  ('временами становлюсь забывчив', 'временами становлюсь забывчив'),
                                  ('заметно ослабли внимание и память',
                                   'заметно ослабли внимание и память')]
                         )
    comment = TextAreaField('Комментарий')
    submit = SubmitField('Сохранить')