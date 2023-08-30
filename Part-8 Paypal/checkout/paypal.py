

import sys
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AdJcUzRL6_5S6RLmPcSh3TiqHz1dJBvv3mb_rx-mfER1Sz36LTDOlr14oVCg-AaMMIpER9D6q5m1fx91"
        self.client_secret = "EN05eUjRE0qIqNwrjuyBA0lph9fIiH1K3K5JGn3cnsfKDqhQsPu-2X4Obdb6QXbXa2A0bebDYnUlo-pX"
        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
