SELECT s.student_id, s.student_name, sub.subject_name, IFNULL(COUNT(e.student_id), 0) as attended_exams
FROM students s
CROSS JOIN subjects sub
LEFT JOIN examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, sub.subject_name
ORDER BY s.student_id, sub.subject_name