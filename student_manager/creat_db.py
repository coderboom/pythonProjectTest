import pymysql
import db

# 连接数据库
db = pymysql.connect(**db.db_dict)
cursor = db.cursor()

# 创建学生表
create_student_sql = ("CREATE TABLE IF NOT EXISTS students "
                      "(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100), phone_number VARCHAR(20));")
cursor.execute(create_student_sql)

# 创建学科成绩表
create_subject_scores_sql = ("CREATE TABLE IF NOT EXISTS subject_scores "
                             "(id INT AUTO_INCREMENT PRIMARY KEY,student_id INT,subject VARCHAR(50),"
                             "score DECIMAL(5,2),FOREIGN KEY (student_id) REFERENCES students(id) );")
cursor.execute(create_subject_scores_sql)

db.commit()
