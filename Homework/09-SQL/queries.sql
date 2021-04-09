SELECT emp.emp_no, emp.first_name, emp.last_name, emp.sex, sal.salary
FROM salaries AS sal
INNER JOIN employees AS emp ON
emp.emp_no = emp.emp_no;

SELECT * FROM employees
WHERE hire_date LIKE '1986%';


SELECT dept.dept_no, dept.dept_name, mang.emp_no,  emp.first_name, emp.last_name, mang.from_date, mang.to_date
FROM departments AS dept
INNER JOIN dept_manager AS mang ON
mang.dept_no = dept.dept_no
JOIN employees AS emp ON
emp.emp_no = mang.emp_no;

SELECT emp.emp_no,  emp.first_name, emp.last_name, dept.dept_name
FROM employees AS emp
INNER JOIN dept_emp AS dept_e ON
emp.emp_no = dept_e.emp_no
INNER JOIN departments AS dept ON
dept.dept_no = dept_e.dept_no;

SELECT * FROM employees
WHERE first_name LIKE 'Hercules'
AND last_name LIKE 'B';

SELECT emp.emp_no, emp.first_name, emp.last_name, dept.dept_name
FROM employees AS emp
INNER JOIN dept_emp AS dept_emp ON
emp.emp_no = dept_emp.emp_no
INNER JOIN departments AS dept ON
dept.dept_no = dept_emp.dept_no
WHERE dept.dept_name LIKE 'Sales';

SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
FROM employees AS emp
INNER JOIN dept_emp AS dept_e ON
emp.emp_no = dept_e.emp_no
INNER JOIN departments AS dept ON
dept.dept_no = dept_e.dept_no
WHERE dept.dept_name LIKE 'Development'
OR dept.dept_name LIKE 'Sales';


SELECT last_name, COUNT(*) AS frequency
FROM employees
GROUP BY last_name
ORDER BY frequency DESC;