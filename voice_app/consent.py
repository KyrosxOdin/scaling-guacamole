import json
import os
from datetime import datetime

CONSENT_LOG = "consent_log.json"

class ConsentManager:
    """Manage user consent and legal compliance."""
    def __init__(self):
        self.log = []
        if os.path.exists(CONSENT_LOG):
            with open(CONSENT_LOG, 'r') as f:
                self.log = json.load(f)

    def request_consent(self, subject_name:str):
        print(f"Please review and sign the consent for {subject_name}.")
        input_sig = input("Type your full name as digital signature: ")
        entry = {
            'subject': subject_name,
            'signed_by': input_sig,
            'timestamp': datetime.utcnow().isoformat()
        }
        self.log.append(entry)
        with open(CONSENT_LOG, 'w') as f:
            json.dump(self.log, f, indent=2)
        print("Consent recorded.")
        return True
