from rest_framework.views import APIView
from rest_framework.response import Response
import math

class PostProcView(APIView):

    def identity(self, options):
        out = []

        for opt in options:
            out.append({
                **opt,
                'postproc': opt['votes'],
            })

        out.sort(key=lambda x: -x['postproc'])
        return Response(out)

    def dhondt(self, options, totalEscanio):

        #Salida que vamos a devolver
        out = [] 

        #Añadimos en options el parametro escanio donde se guardara
        #la cantidad de escanios por opcion (la s en la formula de la ley)
        for opt in options:
            out.append({
                **opt, 

                'escanio': 0,
            })

        #Igualamos el nnumEscanios al numero total de escanios
        numEscanos = totalEscanio

        #Entra en el bucle hasta que no se repartan todos los escanios
        while numEscanos>0:
            
            actual = 0
            
            #Se comprueban las opciones posibles
            for i in range(1, len(out)):
                valorActual = out[actual]['votes'] / (out[actual]['escanio'] + 1)
                valorComparar = out[i]['votes'] / (out[i]['escanio'] + 1)

                
                if(valorActual<valorComparar):
                    actual = i
            
            #Al final de recorrer todos, la opcion cuyo indice es actual es el que posee más votos y,
            #por tanto, se le añade un escaño
            out[actual]['escanio'] = out[actual]['escanio'] + 1
            numEscanos = numEscanos - 1
        
        #Ordenamos las opciones
        out.sort(key = lambda x: -x['escanio'])

        return Response(out)
        
    
    def simple(self, options, escanio):
        out = []
        for simp in options:
            out.append({
                **simp,
                'escanio': 0,
            })
        out.sort(key=lambda x: -x['votes'])

        sea = escanio
        n = 0

        for votes in out:
                n = votes['votes'] + n
        
        valEs = n/sea

        n1 = 0
        while sea > 0:
            if n1 < len(out):
                escanio_ = math.trunc(out[n1]['votes']/valEs) 
                out[n1]['escanio'] = escanio_
                sea = sea - escanio_
                n1 = n1+1
            else:
                now = 0
                c = 1
                while c <len(out):
                    vAct = out[now]['votes']/valEs - out[now]['escanio']
                    vCom = out[c]['votes']/valEs - out[c]['escanio']
                    if(vAct >= vCom):
                        c = c + 1
                    else:
                        now=c
                        c = c + 1
                out[now]['escanio'] = out[now]['escanio'] + 1
                sea = sea - 1

        return Response(out)

    def post(self, request):
        """
         * type: IDENTITY | EQUALITY | WEIGHT
         * options: [
            {
             option: str,
             number: int,
             votes: int,
             ...extraparams
            }
           ]
        """

        t = request.data.get('type')
        opts = request.data.get('options', [])
        

        if t == 'IDENTITY':
            return self.identity(opts)
        elif t == 'DHONDT':
            return self.dhondt(opts, request.data.get('escanio'))
        elif t == 'SIMPLE':
            return self.simple(opts, request.data.get('escanio'))
        return Response({})
