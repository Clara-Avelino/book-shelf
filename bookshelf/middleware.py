import requests 
from django.conf import settings # Acessa a chave secreta
from django.http import JsonResponse # Retorna erro se o token for inválido

class JWTAuthMiddleware:
    def __init__(self, get_response):
        # Guarda a próxima etapa da requisição
        self.get_response = get_response
    
    def __call__(self, request):
        
        # Modo para acessar com um usuario simulado em modo DEBUG
        # if settings.DEBUG:
        #     request.external_user_id = 1
        #     request.external_username = "dev"
        #     return self.get_response(request)
        
        # Inicializa valores padrão
        request.external_user_id = None
        request.external_username = None

        # Lê o cabeçalho Authorization da requisição
        auth_token = request.session.get('auth_token') # Pega o token da sessão do Django
        email_na_sessao = request.session.get('user_email')

        if auth_token:
            try:
                # Adiciona Bearer se não tiver
                token_header = f"Bearer {auth_token}"

                response = requests.get(
                    "https://usuarioapi-production.up.railway.app/api/usuarios/",
                    headers={"Authorization": token_header},
                    timeout=5
                )

                # Deve ser IGUAL a 200 para capturar o usuário
                if response.status_code == 200:
                    user_list = response.json()

                    email_logado = request.session.get('user_email') 

                    # Se a API retorna uma lista, pegamos o primeiro usuário
                    if isinstance(user_list, list):
                        user = next((u for u in user_list if u.get('email') == email_logado), None)
                        
                        if not user and len(user_list) > 0:
                            user = user_list[0]
                    else:
                        user = user_list

                    if user:
                        request.external_user_id = user.get("id")
                        request.external_username = user.get("username")
                        print(f"Logado como: {request.external_username} (ID: {request.external_user_id})")
                    
            except Exception as e:
                print(f"Erro no Middleware: {e}")

        return self.get_response(request)





