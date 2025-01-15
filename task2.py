-- Updating the session time for Charles Darwin
UPDATE WorkoutSessions
SET session_time = 'Evening'
WHERE member_id = (SELECT id FROM Members WHERE name = 'Charles Darwin');
