import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from base import mods
from census.models import Census


# TODO: check permissions and census
class BoothView(TemplateView):
    template_name = 'booth/booth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)
        try:
            r = mods.get('voting', params={'id': vid})
            # Casting numbers to string to manage in javascript with BigInt
            # and avoid problems with js and big number conversion
            for k, v in r[0]['pub_key'].items():
                r[0]['pub_key'][k] = str(v)

            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        context['KEYBITS'] = settings.KEYBITS
        print(context)
        return context


class BoothListView(TemplateView):
    #Colocamos el nombre de nuestra template
    template_name = 'booth/booth_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['KEYBITS'] = settings.KEYBITS
        return context


class VotingList(APIView):
    def post(self, request):
        # Obtenemos el id del usuario que ha iniciado sesión
        idUser = request.user.id
        # Obtenemos del móduclo Census los ids de las votaciones en las que se le permite votar al usuario
        votacionesCensus = Census.objects.filter(voter_id = idUser)
        idsVotaciones = []
        for v in votacionesCensus:
            idsVotaciones.append(v.voting_id)
        
        votaciones = []
        for idVoting in idsVotaciones:
            # Obtenemos cada votación gracias al id
            votacion = mods.get('voting', params={'id': idVoting})
            votaciones.append(votacion)
        
        # Mandamos las votaciones a nuestra página
        return Response(votaciones)
