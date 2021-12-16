from rest_framework.views import APIView
from rest_framework.response import Response


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

        
        out = [] 

        for opt in options:
            out.append({
                **opt, 

                'escanio': 0,
            })

        
        numEscanos = totalEscanio

        while numEscanos>0:
            
            actual = 0
            
            for i in range(1, len(out)):
                valorActual = out[actual]['votes'] / (out[actual]['escanio'] + 1)
                valorComparar = out[i]['votes'] / (out[i]['escanio'] + 1)

                
                if(valorActual<valorComparar):
                    actual = i
            
        
            out[actual]['escanio'] = out[actual]['escanio'] + 1
            numEscanos = numEscanos - 1
        
        
        out.sort(key = lambda x: -x['escanio'])
        print(out)
        
        
        
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

        t = request.data.get('type', 'IDENTITY')
        opts = request.data.get('options', [])
        s = request.data.get('escanio')
        print(opts)
        

        if t == 'IDENTITY':
            return self.identity(opts)
        elif t == 'DHONDT':
            print("Entra en metodo")
            return self.dhondt(opts, request.data.get('escanio'))
        return Response({})
