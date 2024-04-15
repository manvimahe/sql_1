##parsing on sample queries  : 

```
SELECT e.employee_id,
       e.first_name,
       e.last_name,
       COUNT(d.dependent_id) AS num_dependents
FROM employees e
LEFT JOIN dependents d ON e.employee_id = d.employee_id
GROUP BY e.employee_id
ORDER BY num_dependents DESC"
```

Columns Used :-
 ['employees.employee_id', 'employees.first_name', 'employees.last_name', 'dependents.dependent_id', 'dependents.employee_id']


Tables Used :-
 ['employees', 'dependents']


Subqueries Used :-
 {}


Column aliases Used :-
 {'num_dependents': 'dependents.dependent_id'}

```
SELECT d.department_name,
       SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY total_salary DESC"
```
Columns Used :-
 ['departments.department_name', 'employees.salary', 'employees.department_id', 'departments.department_id']


Tables Used :-
 ['employees', 'departments']


Subqueries Used :-
 {}


Column aliases Used :-
 {'total_salary': 'employees.salary'}

```
SELECT e.first_name,
       e.last_name,
       c.country_name,
       r.region_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
JOIN countries c ON l.country_id = c.country_id
JOIN regions r ON c.region_id = r.region_id"
```
Columns Used :-
 ['employees.first_name', 'employees.last_name', 'countries.country_name', 'regions.region_name', 'employees.department_id', 'departments.department_id', 'departments.location_id', 'locations.location_id', 'locations.country_id', 'countries.country_id', 'countries.region_id', 'regions.region_id']


Tables Used :- 
 ['employees', 'departments', 'locations', 'countries', 'regions']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
SELECT e.employee_id,
       e.first_name,
       e.last_name,
       COUNT(d.dependent_id) AS num_dependents
FROM employees e
LEFT JOIN dependents d ON e.employee_id = d.employee_id
GROUP BY e.employee_id"
```
Columns Used :-
 ['employees.employee_id', 'employees.first_name', 'employees.last_name', 'dependents.dependent_id', 'dependents.employee_id']


Tables Used :-
 ['employees', 'dependents']


Subqueries Used :- 
 {}


Column aliases Used :-
 {'num_dependents': 'dependents.dependent_id'}

```
SELECT j.job_title,
       AVG(e.salary) AS average_salary
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title"
```
Columns Used :-
 ['jobs.job_title', 'employees.salary', 'employees.job_id', 'jobs.job_id']


Tables Used :-
 ['employees', 'jobs']


Subqueries Used :-
 {}


Column aliases Used :-
 {'average_salary': 'employees.salary'}

```
SELECT e.first_name,
       e.last_name,
       j.job_title,
       e.hire_date
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
WHERE e.hire_date > '1995-01-01'
ORDER BY e.hire_date"
```
Columns Used :-
 ['employees.first_name', 'employees.last_name', 'jobs.job_title', 'employees.hire_date', 'employees.job_id', 'jobs.job_id']


Tables Used :-
 ['employees', 'jobs']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
SELECT d.department_name,
       e.first_name,
       e.last_name,
       e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE (e.department_id,
       e.salary) IN
    (SELECT department_id,
            MAX(salary)
     FROM employees
     GROUP BY department_id)"
```
Columns Used :-
 ['departments.department_name', 'employees.first_name', 'employees.last_name', 'employees.salary', 'employees.department_id', 'departments.department_id', 'department_id', 'salary']


Tables Used :-
 ['employees', 'departments'] 


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
SELECT e.first_name AS employee_first_name,
       e.last_name AS employee_last_name,
       m.first_name AS manager_first_name,
       m.last_name AS manager_last_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id"
```
Columns Used :-
 ['employees.first_name', 'employees.last_name', 'employees.manager_id', 'employees.employee_id']


Tables Used :-
 ['employees']


Subqueries Used :-
 {}


Column aliases Used :-
 {'employee_first_name': 'employees.first_name', 'employee_last_name': 'employees.last_name', 'manager_first_name': 'employees.first_name', 'manager_last_name': 'employees.last_name'}

```
SELECT d.department_name,
       SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name"
