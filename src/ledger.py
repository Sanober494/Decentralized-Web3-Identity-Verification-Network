class DecentralizedLedger:
    def __init__(self):
        self.identity_tokens = {}

    def store_identity_token(self, user_id, identity_token):
        self.identity_tokens[user_id] = identity_token

    def get_identity_token(self, user_id):
        return self.identity_tokens.get(user_id)
