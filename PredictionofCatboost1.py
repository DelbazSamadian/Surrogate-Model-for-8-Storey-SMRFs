# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:00:15 2023

@author: User
"""
# from catboost import CatBoostRegressor

# # Load the trained CatBoost model
# model_path = r"F:\ML\2-Story\Final Results\final_for_paper\MIDR\Codes\CATBoost.cbm"
# catboost_best_model = CatBoostRegressor()
# catboost_best_model.load_model(model_path)

# # Assuming new_data is a DataFrame with your new input values
# import pandas as pd
# new_data = pd.DataFrame({
#     'Sa(g)': [-0.280156544],
#     'T1': [1.422703688],
#     'CAV': [0.252374225],
#     'D95_D5': [0.649791238],
#     'IA': [-0.006281968],
#     'Omega': [-0.420189648],
#     'Lbay': [1.459282525],
#     'Fy': [1.564368979],
#     'Es': [-0.242232265],
#     'ϴp_Beam2': [-0.999145972]
# })

# # Make predictions on the new input data
# predictions = catboost_best_model.predict(new_data)
# # Print the predictions
# print("Predicted Class Labels:", predictions)
#%%
# from catboost import CatBoostRegressor

# # Load the trained CatBoost model
# model_path = r"F:\ML\2-Story\Final Results\final_for_paper\MIDR\Codes\CATBoost.cbm"
# catboost_best_model = CatBoostRegressor()
# catboost_best_model.load_model(model_path)
# import pandas as pd
# import numpy as np

# # Load mean and std values from the Excel file
# mean_std_file_path = r"F:\ML\2-Story\Final Results\final_for_paper\MIDR\Codes\mean_std_values.csv"  # Replace with the actual path
# mean_std_values = pd.read_csv(mean_std_file_path)

# # Assuming new_data_non_standardized is a DataFrame with your new non-standardized input values
# new_data_non_standardized = pd.DataFrame({
#     'Sa(g)': [0.3152],
#     'T1': [1.209562202],
#     'CAV': [1.56735603],
#     'D95_D5': [0.7208126],
#     'IA': [1.555846206],
#     'Omega': [1.413165137],
#     'Lbay': [388.07],
#     'Fy': [64.78],
#     'Es': [42005.71],
#     'ϴp_Beam2': [0.027706332]
# })

# # Set the parameter names as the index for mean_std_values DataFrame
# mean_std_values = mean_std_values.set_index('Parameter')

# # Extract mean and std values for each parameter
# means = mean_std_values['mean'].to_dict()
# stds = mean_std_values['std'].to_dict()

# # Standardize the new input data using the mean and std values
# new_data_standardized = (new_data_non_standardized - means) / stds

# # Make predictions on the standardized input data
# predictions_standardized = catboost_best_model.predict(new_data_standardized)
# # Print the predictions
# print("Predicted Class Labels:", predictions_standardized)
#%%
# import tkinter as tk
# from tkinter import ttk
# from catboost import CatBoostRegressor
# import pandas as pd

# class CatBoostPredictorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("CatBoost Predictor")

#         # Load the trained CatBoost model
#         model_path = "F:/ML/2-Story/Final Results/final_for_paper/MIDR/Codes/CATBoost.cbm"
#         self.catboost_best_model = CatBoostRegressor()
#         self.catboost_best_model.load_model(model_path)

#         # Load mean and std values from the Excel file
#         mean_std_file_path = "F:/ML/2-Story/Final Results/final_for_paper/MIDR/Codes/mean_std_values.csv"
#         self.mean_std_values = pd.read_csv(mean_std_file_path)
#         self.mean_std_values = self.mean_std_values.set_index('Parameter')

#         # Create GUI elements
#         self.create_widgets()

#     def create_widgets(self):
#         # Create labels and entry widgets for each parameter
#         parameter_labels = ['Sa(g)', 'T1', 'CAV', 'D95_D5', 'IA', 'Omega', 'Lbay', 'Fy', 'Es', 'ϴp_Beam2']
#         self.entries = {}
#         for i, label in enumerate(parameter_labels):
#             ttk.Label(self.root, text=label).grid(row=i, column=0, padx=5, pady=5)
#             entry = ttk.Entry(self.root)
#             entry.grid(row=i, column=1, padx=5, pady=5)
#             self.entries[label] = entry

#         # Create a button for making predictions
#         ttk.Button(self.root, text="Predict", command=self.predict).grid(row=len(parameter_labels), column=0, columnspan=2, pady=10)

#     def predict(self):
#         # Get user input from entry widgets
#         user_input = {label: float(entry.get()) for label, entry in self.entries.items()}

#         # Standardize the user input using the mean and std values
#         user_input_standardized = (pd.DataFrame(user_input, index=[0]) - self.mean_std_values['mean']) / self.mean_std_values['std']

#         # Make predictions on the standardized input data
#         prediction = self.catboost_best_model.predict(user_input_standardized)

#         # Display the prediction (you can update this part based on your GUI design)
#         result_label = ttk.Label(self.root, text=f"Predicted Class Labels: {prediction}")
#         result_label.grid(row=len(self.entries) + 1, column=0, columnspan=2, pady=10)


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CatBoostPredictorApp(root)
#     root.mainloop()
#%%
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from catboost import CatBoostRegressor

# Load the trained CatBoost model
model_path = "F:/ML/8-Story/Final Results/final_for_paper/MIDR/Codes/CATBoost1.cbm"
catboost_best_model = CatBoostRegressor()
catboost_best_model.load_model(model_path)

# Load mean and standard deviation values
mean_std_file_path = "F:/ML/8-Story/Final Results/final_for_paper/MIDR/Codes/mean_std_values1.csv"
mean_std_values = pd.read_csv(mean_std_file_path, index_col=0)

# Function to make predictions based on user input
def predict_output():
    try:
        # Get user input for the 10 features
        user_input = {
            'Sa': pd.to_numeric(entry_widgets['Sa'].get(), errors='coerce'),
            'D95-5': pd.to_numeric(entry_widgets['D95-5'].get(), errors='coerce'),
            'CAV': pd.to_numeric(entry_widgets['CAV'].get(), errors='coerce'),
            'T1': pd.to_numeric(entry_widgets['T1'].get(), errors='coerce'),
            'Ia': pd.to_numeric(entry_widgets['Ia'].get(), errors='coerce'),
            'MP3': pd.to_numeric(entry_widgets['MP3'].get(), errors='coerce'),
            'asRatio_Beam7': pd.to_numeric(entry_widgets['asRatio_Beam7'].get(), errors='coerce'),
            'asRatio_Beam3': pd.to_numeric(entry_widgets['asRatio_Beam3'].get(), errors='coerce'),
            'MP1': pd.to_numeric(entry_widgets['MP1'].get(), errors='coerce'),
            'asRatio_Beam5': pd.to_numeric(entry_widgets['asRatio_Beam5'].get(), errors='coerce'),
            
        }

        # Convert the user input into a DataFrame
        user_input_df = pd.DataFrame([user_input])

        # Check for NaN values in the DataFrame
        if user_input_df.isna().any().any():
            problematic_features = user_input_df.columns[user_input_df.isna().any()].tolist()
            raise ValueError(f"Input contains non-numeric values in features: {problematic_features}")

        # Standardize the user input using the loaded mean and standard deviation values
        user_input_std = (user_input_df - mean_std_values['mean']) / mean_std_values['std']
        # Standardize the user input using the loaded mean and standard deviation values
        #user_input_std = user_input_df 


        # Use the trained CatBoost model to make predictions on the standardized input
        predicted_output = catboost_best_model.predict(user_input_std.values)

        # Display the predicted output
        result_label.config(text=f'Predicted Output: {predicted_output[0]:.6f}', fg='blue', font=('Times New Roman', 16, 'italic'))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("CatBoost Predictor")

# Create a frame for the title box
title_frame_outer = tk.Frame(app, bg='lightgrey', pady=10)
title_frame_outer.grid(row=0, column=0, columnspan=3)  # Adjust columnspan based on the number of columns in your layout

# Create a title box at the top middle of the app with a border
title_frame = tk.Frame(title_frame_outer, bg='lime', bd=2, relief=tk.GROOVE)
title_frame.grid(row=0, column=1, padx=10, pady=5, sticky="n")  # Adjust column and row based on your layout

title_label = tk.Label(title_frame, text="Surrogate Model for Prediction of MIDR for 8-Story SMRF", font=('Times New Roman', 20, 'italic'), fg='black', bg='lime')  # Set font to Times New Roman, size to 16, and style to italic
title_label.pack()
# Create and place input labels, entry widgets, and description boxes
input_labels = ['Sa', 'D95-5','CAV','T1',  'Ia', 'MP3', 'asRatio_Beam7','asRatio_Beam3', 'MP1','asRatio_Beam5'  ]
descriptions = [
    "Acceleration response spectrum(g)",
    "Ratio of response spectrum at 95% and 5% damping(sec)",
    "Cumulative absolute velocity(m/s)",
    "Period of the structure(sec)",
    "Arias Intensity(m/s2)",
    "Third mode mass participation",
    "Ratio of elastic stiffness to the pre-peak stiffness at Beam7",
    "Ratio of elastic stiffness to the pre-peak stiffness at Beam3",
    "First mode mass participation",
    "Ratio of elastic stiffness to the pre-peak stiffness at Beam5",
    
]

acceptable_ranges = [
    "(0.00 - 0.45)",
    "(0.01 - 3.0)",
    "(0.01 - 3.0)",   
    "(1.50 - 3.50)",
    "(0.01 - 6.0)",
    "(86.00 - 98.00)",
    "(0.01 - 0.06)",
    "(0.01 - 0.06)",
    "(40 - 90)",
    "(60.00 - 90.00)",
    
]

# Create a label for developer information
developer_label = tk.Label(app, text="Developed by Samadian, D., Muhit, I.B., Occhipinti, A., Dawood, N.(2023) SCED, Teesside University, Tees Valley, U.K.", font=('Times New Roman', 12), fg='black', bg='lightgrey')
developer_label.grid(row=len(input_labels) + 4, column=0, columnspan=3, sticky="w")  # Adjust row number and columnspan based on the number of columns in your layout, and use sticky to set alignment

#
# Set the size of the main window
app.geometry("700x1500")


# Declare entry widgets for user input globally
entry_widgets = {}
for i, label in enumerate(input_labels):
    # Create a frame for the label with a border
    frame_label = tk.Frame(app, bd=2, relief=tk.GROOVE, bg='red')
    frame_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
    tk.Label(frame_label, text=label + ":", bg='bisque', fg='black', font=('Times New Roman', 14, )).pack()

    # Create a frame for the entry widget with a border
    frame = tk.Frame(app, bd=2, relief=tk.GROOVE, bg='bisque')
    frame.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")
    entry_widgets[label] = ttk.Entry(frame, width=10, justify='center', font=('Times New Roman', 14,))
    entry_widgets[label].pack()

    # Create a frame for the description and acceptable range with a box around it
    frame = tk.Frame(app, bd=2, relief=tk.GROOVE, padx=5, pady=5, bg='lightsteelblue')
    frame.grid(row=i+1, column=2, padx=10, pady=5, sticky="w")
    tk.Label(frame, text=f"{descriptions[i]}\nAcceptable range: {acceptable_ranges[i]}", justify='left', fg='black', bg='azure', font=('Times New Roman', 14, )).pack()
# Create the Predict button with a colored border
predict_button = tk.Button(app, text="Predict", command=predict_output, bg='green', fg='white', font=('Times New Roman', 16, ), bd=2, relief=tk.GROOVE, highlightbackground='blue')
predict_button.grid(row=len(input_labels) + 2, column=0, columnspan=2, pady=10)  # Adjust row number based on the placement of the developer information label

# Create a label for displaying the predicted output
result_label = tk.Label(app, text="", bg='cornflowerblue', fg='black', font=('Times New Roman', 16,))
result_label.grid(row=len(input_labels) + 3, column=0, columnspan=3, pady=10)  # Adjust row number based on the placement of the developer information label and the prediction button

# Run the application
app.mainloop()

