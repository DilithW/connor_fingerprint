import hashlib
import random

class FingerprintAuthenticationSystem:
    def __init__(self):
        self.enrolled_fingerprints = {}

    def enroll_fingerprint(self, user_id):
        # Simulate the process of capturing a fingerprint and generating a hash
        fingerprint_data = self.capture_fingerprint()
        fingerprint_hash = self.generate_fingerprint_hash(fingerprint_data)
        self.enrolled_fingerprints[user_id] = fingerprint_hash
        return f"Fingerprint enrolled for user {user_id}."

    def authenticate_fingerprint(self, user_id):
        if user_id not in self.enrolled_fingerprints:
            return "User not found."

        # Simulate the process of capturing a fingerprint for authentication
        fingerprint_data = self.capture_fingerprint()
        fingerprint_hash = self.generate_fingerprint_hash(fingerprint_data)

        if self.enrolled_fingerprints[user_id] == fingerprint_hash:
            return "Authentication successful."
        else:
            return "Authentication failed."

    def capture_fingerprint(self):
        # Simulate capturing a fingerprint. In a real system, this would interface with the hardware.
        simulated_fingerprint_data = f"fingerprint_{random.randint(1000, 9999)}"
        print(f"Captured fingerprint data: {simulated_fingerprint_data}")
        return simulated_fingerprint_data

    def generate_fingerprint_hash(self, fingerprint_data):
        # Hash the fingerprint data for storage and comparison
        fingerprint_hash = hashlib.sha256(fingerprint_data.encode()).hexdigest()
        print(f"Generated fingerprint hash: {fingerprint_hash}")
        return fingerprint_hash

def main():
    fas = FingerprintAuthenticationSystem()

    while True:
        print("\nFingerprint Authentication System")
        print("1. Enroll Fingerprint")
        print("2. Authenticate Fingerprint")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            message = fas.enroll_fingerprint(user_id)
            print(message)

        elif choice == '2':
            user_id = input("Enter user ID: ")
            message = fas.authenticate_fingerprint(user_id)
            print(message)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
1