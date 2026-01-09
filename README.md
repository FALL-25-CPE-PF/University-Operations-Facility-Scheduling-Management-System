# University Facility Booking & Management System

A role-based console application developed in Python to automate the booking, approval, and scheduling of university facilities such as lecture halls, laboratories, and event spaces.

---

## 📌 Project Description
The University Facility Booking & Management System is designed to replace manual and paper-based facility booking with an automated, structured, and transparent digital workflow.  
The system uses Role-Based Access Control (RBAC) and CSV-based persistent storage to efficiently manage users, facilities, booking requests, and schedules.

---

## 🎯 Objectives
- Implement user authentication with role-based access
- Automate facility booking and approval process
- Reduce scheduling conflicts and manual workload
- Maintain persistent data using CSV files
- Provide a clean, menu-driven console interface

---

## ✨ Key Features
- User Registration & Login
- Role-Based Access Control (Admin, Teacher, Student)
- Facility Management (Add, View, Update Status)
- Booking Request Submission & Tracking
- Admin Approval / Rejection Workflow
- Automated Schedule Generation
- View Personal Requests & Schedules
- Change Password Functionality
- CSV-Based Persistent Storage

---

## 👥 User Roles & Permissions

### 🔹 Admin
- Add new facilities
- View all facilities
- Update facility status (Active / Inactive)
- View all booking requests
- Approve or reject requests
- Generate final schedules

### 🔹 Teacher
- Request facilities for lectures or labs
- View own booking requests
- View assigned schedule

### 🔹 Student
- Request facilities for practice or events
- View own booking requests
- Cancel pending requests

---

## 🗂️ Project Structure

University_Facility_Management_System.py
users.csv
facilities.csv
requests.csv
schedule.csv
README.md


---

## ⚙️ Technologies Used
- Programming Language: Python 3
- Modules: csv, os
- Data Storage: CSV Files
- Interface: Console / Terminal
- Version Control: Git & GitHub

---

## ▶️ How to Run the Project
1. Clone the repository
2. Ensure Python 3 is installed
3. Open terminal in project directory
4. Run the command:

```bash
python University_Facility_Management_System.py
