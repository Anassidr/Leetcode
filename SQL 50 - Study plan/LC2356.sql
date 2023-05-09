SELECT  teacher_id, COUNT(DISTINCT subject_id) cnt from teacher
GROUP BY teacher_id