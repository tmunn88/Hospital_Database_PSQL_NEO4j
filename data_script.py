# Name: Tiffany J Munn, Project: Project2-Data Generation Portion

import csv
import pandas as pd
import random
from random import shuffle, seed
from faker import Faker
fake = Faker()


# # Creating Doctor Data
doctors_id_list = [x for x in range(1, 101)]
doctors_dict = {"id": doctors_id_list,
                "ssn": [],
                "first_name": [],
                "last_name": [],
                "phone_number": [],
                }

num_docs = 100

fake.random.seed(4321)

# this ssn sample with be used for doctors and patients but uniquely so
social_sample = []
while len(social_sample) < 10065:
    social = fake.ssn()
    if social not in social_sample:
        # to prevent duplicates
        social_sample.append(social)

# insert doctor's data into the dictionary
for x in range(num_docs):
    doctors_dict["first_name"].append(fake.first_name())
    doctors_dict["last_name"].append(fake.last_name())
    doctors_dict["phone_number"].append(fake.phone_number())

doctors_dict["ssn"] = social_sample[0:100]
# creates a quick table format of data
doctor_tbl = pd.DataFrame(doctors_dict)

# exports data to csv file; import to psql through COPY command
doctors = doctor_tbl.to_csv(
    r'C:\Users\Tiff\Desktop\nosql-db\projects\doctor_tbl.csv', index=None, header=True)


# Creating Patient Data
# take a random sample of 35% of doctors; make them patients

pts_also_docs = doctor_tbl.sample(frac=0.35)
pts_also_docs.drop(['id'], axis=1, inplace=True)

# create the other 9965 patients

# # patient dictionaries
pt_doc_ids = [x for x in range(1, 36)]
pt_ids = [x for x in range(36, 10001)]

pts_also_docs_dict = {"id": pt_doc_ids,
                      "ssn": pts_also_docs["ssn"],
                      "first_name": pts_also_docs["first_name"],
                      "last_name": pts_also_docs["last_name"],
                      "phone_number": pts_also_docs["phone_number"],
                      }

pts_also_docs_df = pd.DataFrame(pts_also_docs_dict)

pts_dict = {"id": pt_ids,
            "ssn": [],
            "first_name": [],
            "last_name": [],
            "phone_number": [],
            }

pts_not_docs = 9965

# # insert patient's data into the dictionary
for x in range(pts_not_docs):
    pts_dict["first_name"].append(fake.first_name())
    pts_dict["last_name"].append(fake.last_name())
    pts_dict["phone_number"].append(fake.phone_number())


pts_dict["ssn"] = social_sample[100:10065]

# # makes data readable in 'table' format
pts_not_docs_df = pd.DataFrame(pts_dict)

# append the two dataframes
patient_tbl = pts_also_docs_df.append(pts_not_docs_df, ignore_index=True)

# exports data to csv file; import to psql through COPY command
patient = patient_tbl.to_csv(
    r'C:\Users\Tiff\Desktop\nosql-db\projects\patient_tbl.csv', index=None, header=True)


# Creating data for patient_doctors lookup table

# lists displayed here for sampling references
doctors_id_sample = [x for x in range(1, 101)]
patient_id_sample = [x for x in range(1, 10001)]

patient_id_vector = []
doc_id_vector = []

patient_doctors_dict = {
    "p_id": [],
    "d_id": [],
}

doc_num1 = 1
doc_num2 = 2
doc_num3 = 3
doc_num4 = 4
doc_num5 = 5


onedoc_samp = random.sample(patient_id_sample, k=6900)
for patient in onedoc_samp:
    patient_id_vector.append(patient)
    doc_id_elem = random.sample(doctors_id_sample, k=1)
    doc_id_vector.extend(doc_id_elem)
# remove patients already given a doc from sample
for patient in onedoc_samp:
    patient_id_sample.remove(patient)


twodoc_samp = random.sample(patient_id_sample, k=1500)
for patient in twodoc_samp:
    patient_id_vector.extend(doc_num2*[patient])
    doc_id_elem = random.sample(doctors_id_sample, k=2)
    doc_id_vector.extend(doc_id_elem)
