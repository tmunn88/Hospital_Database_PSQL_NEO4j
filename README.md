# Implementing a Hospital Database PSQL using Simulated Data

In this project I implementing a database for SmallTown Hospital, a local hypothetical hospital in my town using data generated with python.

## Schema
A Doctor has a name and sees many Patients

A Patient has a name and can have many Illnesses. A Doctor can be a Patient

An Illness has a name

A Patient can receive many Treatments

A Treatment has a name

## Guidelines

I inserted 10000 unique patients, 100 uniquedoctors, 1000 unique illnesses, and 750 unique treatments. 

Every patient is seeing 1-5 doctors, and has between 0-3 different illnesses. 

Any patients that have an illness will be receiving at least one treatment. 

Doctors have a 35% chance of being a patient themselves, in which case the patient rules apply to them.
