from payment_modes import PaymentMode
from paypal_processor import PayPalProcessor
from googlepay_processor import GooglePayProcessor
from creditcard_processor import CreditCardProcessor
from invalid_processor import InvalidProcessor

PROCESSOR_MAP = {
    PaymentMode.PAYPAL: PayPalProcessor,
    PaymentMode.GOOGLEPAY: GooglePayProcessor,
    PaymentMode.CREDITCARD: CreditCardProcessor,
    PaymentMode.INVALID: InvalidProcessor
}

def checkout(mode: PaymentMode, amount: float):
    processor_class = PROCESSOR_MAP.get(mode, InvalidProcessor)
    processor = processor_class()
    processor.process(amount)
