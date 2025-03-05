class ConversationManager:
    def __init__(self):
        self.conversations = {}
        self.pending_location_request = {}  # Armazena se o usuário deve fornecer localização

    def add_message(self, user_id, mensagem, role="user"):
        """Adiciona a mensagem ao histórico do usuário"""
        if user_id not in self.conversations:
            self.conversations[user_id] = []

        self.conversations[user_id].append({"role": role, "content": mensagem})

    def get_context(self, user_id):
        """Retorna o histórico da conversa do usuário"""
        return self.conversations.get(user_id, [])

    def set_pending_location_request(self, user_id, status=True):
        """Marca se o chatbot está esperando a localização do usuário"""
        self.pending_location_request[user_id] = status

    def is_waiting_for_location(self, user_id):
        """Verifica se o usuário deve fornecer uma localização"""
        return self.pending_location_request.get(user_id, False)

    def clear_pending_location_request(self, user_id):
        """Reseta o estado de espera por localização"""
        if user_id in self.pending_location_request:
            del self.pending_location_request[user_id]
