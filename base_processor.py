from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float):
        """Process the payment with the given amount."""
        pass
