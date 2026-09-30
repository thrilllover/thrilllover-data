# Stage 1: Data Exploration

'''1. Load all six datasets into Pandas DataFrames.
Display the first 10 rows and last 10 rows of every dataset.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

appointments_df = pd.read_csv('Appointments.csv')
date_df = pd.read_csv('Date_Table.csv')
doctors_df = pd.read_csv('Doctors.csv')
hospitals_df = pd.read_csv('Hospitals.csv')
patients_df = pd.read_csv('Patients.csv')
treatments_df = pd.read_csv('Treatments.csv')

dataframes = [appointments_df, patients_df, treatments_df, hospitals_df, doctors_df, date_df]
names = ['Appointments', 'Patients', 'Treatments', 'Hospitals', 'Doctors', 'Date']
for d in range(len(dataframes)):
    print(f'========{names[d]}===========')
    print(dataframes[d].head(10))
    print(dataframes[d].tail(10))


'''2. Display the shape, column names, and data types for every dataset.'''
for d in range(len(dataframes)):
    print(f'==============={names[d]}===================')
    print('The Shape is:', dataframes[d].shape)
    print(dataframes[d].info())


'''3. Generate descriptive statistics for all numerical columns.'''


print('Descriptive statistics:\n',appointments_df['Consultation_Fee'].describe())
print('Descriptive statistics:\n', patients_df['Age'].describe())
print('Descriptive statistics:\n', treatments_df['Treatment_Cost'].describe())
print('Descriptive statistics:\n', doctors_df['Experience_Years'].describe())


'''4. Identify missing values in every dataset.
Display the total number of missing values per column'''

for d in range(len(dataframes)):
    print(f'============{names[d]}==============')
    print(dataframes[d].isnull().sum())


'''5. Identify duplicate records in every dataset.
Display the total number of duplicate rows.'''

for d in range(len(dataframes)):
    print(f'============{names[d]}==============')
    print(dataframes[d].duplicated().sum())

print(appointments_df[appointments_df.duplicated()])
print(treatments_df[treatments_df.duplicated()])


# Stage 2: Data Cleaning

'''6. Convert all date-related columns into datetime format.'''

for df in dataframes:
    for column in df.columns:
        if 'Date' in column:
            df[column] = pd.to_datetime(df[column])


'''7. Handle missing values using appropriate techniques.
(Hint: Using these two functions: fillna(), dropna())'''

print(appointments_df[appointments_df['Appointment_Type'].isnull()])
print(appointments_df["Appointment_Type"].value_counts())
appointments_df['Appointment_Type'] = appointments_df['Appointment_Type'].fillna('Unknown')

print(patients_df[patients_df['City'].isnull()])
print(patients_df['City'].value_counts())
patients_df['City'] = patients_df['City'].fillna('Unknown')

print(treatments_df[treatments_df['Treatment_Cost'].isnull()])
print(treatments_df['Treatment_Type'].value_counts())

mri_median = treatments_df[treatments_df['Treatment_Type'] == 'MRI']['Treatment_Cost'].median()

treatments_df.loc[
    (treatments_df['Treatment_Type'] == 'MRI') & 
    (treatments_df['Treatment_Cost'].isnull()), 
    'Treatment_Cost'] = mri_median


'''8. Remove duplicate records from all datasets.'''

print(appointments_df[appointments_df.duplicated()])
appointments_df = appointments_df.drop_duplicates()

print(treatments_df[treatments_df.duplicated()])
treatments_df = treatments_df.drop_duplicates()

'''9. Standardize text-based columns so that values are consistently formatted.
(Hint: Using these functions: str.strip(), str.ftle())'''

# Appointments:

print(appointments_df['Appointment_Status'].value_counts())
print(appointments_df['Appointment_Type'].value_counts())

appointments_df['Appointment_Status'] = appointments_df['Appointment_Status'].str.strip().str.title()

print(appointments_df['Appointment_Status'].value_counts())

# Hospitals:

print(hospitals_df['Region'].value_counts())

hospitals_df['Region'] = hospitals_df['Region'].str.strip().str.title()
print(hospitals_df['Region'].value_counts())

# Doctors:
print(doctors_df['Specialization'].value_counts())

doctors_df['Specialization'] = doctors_df['Specialization'].str.strip().str.title()
print(doctors_df['Specialization'].value_counts())

# Changing data types:

appointments_df['Consultation_Fee'] = appointments_df['Consultation_Fee'].astype('float64')
treatments_df['Treatment_ID'] = treatments_df['Treatment_ID'].astype('Int64')

# Stage 3: Data Integration

'''10. Merge the Appointments and Patients datasets into a new dataset master_df.'''

master_df = pd.merge(
appointments_df,
patients_df,
on = 'Patient_ID',
how = 'left'
)
print(master_df.head(10))

'''11. Merge the master_df and Doctors datasets.'''
master_df1 = pd.merge(
    master_df,
    doctors_df,
    on = 'Doctor_ID',
    how = 'left'
)
print(master_df1.head())

'''12. Merge the master_df and Hospitals datasets.'''
master_df2 = pd.merge(
    master_df1,
    hospitals_df,
    on = 'Hospital_ID',
    how = 'left'
)
print(master_df2.head())

'''13. Create a final Master Dataset containing information from all five operational datasets.'''

final_master_df = pd.merge(
    master_df2,
    treatments_df,
    on = 'Appointment_ID',
    how = 'left'
)
print(final_master_df.head())

final_master_df.to_csv('Final_Business_Report.csv', index = False)
final_master_df.to_excel('Final_Business_Report.xlsx', index = False)


# Stage 4: Business Analysis

'''14. Calculate:
• Total Appointments
• Total Revenue'''

print(final_master_df.info())

total_appointments = final_master_df['Appointment_ID'].nunique()

final_master_df['Total_Revenue'] = final_master_df['Treatment_Cost'].fillna(0)

appointment_1 = ~ final_master_df['Appointment_ID'].duplicated()
final_master_df.loc[appointment_1, 'Total_Revenue'] += final_master_df.loc[appointment_1, 'Consultation_Fee']


print('Total Appointments:', total_appointments)
print('Total Revenue:', final_master_df['Total_Revenue'].sum())

final_master_df.to_excel('Revenue_Analysis_Report.xlsx', index = False)


'''15. Show Total Revenue by Hospital.
Sort the results from highest to lowest.'''

total_revenue_hospital = final_master_df.groupby('Hospital_Name')['Total_Revenue'].sum()

top_revenue_hospital= total_revenue_hospital.sort_values(ascending = False)
print(top_revenue_hospital)

top_revenue_hospital.to_excel('Hospitals_Revenue_Report.xlsx')

'''16. Show Total Revenue by Region.
Sort the results from highest to lowest.'''

total_revenue_region = final_master_df.groupby('Region')['Total_Revenue'].sum()

top_revenue_region = total_revenue_region.sort_values(ascending = False)
print(top_revenue_region)

top_revenue_region.to_excel('Regions_Revenue_Report.xlsx')

'''17. Show Total Revenue by Specialisation.
Sort the results from highest to lowest.'''

total_revenue_special = final_master_df.groupby('Specialization')['Total_Revenue'].sum()

top_revenue_special = total_revenue_special.sort_values(ascending = False)
print(top_revenue_special)

top_revenue_special.to_excel('Specialisation_Revenue_Report.xlsx')

'''18. Show Total Revenue by Patient Category.'''

t_revenue_patient = final_master_df.groupby('Patient_Category')['Total_Revenue'].sum()

print(t_revenue_patient)

t_revenue_patient.to_excel('Patient_Category_Revenue_Report.xlsx')


'''19. Identify the Top 10 Doctors by Revenue.'''

total_revenue_doctor = final_master_df.groupby('Doctor_Name')['Total_Revenue'].sum()
top_10_doctors = total_revenue_doctor.sort_values(ascending = False).head(10)

print('Top 10 Doctors:' , top_10_doctors)

top_10_doctors.to_excel('Top_Doctors_Report.xlsx')


'''20. Identify the Top 10 Treatment Types by Revenue.'''

treatment_type_revenue = final_master_df.groupby('Treatment_Type')['Total_Revenue'].sum()
top_10_treatments = treatment_type_revenue.sort_values(ascending = False).head(10)
print(top_10_treatments)

top_10_treatments.to_excel('Top_Treatments_Report.xlsx')

'''21. Show Revenue by Year.'''

final_master_df['Year'] = final_master_df['Appointment_Date'].dt.year

total_revenue_year = final_master_df.groupby('Year')['Total_Revenue'].sum()
print(total_revenue_year.sort_values(ascending = False))

total_revenue_year.to_excel('Yearly_Revenue_Report.xlsx')

'''22. Show Revenue by Month'''

final_master_df['Month'] = final_master_df['Appointment_Date'].dt.month_name()

revenue_month = final_master_df.groupby('Month')['Total_Revenue'].sum()
print(revenue_month)

revenue_month.to_excel('Monthly_Revenue_Report.xlsx')

# Stage 5: Data Visualisation

'''23. Create a Bar Chart showing the Top 10 Doctors by Revenue'''

plt.figure(figsize = (8,6))
sns.barplot(data = top_10_doctors, color = 'darkorange')

plt.title('Top Doctors by Revenue')
plt.xlabel('Doctor')
plt.ylabel('Total_Revenue')
plt.xticks(rotation=30)

plt.tight_layout()
plt.ticklabel_format(style = 'plain', axis = 'y')

plt.savefig(
    'top_10_doctors.png',
    dpi = 600,
    bbox_inches = 'tight'
)
plt.show()

'''24. Create a Bar Chart showing Revenue by Hospital.'''

plt.figure(figsize = (9,7))
sns.barplot(data = top_revenue_hospital, color= 'darkorange')

plt.title('Total Revenue By Hospitals')
plt.xlabel('Hospital')
plt.ylabel('Total_Revenue')
plt.xticks(rotation=30)

plt.tight_layout()
plt.ticklabel_format(style = 'plain', axis = 'y')

plt.savefig(
    'hospitals_revenue.png',
    dpi = 600,
    bbox_inches = 'tight'
)
plt.show()

'''25. Create a Line Chart showing Monthly Revenue Trends.'''

plt.figure(figsize=(9,7))
plt.plot(revenue_month, 
         color = 'darkorange',
         marker = 'o',
         linestyle = '--'
          )

plt.title('Monthly Revenue Trends')
plt.xlabel('Months')
plt.xticks(rotation = 30)
plt.ylabel('Total Revenue')
plt.grid(True)
plt.ticklabel_format(style = 'plain', axis = 'y')
plt.tight_layout()

plt.savefig(
    'monthly_revenue_trend.png',
    dpi = 600,
    bbox_inches = 'tight'
)
plt.show()

'''26. Create a Pie Chart showing Patient Category Distribution.'''

category = final_master_df['Patient_Category'].value_counts()
plt.pie(category, labels= category.index, autopct= '%1.1f%%')
plt.title('Patient Category Distribution')

plt.savefig(
    'patient_category_distribution.png',
    dpi = 600,
    bbox_inches = 'tight'
)
plt.show()


'''27. Create a Histogram showing Treatment Cost Distribution.'''

plt.hist(final_master_df['Treatment_Cost'].dropna(), bins = 10)

plt.title('Treatment Cost Distribution Histogram')
plt.xlabel('Treatment Cost')
plt.ylabel('Frequency')

plt.savefig(
    'treatment_cost_distribution.png',
    dpi = 600,
    bbox_inches = 'tight'
)
plt.show()


'''28. Create a Correlation Heatmap using Seaborn.'''

numeric_data = final_master_df.groupby('Appointment_ID').agg({
     'Age' : 'first',
     'Consultation_Fee' : 'first',
     'Experience_Years' : 'first',
     'Treatment_Cost' : 'sum',
     'Total_Revenue' : 'sum'
 })
#numeric_data = final_master_df[['Age', 'Experience_Years',  'Treatment_Cost', 'Consultation_Fee', 'Total_Revenue' ]]

correlation_matrix = numeric_data.corr()
plt.figure(figsize = (9,7))

sns.heatmap(
    correlation_matrix,
    annot = True,
    fmt = '.2f',
    cmap = 'coolwarm',
    center = 0,
    linewidths = 0.5,
    square = True,
    cbar_kws = {'label':'Correlation Coefficient'}
)

plt.title('Correlation Heatmap')
plt.xticks(rotation = 30)
plt.tight_layout()

plt.savefig(
    'correlation_heatmap.png',
    dpi = 600,
    bbox_inches = 'tight'
)
plt.show()