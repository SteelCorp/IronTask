from . import models

from rest_framework import viewsets, permissions

from . import models

from rest_framework import serializers




class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sponsor
        fields = (
            'pk',
            'siret',
            'raisonSocial',
            'adresse',
            'codePostal',
            'ville',
            'telephone',

        )

class SponsorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Sponsor class"""

    queryset = models.Sponsor.objects.all()
    serializer_class = SponsorSerializer