# remove patients already given a doc from sample
for patient in twodoc_samp:
    patient_id_sample.remove(patient)


threedoc_samp = random.sample(patient_id_sample, k=1000)
for patient in threedoc_samp:
    patient_id_vector.extend(doc_num3*[patient])
    doc_id_elem = random.sample(doctors_id_sample, k=3)
    doc_id_vector.extend(doc_id_elem)
# remove patients already given a doc from sample
for patient in threedoc_samp:
    patient_id_sample.remove(patient)


fourdoc_samp = random.sample(patient_id_sample, k=500)
for patient in fourdoc_samp:
    patient_id_vector.extend(doc_num4*[patient])
    doc_id_elem = random.sample(doctors_id_sample, k=4)
    doc_id_vector.extend(doc_id_elem)
# remove patients already given a doc from sample
for patient in fourdoc_samp:
    patient_id_sample.remove(patient)

fivedoc_samp = random.sample(patient_id_sample, k=100)
for patient in fivedoc_samp:
    patient_id_vector.extend(doc_num5*[patient])
    doc_id_elem = random.sample(doctors_id_sample, k=5)
    doc_id_vector.extend(doc_id_elem)
# remove patients already given a doc from sample
for patient in fivedoc_samp:
    patient_id_sample.remove(patient)


patient_doctors_dict["p_id"] = patient_id_vector
patient_doctors_dict["d_id"] = doc_id_vector
patient_doctor_tbl = pd.DataFrame(patient_doctors_dict)


# exports data to csv file; import to psql through COPY command
patient_doctor = patient_doctor_tbl.to_csv(
    r'C:\Users\Tiff\Desktop\nosql-db\projects\patient_doctor_tbl.csv', index=None, header=True)

# # Creating Illness Data
illness_id_list = [x for x in range(1, 1001)]
illness_dict = {"id": illness_id_list,
                "ill_name": [],
                "ill_descrip": [],
                }


num_ills = 1000

illness_words = ['infection', 'disease', 'condition', 'syndrome', 'virus', 'illness']

fake.random.seed(4321)
ill_sample = []
while len(ill_sample) < num_ills:
    illness_word1 = fake.last_name()
    illness_word2 = random.choice(illness_words)
    illness = illness_word1 + ' ' + illness_word2
    if illness not in ill_sample:
        # to ensure uniqueness
        ill_sample.append(illness)


for x in range(num_ills):
    illness_dict["ill_descrip"].append(fake.sentence())

illness_dict["ill_name"] = ill_sample

# creates a quick table format of data
illness_tbl = pd.DataFrame(illness_dict)

# exports data to csv file; import to psql through COPY command
illness = illness_tbl.to_csv(
    r'C:\Users\Tiff\Desktop\nosql-db\projects\illness_tbl.csv', index=None, header=True)

# # # Creation of Patient_illness Table

# lists displayed here for sampling references
illness_id_sample = [x for x in range(1, 1001)]
patient_id_sample = [x for x in range(1, 10001)]

patient_id_vector = []
ill_id_vector = []

patients_illnesses_dict = {
    "p_id": [],
    "ill_id": [],
}

ill_num1 = 1
ill_num2 = 2
ill_num3 = 3


oneill_samp = random.sample(patient_id_sample, k=6000)
for patient in oneill_samp:
    patient_id_vector.append(patient)
    ill_id_elem = random.sample(illness_id_sample, k=1)
    ill_id_vector.extend(ill_id_elem)
# remove patients already given a doc from sample
for patient in oneill_samp:
    patient_id_sample.remove(patient)


twoill_samp = random.sample(patient_id_sample, k=2000)
for patient in twoill_samp:
    patient_id_vector.extend(ill_num2*[patient])
    ill_id_elem = random.sample(illness_id_sample, k=2)
    ill_id_vector.extend(ill_id_elem)
