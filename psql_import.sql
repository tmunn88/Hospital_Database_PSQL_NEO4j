/*table creation*/

CREATE TABLE doctor (
    id serial PRIMARY KEY,
    ssn varchar(12),
    first_name varchar(50),
    last_name varchar(50),
    phone_number varchar(25)
);

CREATE TABLE patient (
    id serial PRIMARY KEY,
    ssn varchar(12),
    first_name varchar(50),
    last_name varchar(50),
    phone_number varchar(25)
);

CREATE TABLE patient_doctor (
    p_id integer REFERENCES patient (id) ON
    UPDATE
        CASCADE,
        d_id integer REFERENCES doctor (id) ON
        UPDATE
            CASCADE,
            PRIMARY KEY (p_id,
                d_id)
);

CREATE TABLE illness (
    id serial PRIMARY KEY,
    ill_name varchar(50),
    ill_descrip varchar(255)
);

CREATE TABLE patient_illness (
    p_id integer REFERENCES patient (id) ON
    UPDATE
        CASCADE,
        ill_id integer REFERENCES illness (id) ON
        UPDATE
            CASCADE,
            PRIMARY KEY (p_id,
                ill_id)
);


CREATE TABLE treatment (
    id serial PRIMARY KEY,
    treat_name varchar(50),
    treat_description varchar(255)
);

CREATE TABLE patient_treatment (
    p_id integer REFERENCES patient (id) ON
    UPDATE
        CASCADE,
        treat_id integer REFERENCES treatment (id) ON
        UPDATE
            CASCADE,
            PRIMARY KEY (p_id,
                treat_id)
);

/*coping simulated data from the csv file into the sql tables*/
COPY doctor
FROM
    '/app/postgres/projects/doctor_tbl.csv' DELIMITER ',' CSV HEADER;

COPY patient
FROM
    '/app/postgres/projects/patient_tbl.csv' DELIMITER ',' CSV HEADER;

COPY patient_doctor
FROM
    '/app/postgres/projects/patient_doctor_tbl.csv' DELIMITER ',' CSV HEADER;


COPY illness
FROM
    '/app/postgres/projects/illness_tbl.csv' DELIMITER ',' CSV HEADER;

COPY patient_illness
FROM
    '/app/postgres/projects/patient_illness_tbl.csv' DELIMITER ',' CSV HEADER;

COPY treatment
FROM
    '/app/postgres/projects/treatment_tbl.csv' DELIMITER ',' CSV HEADER;


COPY patient_treatment
FROM
    '/app/postgres/projects/patient_treatment_tbl.csv' DELIMITER ',' CSV HEADER;
