from base_processor import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing Credit Card payment of ${amount:.2f}")
