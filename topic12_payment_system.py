from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def makePayment(self):
        pass

class MobileMoneyPayment(Payment):
    def makePayment(self):
        print("Payment made using Mobile Money")

class CardPayment(Payment):
    def makePayment(self):
        print("Payment made using Bank Card")

mobile_payment = MobileMoneyPayment()
card_payment = CardPayment()

mobile_payment.makePayment()
card_payment.makePayment()

