import staticjinja


def get_user():
    return 'Леонид Федорович'


def get_bind():
    return {'publication_datetime': 'Вчера, в 21:30',
            'user_name': 'Алексей',
            'count_views': 12,
            'bind_text': '60 шт. ПК от 72-15 до ПК 21-15, '
                         'Криводановка, с доставкой.',
            }


def get_regions():
    return {'selected_region': 'Новосибирск и область',
            'list_region': [{'url': '#', 'name': 'Новосибирск и область'},
                            {'url': '#', 'name': 'Москва и область'},
                            {'url': '#', 'name': 'Нижний новгород и область'},
                            {'url': '#', 'name': 'Киров и область'},
                            ],
            }


def get_company():
    return {'name': 'ООО Сторой-Сервис-Монтаж',
            'region': 'Новосибирск',
            'products': 'ЖБИ, бетон',
            'address': 'Под часами, на том же месте',
            'phone': '00-00-00',
            'logo': 'img/company_default.png',
            'url': 'company_profile.html'
            }


def get_product():
    return {'name': 'ЖБИ',
            'url': 'companies_filter.html',
            'img': 'img/jbi.jpeg',
            }


def index_page():
    title = 'Поставщики новосибирска'
    list_of_binds = [get_bind(), get_bind(), get_bind(), get_bind()]
    comment = {'user_avatar': 'img/avatar_default.png',
               'user_name': 'Кирилл',
               'user_age': 29,
               'user_city': 'Барабинск',
               'comment_text': """Бла, бла, бла! Мне помогло, все супер!
                                Бла, бла, бла! Мне помогло, все супер!
                                Бла, бла, бла! Мне помогло, все супер!""",
               }
    list_of_comments = [comment, comment, comment]
    return {'title': title,
            'user': get_user(),
            'regions': get_regions(),
            'list_of_binds': list_of_binds,
            'list_of_comments': list_of_comments,
            'need_to_show_notify_message': 1,
            }


def binds_page():
    title = 'Заявки'
    list_of_binds = [get_bind(), get_bind(), get_bind(), get_bind(),
                     get_bind(), get_bind(), get_bind(), get_bind(),
                     get_bind(), get_bind()]
    list_links = [{'url': 'index.html', 'title': 'Главная'},
                  {'url': 'binds.html', 'title': 'Заявки'},
                  ]
    return {'title': title,
            'user': get_user(),
            'regions': get_regions(),
            'list_of_binds': list_of_binds,
            'list_links': list_links,
            'need_to_show_notify_message': 0,
            }


def companies_page():
    title = 'Каталог организаций'
    title_main = 'Все производители и оптовые компании'
    list_links = [{'url': 'index.html', 'title': 'Главная'},
                  {'url': 'companies_all.html',
                   'title': 'Каталог организаций'},
                  ]
    list_of_companies = [get_company(), get_company(), get_company(),
                         get_company(), get_company(), get_company()]
    list_of_products = [get_product(), get_product(), get_product(),
                        get_product()]
    return {'title': title,
            'user': get_user(),
            'regions': get_regions(),
            'title_main': title_main,
            'list_links': list_links,
            'list_of_companies': list_of_companies,
            'list_of_products': list_of_products,
            'need_to_show_notify_message': 0,
            }


def companies_filter_page(filter_products='ЖБИ'):
    params = companies_page()
    params['title'] = 'Каталог огранизаций | ' + filter_products
    params['title_main'] = 'Производители и оптовые компании в Новосибирске' \
                           ' и области'
    params['filter_products'] = filter_products
    params['list_links'].append({'url': 'companies_filter.html',
                                 'title': filter_products})
    params['need_to_show_notify_message'] = 0
    return params


def company_profile_page():
    params = get_company()
    params['title'] = 'Информация о компании'
    params['about'] = """
    Физики, специализирующиеся в новой дисциплине, атомтронике, занимаются
    созданием аналогов электронных схем из систем атомов, используя лазеры
    и магнитные поля. В Joint Quantum Institute (JQI) на примере сверхтекучей
    атомтронной цепи удалось продемонстрировать гистерезис — эффект, имеющий
    ключевое значение для электроники. Так, например, он применяется при
    записи информации на жесткие диски и в другие запоминающие устройства,
    в определенных типах сенсоров и сглаживающих фильтров, таких как триггер
    Шмитта.
    Эксперимент, описанный в февральском выпуске Nature стал первым опытом
    наблюдения гистерезиса в ультрахолодном атомном газе. Облако, состоящее
    из 400 тыс. атомов натрия, охладили до температуры около 0,1 микрокельвина,
    при которой образовался конденсат Бозе-Эйнштейна (КБЭ). Атомы удерживались
    в тороидальной ловушке, габаритами чуть больше человеческого эритроцита,
    а сфокусированный лазерный луч использовался, чтобы заставить полученную
    квантовую жидкость двигаться по кольцу.
    """
    params['list_links'] = \
        [{'url': 'index.html', 'title': 'Главная'},
         {'url': 'companies_all.html', 'title': 'Каталог организаций'},
         {'url': 'companies_filter.html', 'title': 'ЖБИ'},
         {'url': 'company_profile.html', 'title': params['name']},
         ]
    params['regions'] = get_regions()
    params['user'] = get_user()
    params['need_to_show_notify_message'] = 0
    return params


def pesonal_page():
    title = 'Личный кабинет'
    list_links = [{'url': 'index.html', 'title': 'Главная'},
                  {'url': 'personal.html', 'title': 'Личный кабинет'},
                  ]
    return {'title': title,
            'user': get_user(),
            'regions': get_regions(),
            'list_links': list_links,
            'need_to_show_notify_message': 0,
            }


if __name__ == "__main__":
    site = staticjinja.make_site(contexts=[('index.html', index_page()),
                                           ('binds.html', binds_page()),
                                           ('companies_all.html',
                                            companies_page()),
                                           ('companies_filter.html',
                                            companies_filter_page('ЖБИ')),
                                           ('company_profile.html',
                                           company_profile_page()),
                                           ('personal.html', pesonal_page()),
                                           ]
                                 )
    site.render(use_reloader=True)
