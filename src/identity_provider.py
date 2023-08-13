class IdentityVerificationProvider:
    def __init__(self, name):
        self.name = name

    def validate_credentials(self, credentials):
        return True

    def generate_identity_token(self, credentials):
        return hashlib.sha256(json.dumps(credentials).encode()).hexdigest()
