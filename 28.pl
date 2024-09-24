% Define diseases and their symptoms
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, sore_throat).
symptom(covid19, fever).
symptom(covid19, cough).
symptom(covid19, shortness_of_breath).
symptom(cold, runny_nose).
symptom(cold, sore_throat).
symptom(allergy, runny_nose).
symptom(allergy, sneezing).

% Define rules for diagnosis
diagnose(Disease, Symptoms) :-
symptom(Disease,Symptom).