# remove patients already given a doc from sample
for patient in twoill_samp:
    patient_id_sample.remove(patient)

threeill_samp = random.sample(patient_id_sample, k=1000)
for patient in threeill_samp:
    patient_id_vector.extend(ill_num3*[patient])
    ill_id_elem = random.sample(illness_id_sample, k=3)
    ill_id_vector.extend(ill_id_elem)
# remove patients already given a doc from sample
for patient in threeill_samp:
    patient_id_sample.remove(patient)


patients_illnesses_dict["p_id"] = patient_id_vector
patients_illnesses_dict["ill_id"] = ill_id_vector
patient_illness_tbl = pd.DataFrame(patients_illnesses_dict)


# exports data to csv file
patient_illness = patient_illness_tbl.to_csv(
    r'C:\Users\Tiff\Desktop\nosql-db\projects\patient_illness_tbl.csv', index=None, header=True)


############################### Treatments and patient treatment table #########################

# # Creating Treatment Data
treat_id_list = [x for x in range(1, 751)]
treat_dict = {"id": treat_id_list,
              "treat_name": [],
              "treat_descrip": [],
              }

num_treats = 750


treat_words = ['treatment', 'cure', 'medicine', 'surgery', 'operation', 'prescription']

fake.random.seed(4321)
treat_sample = []
while len(treat_sample) < num_treats:
    treat_word1 = fake.last_name()
    treat_word2 = random.choice(treat_words)
    treatment = treat_word1 + ' ' + treat_word2
    if treatment not in treat_sample:
        # to ensure uniqueness
        treat_sample.append(treatment)

treat_dict["treat_name"] = treat_sample

for x in range(num_treats):
    treat_dict["treat_descrip"].append(fake.sentence())
# creates a quick table format of data
treatment_tbl = pd.DataFrame(treat_dict)


# exports data to csv file; import to psql through COPY command
treatment = treatment_tbl.to_csv(
    r'C:\Users\Tiff\Desktop\nosql-db\projects\treatment_tbl.csv', index=None, header=True)


# # # Creation of Patient_Treatment Table

# lists displayed here for sampling references
treat_id_sample = [x for x in range(1, 751)]
# only sampling patients that already have an illness
patient_id_sample = (list(set(patients_illnesses_dict["p_id"])))

patient_id_vector = []
treat_id_vector = []

patient_treatment_dict = {
    "p_id": [],
    "treat_id": [],
}

treat_num1 = 1
treat_num2 = 2
treat_num3 = 3

onetreat_samp = random.sample(patient_id_sample, k=6300)
for patient in onetreat_samp:
    patient_id_vector.append(patient)
    treat_id_elem = random.sample(treat_id_sample, k=1)
    treat_id_vector.extend(treat_id_elem)
# remove patients already given a doc from sample
for patient in onetreat_samp:
    patient_id_sample.remove(patient)


twotreat_samp = random.sample(patient_id_sample, k=1800)
for patient in twotreat_samp:
    patient_id_vector.extend(treat_num2*[patient])
    treat_id_elem = random.sample(treat_id_sample, k=2)
    treat_id_vector.extend(treat_id_elem)
# remove patients already given a doc from sample
for patient in twotreat_samp:
    patient_id_sample.remove(patient)

threetreat_samp = random.sample(patient_id_sample, k=900)
for patient in threetreat_samp:
    patient_id_vector.extend(treat_num3*[patient])
    treat_id_elem = random.sample(treat_id_sample, k=3)
    treat_id_vector.extend(treat_id_elem)
# remove patients already given a doc from sample
for patient in threetreat_samp:
    patient_id_sample.remove(patient)


patient_treatment_dict["p_id"] = patient_id_vector
patient_treatment_dict["treat_id"] = treat_id_vector
patient_treatment_tbl = pd.DataFrame(patient_treatment_dict)

# exports data to csv file
patient_treatment = patient_treatment_tbl.to_csv(
    r'C:\Users\Tiff\Desktop\nosql-db\projects\patient_treatment_tbl.csv', index=None, header=True)
