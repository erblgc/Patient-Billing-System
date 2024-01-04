from func import Patient, RegularPatient, InstantPatient

patient1 = RegularPatient('Jack', 'Z', 123456, 60)
patient2 = InstantPatient('Mike', 'X', 654321, 45, 50) 

patients = [patient1, patient2]

for patient in patients:
    print(patient)
    print('Payment =', patient.payment(), '$')
    print()

print(str(RegularPatient('Jack', 'Z', 123456, 50)))
print('Payment =', patient1.payment(), '$')  

print(str(InstantPatient('Mike', 'X', 654321, 45, 50))) 
print('Payment =', patient2.payment(), '$')  