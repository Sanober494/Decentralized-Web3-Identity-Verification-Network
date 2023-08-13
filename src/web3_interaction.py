class UserInterface:
    def __init__(self):
        self.ivps = [IdentityVerificationProvider("IVP1"), IdentityVerificationProvider("IVP2")]
        self.ledger = DecentralizedLedger()
        self.contract = SmartContract()
        self.consensus = ConsensusMechanism()

    def initiate_verification(self, user_id, credentials):
        verified_ivps = [ivp for ivp in self.ivps if ivp.validate_credentials(credentials)]
        if not verified_ivps:
            return "Identity verification failed."

        identity_token = verified_ivps[0].generate_identity_token(credentials)
        self.ledger.store_identity_token(user_id, identity_token)
        return "Identity verified and token stored."

    def submit_credentials_to_ivp(self, ivp_name, credentials):
        ivp = next((ivp for ivp in self.ivps if ivp.name == ivp_name), None)
        if not ivp:
            return "Invalid IVP name."

        if ivp.validate_credentials(credentials):
            identity_token = ivp.generate_identity_token(credentials)
            return f"Credentials submitted to {ivp_name} and identity token generated: {identity_token}"
        else:
            return f"Credentials submission to {ivp_name} failed."

    def interact_with_web3(self, user_id, action):
        identity_token = self.ledger.get_identity_token(user_id)
        if not identity_token:
            return "Identity token not found."

        if not self.contract.verify_identity_token(identity_token):
            return "Identity token verification failed."

        if not self.consensus.verify_consensus(identity_token):
            return "Consensus verification failed."

        return f"Secure and privacy-preserving {action} performed."
