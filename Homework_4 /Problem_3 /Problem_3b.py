import pandas as pd
import numpy as np

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
    cutoff_values = np.arange(1.1, 21.1,0.1)  # Example: from 1 to 20

    best_cutoff = None
    best_youden_index = -float('inf')

    # Loop through each cutoff value
    for cutoff_value in cutoff_values:
        # Calculate sensitivity and specificity for the current cutoff
        sensitivity = se(cutoff_value, positive_values)
        specificity = sp(cutoff_value, negative_values)

        # Calculate Youden index for the current cutoff
        youden_index = get_youden_j_c(sensitivity, specificity)

        # Print results for each cutoff (optional)
        print(f"Cutoff: {cutoff_value}, Sensitivity: {sensitivity:.4f}, Specificity: {specificity:.4f}, Youden Index: {youden_index:.4f}")

        # Update the best cutoff based on the Youden index
        if youden_index is not None and youden_index > best_youden_index:
            best_cutoff = cutoff_value
            best_youden_index = youden_index

    # Print the best cutoff and its corresponding Youden index
    print(f"Best Cutoff: {best_cutoff}, Best Youden Index (J_c): {best_youden_index:.4f}")
