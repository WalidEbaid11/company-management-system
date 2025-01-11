# Company Management System – Back End

## Overview
The **Company Management System** is a back-end application designed to streamline the management of companies, departments, employees, and projects. It provides comprehensive CRUD operations, a workflow for employee performance review cycles, and role-based access control to ensure secure data handling.

This project demonstrates proficiency in back-end development, problem-solving, and attention to detail. It also highlights the ability to meet deadlines and handle complex requirements under pressure.

---

## Features
### Core Features:
- **CRUD Operations**:
  - Manage companies, departments, employees, and projects.
- **Employee Performance Review Workflow**:
  - Stages: Pending Review, Review Scheduled, Feedback Provided, Under Approval, Review Approved, Review Rejected.
  - Transitions between stages are well-defined and managed.
- **Role-Based Access Control**:
  - Three roles: Admin, Manager, Employee.
  - Different access levels for each role.
- **Secure Data Handling**:
  - Authentication and authorization using Django’s built-in mechanisms.

### Bonus Features (Optional):
- **Project Management APIs**:
  - RESTful endpoints for creating, updating, retrieving, and deleting projects.
- **Logging**:
  - Tracks application behavior and captures errors for debugging.

---

## Tech Stack
- **Framework**: Django
- **Database**: PostgreSQL (or SQLite for development)
- **Authentication**: Django Authentication System
- **API Design**: Django REST Framework
- **Testing**: Unit and integration tests using Django’s testing framework
- **Version Control**: Git & GitHub

---
![My Image](https://github.com/WalidEbaid11/YHealth/blob/main/Screenshot/Screenshot%202024-12-03%20104854.jpg)
---
## Project Structure
The project is structured as follows to facilitate development and future maintenance:

```bash
company_management/
├── manage.py                         # The main file for managing the project
├── company_management/                # Main project settings
│   ├── __init__.py
│   ├── asgi.py                       # For running the project with ASGI
│   ├── settings.py                   # Project settings
│   ├── urls.py                       # Main project URLs
│   └── wsgi.py                       # For running the project with WSGI
├── management/                       # Application for managing companies
│   ├── __init__.py
│   ├── admin.py                      # Customization for the admin panel
│   ├── apps.py                       # Application setup
│   ├── migrations/                   # Database migration files
│   │   └── __init__.py
│   ├── models.py                     # Models for the application
│   ├── views.py                      # Views for data management
│   ├── tests.py                      # Project tests
│   ├── serializers.py                # Serializers for converting data to JSON
│   ├── forms.py                      # Form models for user interaction
│   ├── urls.py                       # URLs specific to the company management app
│   └── templates/management/         # HTML templates for the application
│       ├── base.html                 # Base template
│       ├── home.html                 # Home page
│       ├── companies.html            # Display all companies
│       ├── company_detail.html       # Details of a specific company
│       ├── departments.html          # Display all departments
│       ├── department_detail.html    # Details of a specific department
│       ├── employees.html            # Display all employees
│       ├── employee_detail.html      # Details of a specific employee
│       ├── projects.html             # Display all projects
│       └── project_detail.html       # Details of a specific project
├── requirements.txt                  # List of required packages to run the project
└── README.md                         # Project description and usage instructions
