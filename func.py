from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, first_name, last_name, sgk):
        self._first_name = first_name
        self._last_name = last_name
        self._sgk = sgk

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def sgk(self):
        return self._sgk

    @abstractmethod
    def payment(self):
        raise NotImplementedError

    def __repr__(self):
        return f"Patient (First Name='{self.first_name}', Last Name='{self.last_name}', Social Seq Num='{self.sgk}')"

class RegularPatient(Patient):
 
    def __init__(self, first_name, last_name, sgk, weekly_payment):
        super().__init__(first_name, last_name, sgk)
        self.weekly_payment = weekly_payment
 
    @property
    def weekly_payment(self):
        return self._weekly_payment
    
    @weekly_payment.setter
    def weekly_payment(self, v):
        if v<0:
            raise ValueError("Weekly payment must be positive or 0")
        self._weekly_payment = v

    def payment(self):
        return self.weekly_payment

    def __repr__(self):
        return (f"Regular Patient: (First Name= {self.first_name}, Last Name= {self.last_name}, Social Seq Num= {self.sgk}, Weekly Payment= {self.weekly_payment})")

class InstantPatient(Patient):

    def __init__(self, first_name, last_name, sgk, payment_per_hour, hours):
        super().__init__(first_name, last_name, sgk)
        self.hours = hours
        self.payment_per_hour = payment_per_hour

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        if hours < 0 or hours > 168:
            raise ValueError("People can stay 168 hours max")
        self._hours = hours

    @property
    def payment_per_hour(self):
        return self._payment_per_hour

    @payment_per_hour.setter
    def payment_per_hour(self, payment_per_hour):
        if payment_per_hour < 0:
            raise ValueError("Payment per hour must be 0 or positive")
        self._payment_per_hour = payment_per_hour

    def payment(self):
        if self.hours>40:
            overtime_hours = self.hours - 40
            overtime_pay = 1.5 * self.payment_per_hour * overtime_hours
            return overtime_pay +  40*self.payment_per_hour
        else:
            return self.hours * self.payment_per_hour
        
    def __repr__(self):
        return (f"Instant Patient: (First Name= {self.first_name}, Last Name= {self.last_name}, Social Seq Num= {self.sgk}) ({self.hours} hours at {self.payment_per_hour} $ per hour)" )