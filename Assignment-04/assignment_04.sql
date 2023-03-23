# Revising the Select Query I
# https://www.hackerrank.com/challenges/revising-the-select-query/problem
# Solution:

SELECT * FROM CITY WHERE POPULATION > 100000 AND COUNTRYCODE = 'USA';

##############################################################################

# Japanese Cities' Names
# https://www.hackerrank.com/challenges/japanese-cities-name/problem
# Solution:

SELECT NAME FROM CITY WHERE COUNTRYCODE ='JPN';

##############################################################################

# Weather Observation Station 4
# https://www.hackerrank.com/challenges/weather-observation-station-4/problem
# Solution:

SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;

##############################################################################

# Average Population
# https://www.hackerrank.com/challenges/average-population/problem
# Solution:

SELECT FLOOR(AVG(POPULATION)) FROM CITY;

##############################################################################

# Weather Observation Station 8
# https://www.hackerrank.com/challenges/weather-observation-station-8/problem
# Solution:

SELECT DISTINCT CITY FROM STATION
WHERE (CITY LIKE "[AEIOUaeiou]%") AND (CITY LIKE "%[AEIOUaeiou]");

##############################################################################

# Weather Observation Station 9
# https://www.hackerrank.com/challenges/weather-observation-station-9/problem
# Solution:

SELECT DISTINCT city FROM STATION
WHERE NOT (CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' OR CITY LIKE 'U%');

##############################################################################

# Employee Salaries
# https://www.hackerrank.com/challenges/salary-of-employees/problem
# Solution:

SELECT name FROM employee
WHERE salary > 2000 AND months < 10
ORDER BY employee_id;

##############################################################################

# Top Earners
# https://www.hackerrank.com/challenges/earnings-of-employees/problem
# Solution:

SELECT MAX(months * salary), COUNT(months * salary) FROM Employee
WHERE (months * salary) = (SELECT MAX(months * salary) FROM Employee);

##############################################################################

# Duplicate Emails
# https://leetcode.com/problems/duplicate-emails
# Solution:

SELECT email FROM Person
GROUP BY email
HAVING COUNT(*) > 1;

##############################################################################

# Second Highest Salary
# https://leetcode.com/problems/second-highest-salary
# Solution:

SELECT MAX(salary) AS SecondHighestSalary FROM Employee
WHERE salary NOT IN (SELECT MAX(salary) FROM Employee);

##############################################################################

# Rising Temperature
# https://leetcode.com/problems/rising-temperature
# Solution:

SELECT w2.id FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = -1
WHERE w2.temperature > w1.temperature;

##############################################################################

# Not Boring Movies
# https://leetcode.com/problems/not-boring-movies
# Solution:

SELECT * FROM Cinema
WHERE id % 2 = 1 AND description != "boring"
ORDER BY rating DESC;

##############################################################################

# Sales Person
# https://leetcode.com/problems/sales-person
# Solution:

SELECT s.name FROM SalesPerson s
WHERE s.name NOT IN (SELECT s.name FROM Orders o
                    INNER JOIN Company c ON c.com_id = o.com_id
                    LEFT JOIN SalesPerson s ON s.sales_id = o.sales_id
                    WHERE c.name = "RED");

##############################################################################

# Game Play Analysis I
# https://leetcode.com/problems/game-play-analysis-i
# Solution:

SELECT player_id, MIN(event_date) AS first_login FROM Activity
GROUP BY player_id;