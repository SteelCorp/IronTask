from django.test import TestCase
from irontask_app.models import Sponsor

from django.urls import reverse
from irontask_app.views.viewSponsor import *
from django.contrib.auth.models import User
from django.test import Client


class test_SponsorCase(TestCase):

    def setUp(self):
        Sponsor.objects.create(siret='12345678912345',
                               raisonSocial='Leclerc.E',
                               adresse='5 rue du commerce',
                               codePostal='31000',
                               ville='Toulouse',
                               telephone='0305060788',
                               email='leclerc@gmail.com'
                               )
        self.user = User.objects.create_user(username='john', email='john@beatles.fr', password='johnpassword')
        self.c = Client()
        self.client.login(username='john', password='johnpassword')
        self.sponsor = Sponsor.objects.get(siret='12345678912345')

    def test__str__(self):
        b = Sponsor.objects.get(siret='12345678912345')
        self.assertEqual(b.__str__(), 'Leclerc.E')


    def testListSponsorView(self):
        self.client.login(username='john', password='johnpassword')
        reponse = self.c.get(reverse(viewname=listSponsor), follow=True)
        self.assertEqual(reponse.status_code, 200)

    def testEditerSponsorView(self):
        self.client.login(username='john', password='johnpassword')
        reponse = self.c.get(reverse(viewname=editerSponsor, args=[self.sponsor.siret]), follow=True)
        self.assertEqual(reponse.status_code, 200)
