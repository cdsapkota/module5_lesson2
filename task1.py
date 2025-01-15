-- Inserting records into Members table
INSERT INTO Members (id, name, age) VALUES 
(1, 'Charles Darwin', 45),
(2, 'Albert Einstein', 50),
(3, 'Nikola Tesla', 40);

-- Inserting records into WorkoutSessions table
INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES
(101, 1, '2025-01-10', 'Morning', 'Yoga'),
(102, 2, '2025-01-11', 'Afternoon', 'Weightlifting'),
(103, 3, '2025-01-12', 'Evening', 'Cardio');
