
//After building an composing the docker container
docker exec -it nosql-neo4j /bin/bash

// Copying exported data for nodes from projects to neo4j import inside docker container

///Everything has been copied---run imports
cp /app/neo4j/projects/doctor_tbl.csv /var/lib/neo4j/import/doctor_tbl.csv
cp /app/neo4j/projects/patient_tbl.csv /var/lib/neo4j/import/patient_tbl.csv
cp /app/neo4j/projects/patient_doctor_tbl.csv /var/lib/neo4j/import/patient_doctor_tbl.csv

cp /app/neo4j/projects/illness_tbl.csv /var/lib/neo4j/import/illness_tbl.csv
cp /app/neo4j/projects/patient_illness_tbl.csv /var/lib/neo4j/import/patient_illness_tbl.csv

cp /app/neo4j/projects/treatment_tbl.csv /var/lib/neo4j/import/treatment_tbl.csv
cp /app/neo4j/projects/patient_treatment_tbl.csv /var/lib/neo4j/import/patient_treatment_tbl.csv


//Opening Cypher command line shell
/var/lib/neo4j/bin/cypher-shell

//Import the doctor nodes
CREATE CONSTRAINT ON (doctor:Doctor) ASSERT doctor.id IS UNIQUE;
CREATE CONSTRAINT ON (doctor:Doctor) ASSERT doctor.ssn IS UNIQUE;

LOAD CSV WITH HEADERS FROM "file:///doctor_tbl.csv" AS csvLine
CREATE (d:Doctor {id: toInteger(csvLine.id), ssn: csvLine.ssn, first_name: csvLine.first_name, last_name: csvLine.last_name, phone_number: csvLine.phone_number});


//Import the patient nodes

CREATE CONSTRAINT ON (patient:Patient) ASSERT patient.id IS UNIQUE;
CREATE CONSTRAINT ON (patient:Patient) ASSERT patient.ssn IS UNIQUE;

LOAD CSV WITH HEADERS FROM "file:///patient_tbl.csv" AS csvLine
CREATE (p:Patient {id: toInteger(csvLine.id), ssn: csvLine.ssn, first_name: csvLine.first_name, last_name: csvLine.last_name, phone_number: csvLine.phone_number});


///Import the doctor-patient relationship

LOAD CSV WITH HEADERS FROM "file:///patient_doctor_tbl.csv" AS csvLine
MATCH (d:Doctor {id: toInteger(csvLine.d_id)}),(p:Patient {id: toInteger(csvLine.p_id)})
CREATE (d)-[:Treats]->(p);


//Import the illness nodes
CREATE CONSTRAINT ON (illness:Illness) ASSERT illness.id IS UNIQUE;

LOAD CSV WITH HEADERS FROM "file:///illness_tbl.csv" AS csvLine
CREATE (i:Illness {id: toInteger(csvLine.id), name: csvLine.ill_name, description: csvLine.ill_descrip});


//Import the patient-illness relationship
LOAD CSV WITH HEADERS FROM "file:///patient_illness_tbl.csv" AS csvLine
MATCH (p:Patient {id: toInteger(csvLine.p_id)}), (i:Illness {id: toInteger(csvLine.ill_id)})
CREATE (p)-[:Sick_with]->(i);


//Import the treatment nodes
CREATE CONSTRAINT ON (treatment:Treatment) ASSERT treatment.id IS UNIQUE;

LOAD CSV WITH HEADERS FROM "file:///treatment_tbl.csv" AS csvLine
CREATE (t:Treatment {id: toInteger(csvLine.id), name: csvLine.treat_name, description: csvLine.treat_descrip});


//Import the patient-treatment relationship
LOAD CSV WITH HEADERS FROM "file:///patient_treatment_tbl.csv" AS csvLine
MATCH (p:Patient {id: toInteger(csvLine.p_id)}), (t:Treatment {id: toInteger(csvLine.treat_id)})
CREATE (p)-[:Receives]->(t);


//Drop constraints on id( no ssn) and then drop the ids themselves from nodes
DROP CONSTRAINT ON (doctor:Doctor) ASSERT doctor.id IS UNIQUE;
DROP CONSTRAINT ON (patient:Patient) ASSERT patient.id IS UNIQUE;
DROP CONSTRAINT ON (illness:Illness) ASSERT illness.id IS UNIQUE;
DROP CONSTRAINT ON (treatment:Treatment) ASSERT treatment.id IS UNIQUE;

MATCH (n)
WHERE n:Doctor OR n:Patient OR n.Illness or n.Treatment
REMOVE n.id;
