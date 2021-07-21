DROP TRIGGER check_user ON movie_user;
DROP FUNCTION check_user;

DROP TRIGGER handle_introducer ON movie_user;
DROP FUNCTION handle_introducer;


DROP TRIGGER handle_opinion ON movie_opinion;
DROP FUNCTION handle_opinion;


EXISTS(SELECT * FROM movie_user WHERE user_id = 2)