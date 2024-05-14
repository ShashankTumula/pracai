def calculate_disease_likelihood(p_disease, p_symptom_x_given_disease, p_symptom_y_given_disease, p_symptom_x, p_symptom_y):
    # Calculate the joint probability of having both symptoms given Disease A
    p_both_symptoms_given_disease = p_symptom_x_given_disease * p_symptom_y_given_disease
    
    # Calculate the probability of having both symptoms in general
    p_both_symptoms = p_symptom_x * p_symptom_y
    
    # Apply Bayes' Theorem to calculate P(Disease A | Both Symptoms)
    p_disease_given_both_symptoms = (p_both_symptoms_given_disease * p_disease) / p_both_symptoms
    
    return p_disease_given_both_symptoms

# Given probabilities
p_disease = 0.01
p_symptom_x_given_disease = 0.8
p_symptom_y_given_disease = 0.7
p_symptom_x = 0.05
p_symptom_y = 0.04

# Calculate likelihood of Disease A given both symptoms are present
likelihood = calculate_disease_likelihood(p_disease, p_symptom_x_given_disease, p_symptom_y_given_disease, p_symptom_x, p_symptom_y)
print(f"The likelihood of Disease A given both Symptom X and Symptom Y are present is: {likelihood:.4f}")