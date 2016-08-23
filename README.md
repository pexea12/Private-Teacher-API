# Private-Teacher-API
Web service for Private-Teacher project. Written by Flask (Python)

## Users
`/api/login` (**_Guest_**) - **POST**  
* Login
* Params: `username`, `password`

`/api/logout` (**_Admin, Member_**) - **GET**  
* Logout

`/api/users` (**_Admin_**) - **GET**  
* View the users table
* Params: 
  * `limit`: Limit the number of records
  * `id`, `name`, `image`, `phone`, `email`
  * `priviledge`: `Admin` or `Member`

`/api/users/<int:user_id>` (**_Admin, Member_**) - **GET**  
* View user by ID. Member can only view their own profile

`/api/users/add` (**_Admin, Guest_**) - **POST**  
* Add new user or register
* Params: `name`, `email`, `password`, `image`, `phone`, `priviledge`

`/api/users/update/<int:user_id>` (**_Admin, Member_**) - **PUT**  
* Update the profile of user by ID. Member can only update their own profile
* Params: `name`, `email`, `password`, `image`, `phone`, `priviledge`

`/api/users/delete/<int:user_id>` (**_Admin_**) - **DELETE**  
* Delete the profile of user by ID

## Students

`/api/students/list` (**All**) - **GET**
* View the students table
* Params: 
  * `id`, `name`, `email`, `phone`, `image`
  * `price_per_hour`: The price that the student expects to pay his or her teacher
  * `school`: The school of the student
  * `level`: The current level of the student
  * `user_id`: The ID of the user who creates this student profile
  * `location`: The location of the student
  * `limit`: Limit the number of records

`/api/students/<int:student_id>` (**All**) - **GET**
* View the student by ID

`/api/students/add` (**_Admin, Member_**) - **POST**
* Add new student profile
* Params: 
  * `name`, `email`, `phone`, `image`
  * `price_per_hour`: The price that the student expects to pay his or her teacher
  * `school`: The school of the student
  * `level`: The current level of the student
  * `user_id`: The ID of the user who creates this student profile
  * `description`: What the student wants to say about him or her
  * `location`: The location of the student

`/api/students/update/<int:student_id>` (**_Admin, Member_**) - **PUT**
* Update the info of the student by student ID. Members can only update the student profiles that they create
* Params: The same params as `/api/students/add`

`/api/students/delete/<int:student_id>` (**_Admin, Member_**) - **DELETE**
* Delete the student profiles by student ID. Members can only delete their profiles


## Teachers

`/api/teachers/list` (**All**) - **GET**
* View the teachers table
* Params: 
  * `id`, `name`, `email`, `phone`, `image`
  * `salary_per_hour`: The salary that the teacher expects to receive from his or her student
  * `job`: The current job of the teacher
  * `work_place`: The current work place of the teacher
  * `level_to_teach`: The level of students whom the teacher expects to teach
  * `user_id`: The ID of the user who creates this teacher profile
  * `location`: The location of the teacher
  * `limit`: Limit the number of records

`/api/teachers/<int:teacher_id>` (**All**) - **GET**
* View the teacher by ID

`/api/teachers/add` (**_Admin, Member_**) - **POST**
* Add new teacher profile
* Params: 
  * `id`, `name`, `email`, `phone`, `image`
  * `salary_per_hour`: The salary that the teacher expects to receive from his or her student
  * `job`: The current job of the teacher
  * `work_place`: The current work place of the teacher
  * `level_to_teach`: The level of students whom the teacher expects to teach
  * `user_id`: The ID of the user who creates this teacher profile
  * `description`: What the teacher wants to say about him or her
  * `location`: The location of the teacher
  * `rating`: The average rating of the teacher
  * `rating_number`: The number of ratings that the teacher receives
  * `limit`: Limit the number of records

`/api/teachers/update/<int:teacher_id>` (**_Admin, Member_**) - **PUT**
* Update the info of the teacher by teacher ID. Members can only update the teacher profiles that they create
* Params: The same params as `/api/teachers/add`

`/api/teachers/delete/<int:teacher_id>` (**_Admin_**) - **DELETE**
* Delete the teacher profiles by teacher ID. Members can only delete their profiles
