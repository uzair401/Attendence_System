# Attendance System

## Overview
The Attendance System is a role-based web application designed to streamline attendance management for educational institutions and organizations. It employs advanced technologies like facial recognition and QR code scanning to automate the attendance marking process, enhancing efficiency and accuracy.

## Features
- **Role-Based Access Control**: Supports multiple user roles, including administrators, teachers, and students, each with specific permissions and functionalities.
- **Facial Recognition**: Utilizes facial recognition technology to automatically mark attendance based on students' faces during lectures.
- **QR Code Scanning**: Allows students to mark their attendance by scanning a unique QR code generated for each session, providing an alternative method for attendance tracking.
- **Attendance Management**: Admins and teachers can view, edit, and manage attendance records efficiently.
- **Reporting**: Generates detailed attendance reports for classes, individual students, and overall attendance statistics.
- **Responsive Design**: A user-friendly interface accessible on various devices, ensuring ease of use for all users.

## Technologies Used
- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap (AdminLTE3)
- **Facial Recognition**: [Specify any libraries or tools used, e.g., OpenCV]
- **QR Code Generation**: [Specify any libraries or tools used, e.g., qrcode]

## Installation

### Prerequisites
- Python 3.x
- PostgreSQL
- Virtual environment (recommended for isolation)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/uzair401/Attendence_System.git
   cd Attendence_System
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up your database:

Create a PostgreSQL database.
Update the database connection settings in settings.py.
Run migrations to set up the database schema:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the application at http://127.0.0.1:8000/.

Usage
Login: Users can log in using their credentials, with access tailored to their roles.
Mark Attendance:
For facial recognition: Ensure the camera is enabled for real-time facial recognition.
For QR code scanning: Students can scan the QR code displayed for each class session.
View Reports: Users can navigate to the reporting section to generate and view attendance reports based on various criteria.
