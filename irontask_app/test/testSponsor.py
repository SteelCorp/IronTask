from django.test import TestCase
from irontask_app.models import Sponsor
from django.test import Client


class test_SponsorCase(TestCase):


    def setUp(self):
        Sponsor.objects.create(siret = '12345678912345',
                               raisonSocial='Leclerc.E',
                               adresse='5 rue du commerce',
                               codePostal='31000',
                               ville='Toulouse',
                               telephone='0305060788',
                               email='leclerc@gmail.com'
    )

    def test__str__(self):
        b = Sponsor.objects.get(siret = '12345678912345')
        self.assertEqual(b.__str__(), 'Leclerc.E')


