# Patient Billing System

This Python project models a hospital billing system with two types of patients: `RegularPatient` and `InstantPatient`.

## Features

- The `Patient` class serves as an abstract base class (ABC) defining a common interface for all patients.
- The `RegularPatient` class represents patients with weekly payments.
- The `InstantPatient` class represents patients with payments based on hours worked.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/erblgc/patient-billing-system.git
    ```
   
## Navigate to the project directory:

    cd patient-billing-system
    
## Run the main script:

    python main.py
    
## Usage

Instantiate a RegularPatient:

    patient1 = RegularPatient('Jack', 'Z', 123456, 60)

Instantiate an InstantPatient:

    patient2 = InstantPatient('Mike', 'X', 654321, 45, 50)

Use the payment method to calculate payments:

    print('Payment =', patient1.payment(), '$')
    print('Payment =', patient2.payment(), '$')

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.
