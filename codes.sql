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