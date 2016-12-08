import staticjinja


basic_info = {
    'user': 'Леонид Федорович',
    'regions': {'selected_region': 'Новосибирск и область',
                'list_region': [
                    {'url': '#', 'name': 'Новосибирск и область'},
                    {'url': '#', 'name': 'Москва и область'},
                    {'url': '#', 'name': 'Нижний новгород и область'},
                    {'url': '#', 'name': 'Киров и область'},
                ],
                },
}
bind = {
    'publication_datetime': 'Вчера, в 21:30',
    'user_name': 'Алексей',
    'count_views': 12,
    'bind_text': '60 шт. ПК от 72-15 до ПК 21-15, '
                 'Криводановка, с доставкой.',
}
comment = {'user_avatar': 'img/avatar_default.png',
           'user_name': 'Кирилл',
           'user_age': 29,
           'user_city': 'Барабинск',
           'comment_text': """Бла, бла, бла! Мне помогло, все супер!
                            Бла, бла, бла! Мне помогло, все супер!
                            Бла, бла, бла! Мне помогло, все супер!""",
           }
company = {'name': 'ООО Сторой-Сервис-Монтаж',
           'region': 'Новосибирск',
           'products': 'ЖБИ, бетон',
           'address': 'Под часами, на том же месте',
           'phone': '00-00-00',
           'logo': 'img/company_default.png',
           'url': 'company_profile.html'
           }
product = {'name': 'ЖБИ',
           'url': 'companies_filter.html',
           'img': 'img/jbi.jpeg',
           }
index_page_data = {
    'title': 'Поставщики Новосибирска',
    'list_of_binds': [bind for number in range(4)],
    'list_of_comments': [comment for number in range(3)],
    'need_to_show_notify_message': 1,
}
index_page_data.update(basic_info)
binds_page_data = {
    'title': 'Заявки',
    'list_of_binds': [bind for number in range(10)],
    'list_links': [{'url': 'index.html', 'title': 'Главная'},
                   {'url': 'binds.html', 'title': 'Заявки'},
                   ],

}
binds_page_data.update(basic_info)
companies_page_data = {
    'title': 'Каталог организаций',
    'title_main': 'Все производители и оптовые компании',
    'list_links': [{'url': 'index.html', 'title': 'Главная'},
                   {'url': 'companies_all.html',
                    'title': 'Каталог организаций'},
                   ],
    'list_of_companies': [company for number in range(6)],
    'list_of_products': [product for number in range(4)],
}
companies_page_data.update(basic_info)
companies_filter_page_data = {
    'title': 'Каталог огранизаций | ЖБИ',
    'title_main': 'Производители и оптовые компании в Новосибирске и области',
    'filter_products': 'ЖБИ',
    'list_links': [{'url': 'index.html', 'title': 'Главная'},
                   {'url': 'companies_all.html',
                    'title': 'Каталог организаций'},
                   {'url': 'companies_filter.html', 'title': 'ЖБИ'},
                   ],
    'list_of_companies': [company for number in range(6)],
    'list_of_products': [product for number in range(4)],
}
companies_filter_page_data.update(basic_info)
company_profile_page_data = {
    'title': 'Информация о компании',
    'about': """
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
    """,
    'list_links': [{'url': 'index.html', 'title': 'Главная'},
                   {'url': 'companies_all.html',
                    'title': 'Каталог организаций'},
                   {'url': 'companies_filter.html', 'title': 'ЖБИ'},
                   {'url': 'company_profile.html', 'title': company['name']},
                   ],
}
company_profile_page_data.update(basic_info)
company_profile_page_data.update(company)
pesonal_page_data = {
    'title': 'Личный кабинет',
    'list_links': [{'url': 'index.html', 'title': 'Главная'},
                   {'url': 'personal.html', 'title': 'Личный кабинет'},
                   ],
}
pesonal_page_data.update(basic_info)


if __name__ == "__main__":
    site = staticjinja.make_site(outpath='docs',
                                 contexts=[('index.html', index_page_data),
                                           ('binds.html', binds_page_data),
                                           ('companies_all.html',
                                            companies_page_data),
                                           ('companies_filter.html',
                                            companies_filter_page_data),
                                           ('company_profile.html',
                                           company_profile_page_data),
                                           ('personal.html',
                                            pesonal_page_data),
                                           ]
                                 )
    site.render(use_reloader=True)
