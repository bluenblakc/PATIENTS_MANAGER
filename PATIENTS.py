import json
import os

# file where all patient info will be saved
data_file = "patients.json"


# load all patients from file
def load_patients():
    if os.path.isfile(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return []


# write updated data back to file
def save_patients(p_list):
    with open(data_file, "w") as f:
        json.dump(p_list, f, indent=4)


# add patient function
def add_patient():
    all_patients = load_patients()
    print("\n--- Add New Patient ---")

    pid = input("Patient ID: ")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    illness = input("Disease / Issue: ")
    doctor = input("Doctor Assigned: ")
    admit_date = input("Admit Date: ")
    phone = input("Contact Number: ")

    patient_data = {
        "id": pid,
        "name": name,
        "age": age,
        "gender": gender,
        "illness": illness,
        "doctor": doctor,
        "admit_date": admit_date,
        "phone": phone
    }

    all_patients.append(patient_data)
    save_patients(all_patients)
    print("Patient record saved.\n")


# view all patients
def view_all():
    data = load_patients()
    print("\n--- All Patient Records ---")

    if len(data) == 0:
        print("No patients found.\n")
        return

    for p in data:
        print("-------------------------------")
        print("ID:", p["id"])
        print("Name:", p["name"])
        print("Age:", p["age"])
        print("Gender:", p["gender"])
        print("Disease:", p["illness"])
        print("Doctor:", p["doctor"])
        print("Admit Date:", p["admit_date"])
        print("Phone:", p["phone"])
    print("-------------------------------\n")


# search using patient ID
def search_patient():
    data = load_patients()
    pid = input("\nEnter ID to search: ")

    for p in data:
        if p["id"] == pid:
            print("\n--- Patient Found ---")
            print("ID:", p["id"])
            print("Name:", p["name"])
            print("Age:", p["age"])
            print("Gender:", p["gender"])
            print("Disease:", p["illness"])
            print("Doctor:", p["doctor"])
            print("Admit Date:", p["admit_date"])
            print("Phone:", p["phone"], "\n")
            return

    print("No record with that ID.\n")


# update patient details
def update_patient():
    data = load_patients()
    pid = input("\nEnter Patient ID to update: ")

    for p in data:
        if p["id"] == pid:
            print("\n--- Update (Leave blank to keep same) ---")

            new_name = input(f"Name [{p['name']}]: ")
            new_age = input(f"Age [{p['age']}]: ")
            new_gender = input(f"Gender [{p['gender']}]: ")
            new_ill = input(f"Disease [{p['illness']}]: ")
            new_doc = input(f"Doctor [{p['doctor']}]: ")
            new_date = input(f"Admit Date [{p['admit_date']}]: ")
            new_phone = input(f"Phone [{p['phone']}]: ")

            # updating only if user typed something
            if new_name: p["name"] = new_name
            if new_age: p["age"] = new_age
            if new_gender: p["gender"] = new_gender
            if new_ill: p["illness"] = new_ill
            if new_doc: p["doctor"] = new_doc
            if new_date: p["admit_date"] = new_date
            if new_phone: p["phone"] = new_phone

            save_patients(data)
            print("Record updated.\n")
            return

    print("No patient found with that ID.\n")


# delete a patient record
def delete_patient():
    data = load_patients()
    pid = input("\nEnter Patient ID to delete: ")

    updated_list = [p for p in data if p["id"] != pid]

    if len(updated_list) != len(data):
        save_patients(updated_list)
        print("Record deleted.\n")
    else:
        print("No record found to delete.\n")


# menu screen
def main_menu():
    while True:
        print("""
=============================
   Hospital Patient System
=============================
1. Add Patient
2. View All Patients
3. Search Patient
4. Update Details
5. Delete Patient
6. Exit
""")

        option = input("Choose option: ")

        if option == "1":
            add_patient()
        elif option == "2":
            view_all()
        elif option == "3":
            search_patient()
        elif option == "4":
            update_patient()
        elif option == "5":
            delete_patient()
        elif option == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Start program
main_menu()
