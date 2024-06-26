# Employee Management System

This project is a simple Flask application for managing employee data using SQLite as the database.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/kill3rstabs/EmployeeManagementSystem.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Create the SQLite database:**

    ```bash
    python schema.py
    ```

## Running the Application

```bash
flask run

```
# Application Access

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser to access the application.

## API Endpoints

### Retrieve all employees
- **Endpoint:** /
- **Method:** GET

### Calculate Retention Rate
- **Endpoint:** /retention_rate/<start_date>/<end_date>
- **Method:** GET
- **Example:** /retention_rate/2022-01-01/2023-01-01

### Filter by Salary Range
- **Endpoint:** /filter_by_salary_range/<int:min_salary>/<int:max_salary>
- **Method:** GET
- **Example:** /filter_by_salary_range/50000/80000

### Get Top Earners
- **Endpoint:** /top_earners/<int:n>
- **Method:** GET
- **Example:** /top_earners/5

### Filter Employees by Experience Level
- **Endpoint:** /filter_by_experience/int:min_experience/int:max_experience
- **Method:** GET
- **Example:** /filter_by_experience/1/3

### Calculate Average Salary by Position
- **Endpoint:** /average_salary_by_position
- **Method:** GET
