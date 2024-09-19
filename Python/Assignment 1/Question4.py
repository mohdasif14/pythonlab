#Question 4
# Function to capture patient information

def capture_patient_info():
    firstname = input("Enter the patient's first name: ")
    lastname = input("Enter the patient's last name: ")
    ssn = input("Enter the patient's Special Security Number (SSN): ")

    has_insurance = input("Does the patient have insurance? (yes/no): ").strip().lower()
    if has_insurance == 'yes':
        has_insurance = True
    elif has_insurance == 'no':
        has_insurance = False
    else:
        print("Invalid input, assuming no insurance.")
        has_insurance = False

    billing_amount = float(input("Enter the patient's billing amount: $"))

    patient_info = {
        'Firstname': firstname,
        'Lastname': lastname,
        'SSN': ssn,
        'HasInsurance': has_insurance,
        'BillingAmount': billing_amount
    }

    return patient_info


patient = capture_patient_info()

print("\nPatient Information:")
for key, value in patient.items():
    print(f"{key}: {value}")