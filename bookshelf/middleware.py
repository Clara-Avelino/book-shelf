import requests 
from django.conf import settings # Acessa a chave secreta
from django.http import JsonResponse # Retorna erro se o token for inválido

class JWTAuthMiddleware:
    def __init__(self, get_response):
        # Guarda a próxima etapa da requisição
        self.get_response = get_response
    
    def __call__(self, request):
        # Modo para acessar com um usuario simulado em modo DEBUG
        if settings.DEBUG:
            request.external_user_id = 1
            request.external_username = "dev"
            return self.get_response(request)
        
        # Inicializa valores padrão
        request.external_user_id = None
        request.external_username = None

        # Lê o cabeçalho Authorization da requisição
        auth_header = request.headers.get('Authorization') # Lendo o token

        if auth_header:
            try:
                response = requests.get(
                f"{settings.AUTH_API_URL}/api/usuarios/",
                headers={"Authorization": auth_header},
                timeout=5
            )

                if response.status_code != 200:
                    return JsonResponse({'error': 'Token inválido'}, status=401)

            # Aqui você pode extrair dados do primeiro usuário autenticado
                user = response.json()[0]  
                request.external_user_id = user["id"]
                request.external_username = user["username"]

            except Exception:
                return JsonResponse({'error': 'Erro ao validar token'}, status=401)

        return self.get_response(request)





