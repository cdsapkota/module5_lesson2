-- Deleting Albert Einstein's workout sessions (due to foreign key constraint)
DELETE FROM WorkoutSessions
WHERE member_id = (SELECT id FROM Members WHERE name = 'Albert Einstein');

-- Deleting Albert Einstein's record from the Members table
DELETE FROM Members
WHERE name = 'Albert Einstein';
