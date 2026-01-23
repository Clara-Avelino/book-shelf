import requests 
from django.conf import settings 
from django.http import JsonResponse 

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Simulado um usuario em modo DEBUG
        # if settings.DEBUG:
        #     request.external_user_id = 1
        #     request.external_username = "dev"
        #     return self.get_response(request)

        # Ignora a validação para arquivos estáticos
        if request.path.startswith('/static/') or request.path.startswith('/media/'):
            return self.get_response(request)
        
        # Inicializa como None
        request.external_user_id = None
        request.external_username = None
        
        # Pega os dados da sessão
        auth_token = request.session.get('auth_token')
        email_logado = request.session.get('user_email')

        if auth_token:
            try:
                # Adiciona Bearer se não tiver
                token_header = f"Bearer {auth_token}"

                response = requests.get(
                    "https://usuarioapi-production.up.railway.app/api/usuarios/",
                    headers={"Authorization": token_header},
                    timeout=5
                )

                if response.status_code == 200:
                    user_list = response.json()
                    user = None
                    
                    if isinstance(user_list, list):
                        user = next((u for u in user_list if u.get('email') == email_logado), None)
                    else:
                        user = user_list

                    if user:
                        # Atribuí os valores reais
                        request.external_user_id = user.get("id")
                        request.external_username = user.get("username")
                    
            except Exception as e:
                print(f"Erro no Middleware: {e}")

        print(f"DEBUG API: Path={request.path} | UserID={request.external_user_id} | Username={request.external_username}")

        return self.get_response(request)
