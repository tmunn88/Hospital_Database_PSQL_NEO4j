/* 1. How many doctors are treating doctors? */
SELECT
    Count(d.id) as doctors_treating_doctors
FROM
    patient p,
    patient_doctor pd,
    doctor d
WHERE
    /* ensures that the patient is actually a doctor */
    p.ssn IN (
        SELECT
            doctor.ssn
        FROM
            doctor)
        and
        /* connects the ids of the doctors for those patients */
        p.id = pd.p_id
        and pd.d_id = d.id;

/* Output
 doctors_treating_doctors
--------------------------
                       57
(1 row)*/
/* 2. What's the count of how many patients have each kind of illness? */
SELECT
    i.ill_name,
    Count(pi.p_id) as patient_count
FROM
    patient_illness as pi,
    illness as i
WHERE
    pi.ill_id = i.id
GROUP BY
    i.ill_name
ORDER BY
    patient_count DESC;

/* Output--only showing some records for space
       ill_name       | patient_count
----------------------+---------------
 Maxwell condition    |            26
 Crosby virus         |            26
 Lee virus            |            24
 Horton illness       |            24
 Nelson virus         |            23
 Lamb illness         |            22
 Green condition      |            21
 Garcia syndrome      |            21
 Vaughan syndrome     |            21
 Hamilton illness     |            21
 Jackson virus        |            21
 Shaffer syndrome     |            21
 Kent syndrome        |            21
 Russo infection      |            21
 Moreno virus         |            21
 ----------------------+---------------*/
/* 3. What's the doctor with the most patients? */

WITH MaxGroup AS (
    SELECT
        pd.d_id,
        COUNT(pd.p_id) AS patient_count
    FROM
        patient_doctor pd
    GROUP BY
        pd.d_id
)
SELECT
    d.ssn,
    d.last_name, patient_count
FROM
    MaxGroup, doctor as d
WHERE
    MaxGroup.d_id = d.id
    and patient_count = (
        SELECT
            MAX(patient_count)
        FROM
            MaxGroup);

/*output
ssn     | last_name | patient_count
-------------+-----------+---------------
235-27-5347 | Boyd      |           178
(1 row) */

/* 4. Which doctor is treating the largest number of unique illnesses ? */

WITH MaxIll AS (
    SELECT
        pd.d_id,
        COUNT(DISTINCT(pi.p_id)) AS illness_count
    FROM
        patient_illness pi,
        patient_doctor pd
    WHERE
        pd.p_id=pi.p_id
    GROUP BY
        pd.d_id
)
SELECT
    d.ssn,
    d.last_name, illness_count
FROM
    MaxIll, doctor as d
WHERE
    MaxIll.d_id = d.id
    and illness_count = (
        SELECT
            MAX(illness_count)
        FROM
            MaxIll);

/* Output
     ssn     | last_name | illness_count
-------------+-----------+---------------
 775-35-1141 | Sullivan  |           163
 657-48-2940 | Contreras |           163
(2 rows)  */

/* 5. What illness is being treated with the largest number of unique treatments? */


WITH MaxIllTreat AS (
    SELECT
        pi.ill_id, Count(DISTINCT(pt.treat_id)) as treat_count
    FROM
        patient_treatment pt,
        patient_illness pi
    WHERE
        pt.p_id=pi.p_id
    GROUP BY
        pi.ill_id
)
SELECT
    i.id,i.ill_name, treat_count
FROM
    MaxIllTreat, illness as i
WHERE
    MaxIllTreat.ill_id = i.id
    and treat_count = (
        SELECT
            MAX(treat_count)
        FROM
            MaxIllTreat);


/* Output
id  |   ill_name   | treat_count
-----+--------------+-------------
439 | Nelson virus |          36
(1 row)*/
