drop table if exists departments cascade;
drop table if exists dept_emp cascade;
drop table if exists dept_manager cascade;
drop table if exists employees cascade;
drop table if exists salaries cascade;
drop table if exists titles cascade;


-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE "titles" (
    "title_id" VARCHAR(50) NOT NULL UNIQUE,
    "title" VARCHAR(50),
	"last_updated" timestamp DEFAULT localtimestamp NOT NULL,
    CONSTRAINT "pk_titles" PRIMARY KEY (
        "title_id"
     )
);

CREATE TABLE "departments" (
    "dept_no" VARCHAR(50) NOT NULL UNIQUE,
    "dept_name" VARCHAR(50),
	"last_updated" timestamp DEFAULT localtimestamp NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "dept_emp" (
    "ID" SERIAL NOT NULL,
    "emp_no" INT NOT NULL,
    "dept_no" VARCHAR(50) NOT NULL,
	"last_updated" timestamp DEFAULT localtimestamp NOT NULL,
    CONSTRAINT "pk_dept_emp" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "dept_manager" (
    "ID" SERIAL NOT NULL,
    "dept_no" VARCHAR(50) NOT NULL,
    "emp_no" INT NOT NULL,
	"last_updated" timestamp DEFAULT localtimestamp NOT NULL,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "employees" (
    "emp_no" INT NOT NULL UNIQUE,
    "emp_title_id" VARCHAR(50) NOT NULL,
    "birth_date" DATE,
    "first_name" VARCHAR(50),
    "last_name" VARCHAR(50),
    "sex" VARCHAR(10),
    "hire_date" DATE,
	"last_updated" timestamp DEFAULT localtimestamp NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "salaries" (
    "ID" SERIAL NOT NULL,
    "emp_no" INT NOT NULL,
    "salary" INT,
	"last_updated" timestamp DEFAULT localtimestamp NOT NULL,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "ID"
     )
);


ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "titles" ("title_id");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");


select * from titles;
select * from departments;
select * from dept_emp;
select * from dept_manager;
select * from employees;
select * from salaries;

