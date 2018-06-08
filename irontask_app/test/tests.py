import unittest
from django.urls import reverse
from django.test import Client
from irontask_app.models import UserProfile, Intervenant, Sponsor, Categorie, Materiel, Benevole, TypeTriathlon, Triathlon, Tache, Intervenir, Sponsoriser, Caracteriser, Allouer, Affecter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_userprofile(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_user()
    return UserProfile.objects.create(**defaults)


def create_intervenant(**kwargs):
    defaults = {}
    defaults["siret"] = "siret"
    defaults["raisonSocial"] = "raisonSocial"
    defaults["type"] = "type"
    defaults["adresse"] = "adresse"
    defaults["codePostal"] = "codePostal"
    defaults["ville"] = "ville"
    defaults["telephoneFixe"] = "telephoneFixe"
    defaults["telephonePort"] = "telephonePort"
    defaults["email"] = "email"
    defaults.update(**kwargs)
    return Intervenant.objects.create(**defaults)


def create_sponsor(**kwargs):
    defaults = {}
    defaults["siret"] = "siret"
    defaults["raisonSocial"] = "raisonSocial"
    defaults["adresse"] = "adresse"
    defaults["codePostal"] = "codePostal"
    defaults["ville"] = "ville"
    defaults["telephoneFixe"] = "telephoneFixe"
    defaults["email"] = "email"
    defaults.update(**kwargs)
    return Sponsor.objects.create(**defaults)


def create_categorie(**kwargs):
    defaults = {}
    defaults["libelle"] = "libelle"
    defaults["ageMin"] = "ageMin"
    defaults["ageMax"] = "ageMax"
    defaults["sexe"] = "sexe"
    defaults.update(**kwargs)
    return Categorie.objects.create(**defaults)


def create_materiel(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults["type"] = "type"
    defaults["qteTotal"] = "qteTotal"
    defaults["lieuStockage"] = "lieuStockage"
    defaults.update(**kwargs)
    return Materiel.objects.create(**defaults)


def create_benevole(**kwargs):
    defaults = {}
    defaults["nom"] = "nom"
    defaults["prenom"] = "prenom"
    defaults["dateNaissance"] = "dateNaissance"
    defaults["sexe"] = "sexe"
    defaults["adresse"] = "adresse"
    defaults["codePostal"] = "codePostal"
    defaults["ville"] = "ville"
    defaults["telephoneFixe"] = "telephoneFixe"
    defaults["telephonePortable"] = "telephonePortable"
    defaults["email"] = "email"
    defaults.update(**kwargs)
    return Benevole.objects.create(**defaults)


def create_typetriathlon(**kwargs):
    defaults = {}
    defaults["libelle"] = "libelle"
    defaults["distanceNatation"] = "distanceNatation"
    defaults["distanceCyclisme"] = "distanceCyclisme"
    defaults["distanceCourseAPied"] = "distanceCourseAPied"
    defaults.update(**kwargs)
    return TypeTriathlon.objects.create(**defaults)


def create_triathlon(**kwargs):
    defaults = {}
    defaults["date"] = "date"
    defaults["description"] = "description"
    defaults["heureDepart"] = "heureDepart"
    defaults["codePostal"] = "codePostal"
    defaults["adresse"] = "adresse"
    defaults["ville"] = "ville"
    defaults.update(**kwargs)
    if "fk_TypeTriathlon" not in defaults:
        defaults["fk_TypeTriathlon"] = create_typetriathlon()
    return Triathlon.objects.create(**defaults)


def create_tache(**kwargs):
    defaults = {}
    defaults["nomTache"] = "nomTache"
    defaults["description"] = "description"
    defaults["dateDebut"] = "dateDebut"
    defaults["dateFin"] = "dateFin"
    defaults["dateRappel"] = "dateRappel"
    defaults["niveauAvancement"] = "niveauAvancement"
    defaults["niveauPriorite"] = "niveauPriorite"
    defaults.update(**kwargs)
    if "fk_triathlon" not in defaults:
        defaults["fk_triathlon"] = create_triathlon()
    return Tache.objects.create(**defaults)


def create_intervenir(**kwargs):
    defaults = {}
    defaults["devis"] = "devis"
    defaults["prixDevis"] = "prixDevis"
    defaults.update(**kwargs)
    if "fk_triathlon" not in defaults:
        defaults["fk_triathlon"] = create_triathlon()
    if "fk_intervenant" not in defaults:
        defaults["fk_intervenant"] = create_intervenant()
    return Intervenir.objects.create(**defaults)


def create_sponsoriser(**kwargs):
    defaults = {}
    defaults["donation"] = "donation"
    defaults.update(**kwargs)
    if "fk_triathlon" not in defaults:
        defaults["fk_triathlon"] = create_triathlon()
    if "fk_sponsor" not in defaults:
        defaults["fk_sponsor"] = create_sponsor()
    return Sponsoriser.objects.create(**defaults)


def create_caracteriser(**kwargs):
    defaults = {}
    defaults["nbrParticipant"] = "nbrParticipant"
    defaults.update(**kwargs)
    if "fk_triathlon" not in defaults:
        defaults["fk_triathlon"] = create_triathlon()
    if "fk_categorie" not in defaults:
        defaults["fk_categorie"] = create_categorie()
    return Caracteriser.objects.create(**defaults)


def create_allouer(**kwargs):
    defaults = {}
    defaults["qteUtilise"] = "qteUtilise"
    defaults.update(**kwargs)
    if "fk_triathlon" not in defaults:
        defaults["fk_triathlon"] = create_triathlon()
    if "fk_materiel" not in defaults:
        defaults["fk_materiel"] = create_materiel()
    if "fk_benevole" not in defaults:
        defaults["fk_benevole"] = create_benevole()
    return Allouer.objects.create(**defaults)


def create_affecter(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "fk_benevole" not in defaults:
        defaults["fk_benevole"] = create_benevole()
    if "fk_tache" not in defaults:
        defaults["fk_tache"] = create_tache()
    return Affecter.objects.create(**defaults)


class UserProfileViewTest(unittest.TestCase):
    '''
    Tests for UserProfile
    '''
    def setUp(self):
        self.client = Client()

    def test_list_userprofile(self):
        url = reverse('app_name_userprofile_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_userprofile(self):
        url = reverse('app_name_userprofile_create')
        data = {
            "user": create_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_userprofile(self):
        userprofile = create_userprofile()
        url = reverse('app_name_userprofile_detail', args=[userprofile.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_userprofile(self):
        userprofile = create_userprofile()
        data = {
            "user": create_user().pk,
        }
        url = reverse('app_name_userprofile_update', args=[userprofile.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class IntervenantViewTest(unittest.TestCase):
    '''
    Tests for Intervenant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_intervenant(self):
        url = reverse('app_name_intervenant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_intervenant(self):
        url = reverse('app_name_intervenant_create')
        data = {
            "siret": "siret",
            "raisonSocial": "raisonSocial",
            "type": "type",
            "adresse": "adresse",
            "codePostal": "codePostal",
            "ville": "ville",
            "telephoneFixe": "telephoneFixe",
            "telephonePort": "telephonePort",
            "email": "email",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_intervenant(self):
        intervenant = create_intervenant()
        url = reverse('app_name_intervenant_detail', args=[intervenant.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_intervenant(self):
        intervenant = create_intervenant()
        data = {
            "siret": "siret",
            "raisonSocial": "raisonSocial",
            "type": "type",
            "adresse": "adresse",
            "codePostal": "codePostal",
            "ville": "ville",
            "telephoneFixe": "telephoneFixe",
            "telephonePort": "telephonePort",
            "email": "email",
        }
        url = reverse('app_name_intervenant_update', args=[intervenant.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SponsorViewTest(unittest.TestCase):
    '''
    Tests for Sponsor
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sponsor(self):
        url = reverse('app_name_sponsor_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sponsor(self):
        url = reverse('app_name_sponsor_create')
        data = {
            "siret": "siret",
            "raisonSocial": "raisonSocial",
            "adresse": "adresse",
            "codePostal": "codePostal",
            "ville": "ville",
            "telephoneFixe": "telephoneFixe",
            "email": "email",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sponsor(self):
        sponsor = create_sponsor()
        url = reverse('app_name_sponsor_detail', args=[sponsor.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sponsor(self):
        sponsor = create_sponsor()
        data = {
            "siret": "siret",
            "raisonSocial": "raisonSocial",
            "adresse": "adresse",
            "codePostal": "codePostal",
            "ville": "ville",
            "telephoneFixe": "telephoneFixe",
            "email": "email",
        }
        url = reverse('app_name_sponsor_update', args=[sponsor.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CategorieViewTest(unittest.TestCase):
    '''
    Tests for Categorie
    '''
    def setUp(self):
        self.client = Client()

    def test_list_categorie(self):
        url = reverse('app_name_categorie_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_categorie(self):
        url = reverse('app_name_categorie_create')
        data = {
            "libelle": "libelle",
            "ageMin": "ageMin",
            "ageMax": "ageMax",
            "sexe": "sexe",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_categorie(self):
        categorie = create_categorie()
        url = reverse('app_name_categorie_detail', args=[categorie.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_categorie(self):
        categorie = create_categorie()
        data = {
            "libelle": "libelle",
            "ageMin": "ageMin",
            "ageMax": "ageMax",
            "sexe": "sexe",
        }
        url = reverse('app_name_categorie_update', args=[categorie.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MaterielViewTest(unittest.TestCase):
    '''
    Tests for Materiel
    '''
    def setUp(self):
        self.client = Client()

    def test_list_materiel(self):
        url = reverse('app_name_materiel_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_materiel(self):
        url = reverse('app_name_materiel_create')
        data = {
            "nom": "nom",
            "type": "type",
            "qteTotal": "qteTotal",
            "lieuStockage": "lieuStockage",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_materiel(self):
        materiel = create_materiel()
        url = reverse('app_name_materiel_detail', args=[materiel.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_materiel(self):
        materiel = create_materiel()
        data = {
            "nom": "nom",
            "type": "type",
            "qteTotal": "qteTotal",
            "lieuStockage": "lieuStockage",
        }
        url = reverse('app_name_materiel_update', args=[materiel.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BenevoleViewTest(unittest.TestCase):
    '''
    Tests for Benevole
    '''
    def setUp(self):
        self.client = Client()

    def test_list_benevole(self):
        url = reverse('app_name_benevole_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_benevole(self):
        url = reverse('app_name_benevole_create')
        data = {
            "nom": "nom",
            "prenom": "prenom",
            "dateNaissance": "dateNaissance",
            "sexe": "sexe",
            "adresse": "adresse",
            "codePostal": "codePostal",
            "ville": "ville",
            "telephoneFixe": "telephoneFixe",
            "telephonePortable": "telephonePortable",
            "email": "email",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_benevole(self):
        benevole = create_benevole()
        url = reverse('app_name_benevole_detail', args=[benevole.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_benevole(self):
        benevole = create_benevole()
        data = {
            "nom": "nom",
            "prenom": "prenom",
            "dateNaissance": "dateNaissance",
            "sexe": "sexe",
            "adresse": "adresse",
            "codePostal": "codePostal",
            "ville": "ville",
            "telephoneFixe": "telephoneFixe",
            "telephonePortable": "telephonePortable",
            "email": "email",
        }
        url = reverse('app_name_benevole_update', args=[benevole.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TypeTriathlonViewTest(unittest.TestCase):
    '''
    Tests for TypeTriathlon
    '''
    def setUp(self):
        self.client = Client()

    def test_list_typetriathlon(self):
        url = reverse('app_name_typetriathlon_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_typetriathlon(self):
        url = reverse('app_name_typetriathlon_create')
        data = {
            "libelle": "libelle",
            "distanceNatation": "distanceNatation",
            "distanceCyclisme": "distanceCyclisme",
            "distanceCourseAPied": "distanceCourseAPied",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_typetriathlon(self):
        typetriathlon = create_typetriathlon()
        url = reverse('app_name_typetriathlon_detail', args=[typetriathlon.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_typetriathlon(self):
        typetriathlon = create_typetriathlon()
        data = {
            "libelle": "libelle",
            "distanceNatation": "distanceNatation",
            "distanceCyclisme": "distanceCyclisme",
            "distanceCourseAPied": "distanceCourseAPied",
        }
        url = reverse('app_name_typetriathlon_update', args=[typetriathlon.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TriathlonViewTest(unittest.TestCase):
    '''
    Tests for Triathlon
    '''
    def setUp(self):
        self.client = Client()

    def test_list_triathlon(self):
        url = reverse('app_name_triathlon_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_triathlon(self):
        url = reverse('app_name_triathlon_create')
        data = {
            "date": "date",
            "description": "description",
            "heureDepart": "heureDepart",
            "codePostal": "codePostal",
            "adresse": "adresse",
            "ville": "ville",
            "fk_TypeTriathlon": create_typetriathlon().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_triathlon(self):
        triathlon = create_triathlon()
        url = reverse('app_name_triathlon_detail', args=[triathlon.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_triathlon(self):
        triathlon = create_triathlon()
        data = {
            "date": "date",
            "description": "description",
            "heureDepart": "heureDepart",
            "codePostal": "codePostal",
            "adresse": "adresse",
            "ville": "ville",
            "fk_TypeTriathlon": create_typetriathlon().pk,
        }
        url = reverse('app_name_triathlon_update', args=[triathlon.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TacheViewTest(unittest.TestCase):
    '''
    Tests for Tache
    '''
    def setUp(self):
        self.client = Client()

    def test_list_tache(self):
        url = reverse('app_name_tache_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_tache(self):
        url = reverse('app_name_tache_create')
        data = {
            "nomTache": "nomTache",
            "description": "description",
            "dateDebut": "dateDebut",
            "dateFin": "dateFin",
            "dateRappel": "dateRappel",
            "niveauAvancement": "niveauAvancement",
            "niveauPriorite": "niveauPriorite",
            "fk_triathlon": create_triathlon().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_tache(self):
        tache = create_tache()
        url = reverse('app_name_tache_detail', args=[tache.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_tache(self):
        tache = create_tache()
        data = {
            "nomTache": "nomTache",
            "description": "description",
            "dateDebut": "dateDebut",
            "dateFin": "dateFin",
            "dateRappel": "dateRappel",
            "niveauAvancement": "niveauAvancement",
            "niveauPriorite": "niveauPriorite",
            "fk_triathlon": create_triathlon().pk,
        }
        url = reverse('app_name_tache_update', args=[tache.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class IntervenirViewTest(unittest.TestCase):
    '''
    Tests for Intervenir
    '''
    def setUp(self):
        self.client = Client()

    def test_list_intervenir(self):
        url = reverse('app_name_intervenir_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_intervenir(self):
        url = reverse('app_name_intervenir_create')
        data = {
            "devis": "devis",
            "prixDevis": "prixDevis",
            "fk_triathlon": create_triathlon().pk,
            "fk_intervenant": create_intervenant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_intervenir(self):
        intervenir = create_intervenir()
        url = reverse('app_name_intervenir_detail', args=[intervenir.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_intervenir(self):
        intervenir = create_intervenir()
        data = {
            "devis": "devis",
            "prixDevis": "prixDevis",
            "fk_triathlon": create_triathlon().pk,
            "fk_intervenant": create_intervenant().pk,
        }
        url = reverse('app_name_intervenir_update', args=[intervenir.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SponsoriserViewTest(unittest.TestCase):
    '''
    Tests for Sponsoriser
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sponsoriser(self):
        url = reverse('app_name_sponsoriser_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sponsoriser(self):
        url = reverse('app_name_sponsoriser_create')
        data = {
            "donation": "donation",
            "fk_triathlon": create_triathlon().pk,
            "fk_sponsor": create_sponsor().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sponsoriser(self):
        sponsoriser = create_sponsoriser()
        url = reverse('app_name_sponsoriser_detail', args=[sponsoriser.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sponsoriser(self):
        sponsoriser = create_sponsoriser()
        data = {
            "donation": "donation",
            "fk_triathlon": create_triathlon().pk,
            "fk_sponsor": create_sponsor().pk,
        }
        url = reverse('app_name_sponsoriser_update', args=[sponsoriser.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CaracteriserViewTest(unittest.TestCase):
    '''
    Tests for Caracteriser
    '''
    def setUp(self):
        self.client = Client()

    def test_list_caracteriser(self):
        url = reverse('app_name_caracteriser_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_caracteriser(self):
        url = reverse('app_name_caracteriser_create')
        data = {
            "nbrParticipant": "nbrParticipant",
            "fk_triathlon": create_triathlon().pk,
            "fk_categorie": create_categorie().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_caracteriser(self):
        caracteriser = create_caracteriser()
        url = reverse('app_name_caracteriser_detail', args=[caracteriser.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_caracteriser(self):
        caracteriser = create_caracteriser()
        data = {
            "nbrParticipant": "nbrParticipant",
            "fk_triathlon": create_triathlon().pk,
            "fk_categorie": create_categorie().pk,
        }
        url = reverse('app_name_caracteriser_update', args=[caracteriser.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AllouerViewTest(unittest.TestCase):
    '''
    Tests for Allouer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_allouer(self):
        url = reverse('app_name_allouer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_allouer(self):
        url = reverse('app_name_allouer_create')
        data = {
            "qteUtilise": "qteUtilise",
            "fk_triathlon": create_triathlon().pk,
            "fk_materiel": create_materiel().pk,
            "fk_benevole": create_benevole().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_allouer(self):
        allouer = create_allouer()
        url = reverse('app_name_allouer_detail', args=[allouer.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_allouer(self):
        allouer = create_allouer()
        data = {
            "qteUtilise": "qteUtilise",
            "fk_triathlon": create_triathlon().pk,
            "fk_materiel": create_materiel().pk,
            "fk_benevole": create_benevole().pk,
        }
        url = reverse('app_name_allouer_update', args=[allouer.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AffecterViewTest(unittest.TestCase):
    '''
    Tests for Affecter
    '''
    def setUp(self):
        self.client = Client()

    def test_list_affecter(self):
        url = reverse('app_name_affecter_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_affecter(self):
        url = reverse('app_name_affecter_create')
        data = {
            "fk_benevole": create_benevole().pk,
            "fk_tache": create_tache().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_affecter(self):
        affecter = create_affecter()
        url = reverse('app_name_affecter_detail', args=[affecter.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_affecter(self):
        affecter = create_affecter()
        data = {
            "fk_benevole": create_benevole().pk,
            "fk_tache": create_tache().pk,
        }
        url = reverse('app_name_affecter_update', args=[affecter.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


