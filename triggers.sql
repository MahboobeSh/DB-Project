
CREATE TRIGGER check_user BEFORE INSERT OR UPDATE ON movie_user
    FOR EACH ROW EXECUTE FUNCTION check_user();

CREATE TRIGGER handle_introducer BEFORE INSERT OR UPDATE ON movie_user
    FOR EACH ROW EXECUTE FUNCTION handle_introducer();

CREATE TRIGGER handle_opinion BEFORE INSERT OR UPDATE ON movie_opinion
    FOR EACH ROW EXECUTE FUNCTION handle_opinion();


CREATE TRIGGER handle_watch BEFORE INSERT ON movie_watch
    FOR EACH ROW EXECUTE FUNCTION handle_watch();


CREATE TRIGGER handle_prouser BEFORE INSERT OR UPDATE ON movie_prouser
    FOR EACH ROW EXECUTE FUNCTION handle_prouser();


CREATE TRIGGER handle_smwatch BEFORE INSERT OR UPDATE ON movie_SpecialMovieWatch
    FOR EACH ROW EXECUTE FUNCTION handle_smwatch();