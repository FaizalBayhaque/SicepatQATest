-- query no 1 :
select emp_name, emp_status from tbl_employee;

-- query no 2 : 
select e.emp_name, i.emp_income from tbl_employee e left join tbl_income i 
on e.emp_code = i.emp_code where e.emp_status = 'R';

-- query no 3 :
select e.emp_code, e.emp_name, e.emp_status, i.emp_income from tbl_employee e left join tbl_income i 
on e.emp_code = i.emp_code order by i.emp_income desc;