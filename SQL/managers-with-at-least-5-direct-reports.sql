-- # Write your MySQL query statement below
SELECT manager.name AS name
FROM Employee as manager RIGHT JOIN Employee # every employee, must have a manager
ON manager.id = Employee.managerId
WHERE manager.id IS NOT NULL # manager must exist
GROUP BY manager.id 
HAVING COUNT(Employee.id) >= 5