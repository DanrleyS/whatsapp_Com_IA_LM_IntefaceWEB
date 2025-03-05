from django.urls import path
from .views import (
    home, processar_conversa, classificar_mensagem, 
    chatbot, chatbot_conversacional, treinar_modelo
)

urlpatterns = [
    path('', home, name='home'),
    path('processar_conversa/', processar_conversa, name='processar_conversa'),
    path('classificar_mensagem/', classificar_mensagem, name='classificar_mensagem'),
    path('chatbot/', chatbot, name='chatbot'),
    path('chatbot_conversacional/', chatbot_conversacional, name='chatbot_conversacional'),
    path('treinar_modelo/', treinar_modelo, name='treinar_modelo'),
]

