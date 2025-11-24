# Hospital Patient Management System -- Statement
# Overview
A Python-based CRUD system for managing hospital patient records.\
Data is stored in a JSON file (`patients.json`) for persistence.

# Features Implemented
-   Add new patient records with full details.
-   View all patient records.
-   Search a patient using their ID.
-   Update patient information while preserving previous values if left
    blank.
-   Delete patient records.
-   Data is saved and loaded automatically from a JSON file.
-   Simple text‑based menu interface.

# Challenges Faced
1.  Ensuring data persistence using JSON.
2.  Handling missing or invalid patient IDs.
3.  Preventing data loss while updating only specific fields.
4.  Managing empty inputs during updates.
5.  Validating user inputs (ID, age, phone, etc.) to prevent invalid
    entries.
6.  Avoiding crashes when JSON file does not exist on first run.

# Future Enhancements
-   Add validation for numeric fields (age, phone).
-   Add patient discharge date and status.
-   Implement sorting and filtering options.
-   Add export options (CSV, Excel).
-   Add login system (admin, doctor access roles).
-   Build a GUI using Tkinter, PyQt, or a web dashboard using
    Flask/Django.
-   Implement backup/restore for patient data.
-   Add better error handling and confirmations before updates/deletes.

# Conclusion
This program offers a simple but functional hospital management system
using Python and JSON.\
It can be extended into a full hospital administration tool with UI,
user roles, and advanced features.
