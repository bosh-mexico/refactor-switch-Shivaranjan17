from base_processor import PaymentProcessor

class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")
