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

def prevalence(phi_hat, sensitivity, specificity):
    if sensitivity is None or specificity is None:
        return None
    denominator = sensitivity + specificity - 1
    if denominator == 0: 
        return None

    return (phi_hat - (1 - specificity)) / denominator
    

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
    phi_hat = len(positive_values)/(len(positive_values)+len(negative_values))
    cutoff_values = np.arange(1.1, 21.1,0.01)  # Example: from 1 to 20

    best_cutoff = None
    best_youden_index = -float('inf')
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

        # Calculate Prevalence
        if sensitivity is not None and specificity is not None:  
            current_prevalence = prevalence(phi_hat,sensitivity,specificity)
            prevalence_values.append(current_prevalence)
        else: 
            prevalence_values.append(None)
        
        # Calculate Youden index for the current cutoff
        youden_index = get_youden_j_c(sensitivity, specificity)

        if current_prevalence is not None: 
            print(f"Cutoff: {cutoff_value:.2f}, Sensitivity: {sensitivity:.4f}, Specificity: {specificity:.4f}, Youden Index: {youden_index:.4f}, Prevalence: {current_prevalence:.4f}")
        else: 
            print(f"Cutoff: {cutoff_value:.2f}, Sensitivity: {sensitivity:.4f}, Specificity: {specificity:.4f}, Youden Index: {youden_index:.4f}, Prevalence: None")

        # Update the best cutoff based on the Youden index
        if youden_index is not None and youden_index > best_youden_index:
            best_cutoff = cutoff_value
            best_youden_index = youden_index
            best_prevalence = current_prevalence
            best_sensitivity = sensitivity
            best_specificity = specificity
    # Print the best cutoff value
    print(f"Best Cutoff Value: {best_cutoff:.2f}")
    print(f"Sensitivity at Best Cutoff: {best_sensitivity:.4f}")
    print(f"Specificity at Best Cutoff: {best_specificity:.4f}")
    print(f"Youden Index at Best Cutoff: {best_youden_index:.4f}")
    print(f"Prevalence at Best Cutoff: {best_prevalence:.4f}")

    # Plot the ROC curve
    plt.plot((1-np.array(specificity_values)),np.array(sensitivity_values))
    plt.scatter(0.04,0.9600,25)  # Assuming this scatter point is for emphasis
    plt.title("Receiver Operating Characteristic (ROC) Curve")
    plt.xlabel("(1-specificity)")
    plt.ylabel("Sensitivity")
    plt.show()

    # Plot Prevalence vs. Cutoff
    plt.plot(cutoff_values, np.array(prevalence_values))
    plt.scatter(0.04, 0.9600, 25)  # Assuming this scatter point is for emphasis
    plt.xlabel("Cutoff")
    plt.ylabel("Prevalence")
    plt.title("Prevalence vs. Cutoff")
    plt.show()
