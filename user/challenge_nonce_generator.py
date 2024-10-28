import random

class ChallengeNonceGenerator:
    @staticmethod
    def generate_nonce():
        return random.randint(1, 1e9)