```
Columns Used :-
 ['departments.department_name', 'employees.salary', 'employees.department_id', 'departments.department_id']


Tables Used :-
 ['employees', 'departments']


Subqueries Used :-
 {}


Column aliases Used :-
 {'total_salary': 'employees.salary'}

```
SELECT e.employee_id,
       e.first_name,
       e.last_name,
       d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id"
```
Columns Used :- 
 ['employees.employee_id', 'employees.first_name', 'employees.last_name', 'departments.department_name', 'employees.department_id', 'departments.department_id']


Tables Used :-
 ['employees', 'departments']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
SELECT *
FROM regions
```
Columns Used :-
 ['*']


Tables Used :-
 ['regions']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
INSERT INTO dependents(dependent_id, first_name, last_name, relationship, employee_id)     
VALUES (30,'Sandra','Taylor','Child',176)"
```
Values Inserted :-
 [30, 'Sandra', 'Taylor', 'Child', 176]


Columns Used :-
 ['dependent_id', 'first_name', 'last_name', 'relationship', 'employee_id']


Tables Used :-
 ['dependents']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
INSERT INTO dependents(dependent_id, first_name, last_name, relationship, employee_id)     
VALUES (29,'Alec','Partners','Child',146)"
```
Values Inserted :-
 [29, 'Alec', 'Partners', 'Child', 146]


Columns Used :-
 ['dependent_id', 'first_name', 'last_name', 'relationship', 'employee_id']


Tables Used :-
 ['dependents']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
INSERT INTO dependents(dependent_id, first_name, last_name, relationship, employee_id)     
VALUES (28,'Woody','Russell','Child',145)"
```
Values Inserted :- 
 [28, 'Woody', 'Russell', 'Child', 145]


Columns Used :-
 ['dependent_id', 'first_name', 'last_name', 'relationship', 'employee_id']


Tables Used :-
 ['dependents']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
INSERT INTO dependents(dependent_id, first_name, last_name, relationship, employee_id)     
VALUES (27,'Julia','Raphaely','Child',114)"
```
Values Inserted :-
 [27, 'Julia', 'Raphaely', 'Child', 114]


Columns Used :-
 ['dependent_id', 'first_name', 'last_name', 'relationship', 'employee_id']


Tables Used :-
 ['dependents']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
INSERT INTO dependents(dependent_id, first_name, last_name, relationship, employee_id)     
VALUES (26,'Rip','Colmenares','Child',119)"
```
Values Inserted :-
 [26, 'Rip', 'Colmenares', 'Child', 119]


Columns Used :-
 ['dependent_id', 'first_name', 'last_name', 'relationship', 'employee_id']


Tables Used :-
 ['dependents']


Subqueries Used :-
 {} 


Column aliases Used :-
 {}

```
INSERT INTO dependents(dependent_id, first_name, last_name, relationship, employee_id)     
VALUES (25,'Kevin','Himuro','Child',118)"
```
Values Inserted :-
 [25, 'Kevin', 'Himuro', 'Child', 118]


Columns Used :-
 ['dependent_id', 'first_name', 'last_name', 'relationship', 'employee_id']


Tables Used :-
 ['dependents']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

```
INSERT INTO dependents(dependent_id, first_name, last_name, relationship, employee_id)     
VALUES (24,'Cameron','Tobias','Child',117)"
```
Values Inserted :-
 [24, 'Cameron', 'Tobias', 'Child', 117]


Columns Used :-
 ['dependent_id', 'first_name', 'last_name', 'relationship', 'employee_id']


Tables Used :-
 ['dependents']


Subqueries Used :-
 {} 


Column aliases Used :-
 {}

```
INSERT INTO dependents(dependent_id, first_name, last_name, relationship, employee_id)     
VALUES (23,'Sandra','Baida','Child',116)"
```
Values Inserted :-
 [23, 'Sandra', 'Baida', 'Child', 116]


Columns Used :-
 ['dependent_id', 'first_name', 'last_name', 'relationship', 'employee_id'] 


Tables Used :-
 ['dependents']


Subqueries Used :-
 {}


Column aliases Used :-
 {}

