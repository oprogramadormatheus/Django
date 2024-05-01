from faker import Faker

def make_recipe():

    fake = Faker('pt_BR')
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porções',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': f'{fake.first_name()} {fake.last_name()}',
        'category': fake.word(),
        'cover': 'https://fakeimg.pl/1280x720/269fe6/ffffff?font=bebas'
    }
