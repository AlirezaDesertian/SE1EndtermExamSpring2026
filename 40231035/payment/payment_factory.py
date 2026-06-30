class PaymentProcessor:
    def pay(self, amount):
        pass


class PaymentFactory:
    @staticmethod
    def create_processor(method: str) -> PaymentProcessor:
        pass