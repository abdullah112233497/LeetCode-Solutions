-- Write your PostgreSQL query statement below
SELECT p.lastName, p.firstName, a.city,a.state
From Person p
LEFT JOIN Address a
ON p.personId=a.personId;