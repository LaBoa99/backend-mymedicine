CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE MedicalRecord (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    paternal_surname VARCHAR(255) NOT NULL,
    mother_surname VARCHAR(255) NOT NULL,
    sex_assigned ENUM('M', 'F', 'O') NOT NULL,
    blood_type ENUM('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-') NOT NULL,
    birth_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE Medicine (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    formule VARCHAR(255),
    laboratory VARCHAR(255),
    alternative VARCHAR(255),
    dose_interval VARCHAR(16),
    total_doses  TINYINT UNSIGNED NOT NULL,
    current_doses  TINYINT UNSIGNED NOT NULL DEFAULT 0 -- Se guarda para evitar consultar la tabla MedicalRecord_Medicine
);

CREATE TABLE MedicalRecord_Medicine (
    medical_record_id INTEGER NOT NULL,
    medicine_id INTEGER NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (medical_record_id, medicine_id),
    FOREIGN KEY (medical_record_id) REFERENCES MedicalRecord(id),
    FOREIGN KEY (medicine_id) REFERENCES Medicine(id)
);
