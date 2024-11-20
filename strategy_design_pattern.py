from abc import ABC, abstractmethod


# Step 1: Define the Strategy interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
