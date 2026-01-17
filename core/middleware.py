import jwt # Decodifica o token
from django.conf import settings # Acessa a chave secreta
from django.http import JsonResponse # Retorna erro se o token for inválido

class JWTAuthMiddleware:
    def __init__(self, get_response):
        # Guarda a próxima etapa da requisição
        self.get_response = get_response
    
    def __call__(self, request):
        # Modo para acessar com um usuario simulado em modo DEBUG
        if settings.DEBUG:
            request.external_user_id = settings.DEV_FAKE_USER_ID
            request.external_username = settings.DEV_FAKE_USERNAME
            return self.get_response(request)
        
        # Inicializa valores padrão
        request.external_user_id = None
        request.external_username = None

        # Lê o cabeçalho Authorization da requisição
        auth_header = request.headers.get('Authorization') # Lendo o token

        if auth_header:
            try:
                # Divide "Bearer TOKEN" em duas partes
                prefix, token = auth_header.split(' ')

                # Verifica se o formato é Bearer
                if prefix != 'Bearer':
                    raise Exception('Token mal formatado')
                # Decodifica o token JWT usando a chave secreta
                payload = jwt.decode(
                    token,
                    settings.JWT_SECRET_KEY,
                    algorithms=['HS256'])
                # Extrai dados do payload
                request.external_user_id = payload.get('user_id')
                request.external_username = payload.get('username')
                
            except Exception:
                # Se o token for inválido ou expirado
                return JsonResponse(
                    {'error': 'Token inválido ou expirado'}, status=401)
        else:
            # Caso não tenha token
                request.external_user_id = None

        # Continua o fluxo normal da requisição
        return self.get_response(request)





