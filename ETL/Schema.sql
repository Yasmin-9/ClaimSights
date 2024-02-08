-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/Ru5SGs

CREATE TABLE "claim" (
    "Patient" double   NOT NULL,
    "Age" Int   NOT NULL,
    "Age_Group" str   NOT NULL,
    "Sex" str   NOT NULL,
    "Diagnosis_Code" str   NOT NULL,
    "Diagnosis_Group" str   NOT NULL,
    "Diagnosis_Family" str   NOT NULL,
    "Diagnosis_Description" str   NOT NULL,
    "Med_Code" double   NOT NULL,
    "Med_Description" str   NOT NULL,
    "Med_Description_Simp" str   NOT NULL,
    "Quantity" int   NOT NULL,
    "Status" str   NOT NULL,
    "Amount_Billed" float   NOT NULL,
    "Amount_Paid" float   NOT NULL,
    CONSTRAINT "pk_claim" PRIMARY KEY (
        "Patient"
     )
);

