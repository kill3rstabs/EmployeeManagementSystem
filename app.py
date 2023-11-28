from flask import Flask, render_template, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = 'employee_database.db'


def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall() if not one else cursor.fetchone()
    conn.close()
    return result


@app.route('/')
def index():
    query = 'SELECT * FROM employees'
    employees = query_db(query)
    result_list = [
        {
            'id': row['id'],
            'name': row['name'],
            'position': row['position'],
            'salary': row['salary'],
            'joining_date': row['joining_date']
        }
        for row in employees
    ]
    return jsonify(result_list)


@app.route('/average_salary_by_position')
def average_salary_by_position():
    query = 'SELECT position, AVG(salary) as avg_salary FROM employees GROUP BY position'
    average_salaries = query_db(query)

    result_dict = [
        {   
            'position': row['position'],
            'average_salary': row['avg_salary']
        
        }
        
        for row in average_salaries
    ]

    return jsonify(result_dict)


@app.route('/filter_by_experience/<int:min_experience>/<int:max_experience>')
def filter_by_experience(min_experience, max_experience):
    current_date = datetime.now()
    query = '''
        SELECT * 
        FROM employees 
        WHERE strftime('%Y', 'now') - strftime('%Y', joining_date) BETWEEN ? AND ?
    '''
    filtered_employees = query_db(query, (min_experience, max_experience))
    result_list = [
        {
            'id': row['id'],
            'name': row['name'],
            'position': row['position'],
            'salary': row['salary'],
            'joining_date': row['joining_date']
        }
        for row in filtered_employees
    ]
    return jsonify(result_list)


@app.route('/top_earners/<int:n>')
def top_earners(n):
    query = 'SELECT * FROM employees ORDER BY salary DESC LIMIT ?'
    top_earners = query_db(query, (n,))
    result_list = [
        {
            'id': row['id'],
            'name': row['name'],
            'position': row['position'],
            'salary': row['salary'],
            'joining_date': row['joining_date']
        }
        for row in top_earners
    ]
    return jsonify(result_list)


@app.route('/retention_rate/<start_date>/<end_date>')
def retention_rate(start_date, end_date):
    query = '''
        SELECT position, 
               (COUNT(CASE WHEN joining_date <= ? THEN 1 END) - COUNT(CASE WHEN joining_date <= ? THEN 1 END)) * 100.0 / COUNT(*) as retention_rate
        FROM employees
        GROUP BY position
    '''
    retention_rates = query_db(query, (end_date, start_date))
    result_list = [
        {
            'position': row['position'],
            'retention_rate': row['retention_rate']
        }
        for row in retention_rates
    ]
    return jsonify(result_list)


@app.route('/filter_by_salary_range/<int:min_salary>/<int:max_salary>')
def filter_by_salary_range(min_salary, max_salary):
    query = 'SELECT * FROM employees WHERE salary BETWEEN ? AND ?'
    filtered_employees = query_db(query, (min_salary, max_salary))
    result_list = [
        {
            'id': row['id'],
            'name': row['name'],
            'position': row['position'],
            'salary': row['salary'],
            'joining_date': row['joining_date']
        }
        for row in filtered_employees
    ]
    return jsonify(result_list)


if __name__ == '__main__':
    app.run(debug=True)
