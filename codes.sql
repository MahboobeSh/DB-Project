--handling password and username change in user
CREATE FUNCTION check_user() RETURNS trigger AS $check_user$
    BEGIN 

        IF (TG_OP = 'UPDATE') THEN
        -- Check that password
            IF NEW.username != OLD.username THEN
                RAISE EXCEPTION 'you cannot change username';
            END IF;
        END IF;

        IF (char_length(NEW.password) >= 8 and NEW.password ~ '[A-Z]' and NEW.password ~ '[a-z]' and New.password ~ '[0-9]' ) THEN
            RETURN NEW;
        ELSE
            RAISE EXCEPTION 'password  cannot be short';
        END IF; 

    END;
$check_user$ LANGUAGE plpgsql;

CREATE TRIGGER check_user BEFORE INSERT OR UPDATE ON movie_user
    FOR EACH ROW EXECUTE FUNCTION check_user();


-- handling introducer
CREATE OR REPLACE FUNCTION handle_introducer() RETURNS trigger AS $handle_introducer$
    BEGIN 

        IF (TG_OP = 'INSERT') THEN
        -- Check that password
            IF NEW.introducer_id is not null THEN
                UPDATE movie_user
                SET points =  (SELECT points FROM movie_user WHERE user_id = NEW.introducer_id) +1 
                WHERE user_id = NEW.introducer_id;

            END IF;

        ELSEIF (TG_OP = 'UPDATE') THEN
            IF NEW.introducer_id is not null and OLD.introducer_id is NUll THEN
                UPDATE movie_user
                SET points =  (SELECT points FROM movie_user WHERE user_id = NEW.introducer_id) +1 
                WHERE user_id = NEW.introducer_id;
            ELSEIF NEW.introducer_id is not null and OLD.introducer_id is not null and NEW.introducer_id != OLD.introducer_id THEN
                RAISE EXCEPTION 'you cannot change introducer'; 
            END IF;

            
        END IF;
        RETURN NEW;

    END;
$handle_introducer$ LANGUAGE plpgsql;

CREATE TRIGGER handle_introducer BEFORE INSERT OR UPDATE ON movie_user
    FOR EACH ROW EXECUTE FUNCTION handle_introducer();


--INSERT INTO movie_user(username,first_name, last_name, email, phone_number, password, introducer_id)VALUES ("test10", "m","m","m@gmail.com","09193456","Mm0987654398765",45);

CREATE OR REPLACE FUNCTION handle_opinion() RETURNS trigger AS $handle_opinion$
    BEGIN 

        IF (TG_OP = 'INSERT') THEN
        -- Check that password
            IF (EXISTS(SELECT * FROM movie_watch WHERE user_id = NEW.user_id and movie_id = NEW.movie_id) or 
                EXISTS(SELECT * FROM movie_SepecialMovieWatch WHERE user_id = NEW.user_id and movie_id = NEW.movie_id))  THEN
                RETURN NEW;
            ELSE
                RAISE EXCEPTION 'you have to watch the film before writing an opinion'; 

            END IF;            
        END IF;
        
    END;
$handle_opinion$ LANGUAGE plpgsql;

CREATE TRIGGER handle_opinion BEFORE INSERT OR UPDATE ON movie_opinion
    FOR EACH ROW EXECUTE FUNCTION handle_opinion();



CREATE OR REPLACE FUNCTION handle_watch() RETURNS trigger AS $handle_watch$
    BEGIN 

        IF (EXISTS(SELECT * FROM movie_SepecialMovie WHERE special_movie_id = NEW.movie_id))THEN
            RAISE EXCEPTION 'it has to be inserted in special watch'; 
        ELSE

            RETURN NEW;

        END IF;            
       
        
    END;
$handle_watch$ LANGUAGE plpgsql;

CREATE TRIGGER handle_watch BEFORE INSERT ON movie_watch
    FOR EACH ROW EXECUTE FUNCTION handle_watch();