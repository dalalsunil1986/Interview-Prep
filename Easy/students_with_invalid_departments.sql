-- # Find all students that are in departments that no longer exist
SELECT S.id, S.name
FROM Students S
WHERE S.department_id NOT IN (
    SELECT id
    FROM Departments
);