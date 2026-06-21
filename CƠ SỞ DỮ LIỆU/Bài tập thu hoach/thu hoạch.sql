create table students (
    student_id int auto_increment primary key,
    full_name varchar(100),
    gender varchar(10),
    age int
);

create table courses (
    course_id int auto_increment primary key,
    course_name varchar(100),
    tuition_fee decimal(10, 2)
);

create table enrollments (
    enrollment_id int auto_increment primary key,
    student_id int,
    course_id int,
    enroll_date date,
    score decimal(4, 2),
    foreign key (student_id) references students(student_id),
    foreign key (course_id) references courses(course_id)
);

insert into students (full_name, gender, age) values
('nguyen van a', 'nam', 20),
('le thi b', 'nu', 19),
('tran van c', 'nam', 21),
('pham thi d', 'nu', 22),
('hoang van e', 'nam', 20),
('vu thi f', 'nu', 19),
('ngo van g', 'nam', 23),
('do thi h', 'nu', 21),
('bui van i', 'nam', 20),
('dang thi k', 'nu', 22);

insert into courses (course_name, tuition_fee) values
('java', 5000000),
('python', 4500000),
('mysql', 3000000),
('reactjs', 5500000),
('testing', 3500000);

insert into enrollments (student_id, course_id, enroll_date, score) values
(1, 1, '2026-06-01', 8.5),
(1, 3, '2026-06-02', 7.0),
(2, 1, '2026-06-01', 9.0),
(2, 2, '2026-06-03', 6.5),
(3, 2, '2026-06-03', 8.0),
(3, 4, '2026-06-04', 7.5),
(4, 3, '2026-06-02', 5.5),
(4, 5, '2026-06-05', 9.5),
(5, 1, '2026-06-01', 4.0),
(5, 4, '2026-06-04', 8.0),
(6, 5, '2026-06-05', 7.0),
(7, 1, '2026-06-01', 6.0),
(8, 2, '2026-06-03', 8.5),
(9, 4, '2026-06-04', 9.0),
(10, 1, '2026-06-01', 7.5);


select * from students;


select full_name as ten_sinh_vien, age as tuoi_sinh_vien from students;


update students set age = 22 where student_id = 1;


delete from enrollments where enrollment_id = 15;


select count(*) as tong_so_sinh_vien from students;


select max(score) as diem_cao_nhat, min(score) as diem_thap_nhat, avg(score) as diem_trung_binh from enrollments;


select sum(tuition_fee) as tong_hoc_phi from courses;


select c.course_name, count(e.student_id) as total_student
from courses c
left join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name;


select c.course_name, avg(e.score) as diem_trung_binh
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name;


select c.course_name, count(e.student_id) as total_student
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name
having count(e.student_id) > 2;


select s.*, e.score 
from students s
join enrollments e on s.student_id = e.student_id
where e.score = (select max(score) from enrollments);


select s.*, e.score 
from students s
join enrollments e on s.student_id = e.student_id
where e.score = (select min(score) from enrollments);


select distinct s.* from students s
join enrollments e on s.student_id = e.student_id
where e.score > (select avg(score) from enrollments);


select * from courses where tuition_fee = (select max(tuition_fee) from courses);


select s.full_name, c.course_name, e.score
from enrollments e
join students s on e.student_id = s.student_id
join courses c on e.course_id = c.course_id;


select s.full_name, c.course_name, e.enroll_date
from enrollments e
join students s on e.student_id = s.student_id
join courses c on e.course_id = c.course_id;


select c.course_name, count(e.student_id) as total_student
from courses c
left join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name;


select c.course_name, avg(e.score) as diem_trung_binh
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name;


select c.course_name, count(e.student_id) as total_student
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name
having count(e.student_id) = (
    select max(student_count) 
    from (select count(student_id) as student_count from enrollments group by course_id) as temp
);


select s.full_name, count(e.course_id) as total_course
from students s
join enrollments e on s.student_id = e.student_id
group by s.student_id, s.full_name
having count(e.course_id) = (
    select max(course_count) 
    from (select count(course_id) as course_count from enrollments group by student_id) as temp
);

select s.full_name, c.course_name, e.score
from enrollments e
join students s on e.student_id = s.student_id
join courses c on e.course_id = c.course_id
where e.score > (
    select avg(score) 
    from enrollments 
    where course_id = e.course_id
);