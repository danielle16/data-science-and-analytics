
CREATE TABLE "departments" (
    "dept_no" VARCHAR   NOT NULL,
    "dept_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

select * from dept_manager
CREATE TABLE dept_emp (
    emp_no varchar   NOT NULL,
    dept_no varchar   NOT , 
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
);

CREATE TABLE dept_manager (
    dept_no varchar   NOT NULL,
    emp_no varchar   NOT NULL, 
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

DROP TABLE titles
CREATE TABLE "employees" (
    "emp_no" VARCHAR   NOT NULL,
    "emp_title_id" VARCHAR   NOT NULL,
    "birth_date" VARCHAR   NOT NULL,
    "first_name" VARCHAR   NOT NULL,
    "last_name" VARCHAR   NOT NULL,
    "sex" VARCHAR   NOT NULL,
    "hire_date" VARCHAR   NOT NULL
);

CREATE TABLE "salaries" (
    "emp_no" VARCHAR   NOT NULL,
    "salary" VARCHAR   NOT NULL, 
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

CREATE TABLE "titles" (
    "title_id" VARCHAR   NOT NULL,
    "title" VARCHAR   NOT NULL
);