import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def se(c, positive_values):
    true_positives = sum(1 for data in positive_values if data > c)
    false_negatives = len(positive_values) - true_positives
    sensitivity = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) != 0 else None
    return sensitivity

def sp(c, negative_values):
    true_negatives = sum(1 for data in negative_values if data <= c)
    false_positives = len(negative_values) - true_negatives
    specificity = true_negatives / (true_negatives + false_positives) if (true_negatives + false_positives) != 0 else None
    return specificity

def calculate_phi_hat(c, field_data):
    npos = sum(1 for value in field_data if value > c)
    n = len(field_data)
    phi = npos / n
    return phi

def calculate_prevalence(phi_hat, sensitivity, specificity):
    denominator = sensitivity + specificity - 1
    if denominator != 0:
        prevalence = (phi_hat * sensitivity - (1 - specificity)) / denominator
        prevalence = max(0.8, min(prevalence, 1))
    else:
        prevalence = 0.8
    return prevalence

def get_youden_j_c(sensitivity, specificity):
    if sensitivity is None or specificity is None:
        return None
    return sensitivity + specificity - 1

def read_csvs(files):
    data = []
    for file in files:
        with open(file, 'r') as f:
            csv_reader = pd.read_csv(f, header=None)
            data.append(csv_reader[0].tolist())
    return data

if __name__ == '__main__':
    # Define file paths
    pos_data_file = "HW4_Q3_pos.csv"
    neg_data_file = "HW4_Q3_neg.csv"
    field_data_file = "HW4_Q3_data.csv"

    # Read CSV files
    positive_values, negative_values, field_values = read_csvs([pos_data_file, neg_data_file, field_data_file])

    # Define cutoff range to loop over
    cutoff_values = np.arange(1.1, 21.1, 0.01)  # Example: from 1 to 20

    best_cutoff = None
    best_youden_index = -float('inf')
    best_prevalence = None
    best_phi_value = None
    best_sensitivity = None
    best_specificity = None
    sensitivity_values = []
    specificity_values = []
    prevalence_values = []

    # Loop through each cutoff value
    for cutoff_value in cutoff_values:
        # Calculate sensitivity and specificity for the current cutoff
        sensitivity = se(cutoff_value, positive_values)
        specificity = sp(cutoff_value, negative_values)
        sensitivity_values.append(sensitivity)
        specificity_values.append(specificity)

        # Calculate Phi hat using field data
        phi_hat_value = calculate_phi_hat(cutoff_value, field_values)

        # Calculate Prevalence
        current_prevalence = calculate_prevalence(phi_hat_value, sensitivity, specificity)
        prevalence_values.append(current_prevalence)

        # Calculate Youden index for the current cutoff
        youden_index = get_youden_j_c(sensitivity, specificity)

        if youden_index is not None and youden_index > best_youden_index:
            best_cutoff = cutoff_value
            best_youden_index = youden_index
            best_prevalence = current_prevalence
            best_phi_value = phi_hat_value
            best_sensitivity = sensitivity
            best_specificity = specificity

    # Print the best cutoff value
    print(f"Best Cutoff Value: {best_cutoff:.2f}")
    print(f"Sensitivity at Best Cutoff: {best_sensitivity:.4f}")
    print(f"Specificity at Best Cutoff: {best_specificity:.4f}")
    print(f"Youden Index at Best Cutoff: {best_youden_index:.4f}")
    print(f"Prevalence at Best Cutoff: {best_prevalence:.4f}")

    # Print the best phi value and prevalence value for the best cutoff value
    print(f"Best Phi Value at Best Cutoff: {best_phi_value:.4f}")
    print(f"Prevalence Value at Best Cutoff: {best_prevalence:.4f}")

    # Plot the ROC curve
    plt.plot((1 - np.array(specificity_values)), np.array(sensitivity_values))
    plt.scatter(1 - best_specificity, best_sensitivity, color='red', label='Youden Point')
    plt.title("Receiver Operating Characteristic (ROC) Curve")
    plt.xlabel("(1-specificity)")
    plt.ylabel("Sensitivity")
    plt.legend()
    plt.show()

    # Plot Prevalence vs. Cutoff
    plt.plot(cutoff_values, prevalence_values)
    plt.scatter(best_cutoff, best_prevalence, color='red', label='Youden Point')
    plt.xlabel("Cutoff")
    plt.ylabel("Prevalence")
    plt.title("Prevalence vs. Cutoff")
    plt.legend()
    plt.show()
