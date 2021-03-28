from masoniteorm.seeds import Seeder

from app.User import User
from config.factories import factory


from app.Deal import Deal


class DealsTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        Deal.create({
               'title': 'test deal',
        'description': 'a test deal',
        'organisation': 'test company',
        'contact': 'bob jones',
        'owner': 'dan',
        'stage': 'discover',
        'won': 0,
        'value': '1234',
            'user_id':1
        })


