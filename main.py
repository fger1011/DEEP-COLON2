import matplotlib.pyplot as plt

# Correlation coefficients
doc_func_eff = 1.00
prof_func_eff = 0.91
stud_func_eff = 1.00

prof_func_usab = 1.00
stud_func_usab = 1.00

doc_eff_usab = -1.00
prof_eff_usab = -1.00
stud_eff_usab = -1.00

# Group names
groups = ['Doctors', 'Professors', 'Students']

# Create scatter plot
plt.scatter([doc_func_eff], [doc_eff_usab], label='Doctors')
plt.scatter([prof_func_eff], [prof_func_usab], label='Professors')
plt.scatter([stud_func_eff], [stud_func_usab], label='Students')

# Add labels to data points
for i in range(len(groups)):
    plt.annotate(groups[i], (doc_func_eff, doc_eff_usab), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(groups[i], (prof_func_eff, prof_func_usab), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(groups[i], (stud_func_eff, stud_func_usab), textcoords="offset points", xytext=(0,10), ha='center')

# Set axis labels and title
plt.xlabel('Functionality vs Efficiency')
plt.ylabel('Functionality vs Usability')
plt.title('Scatter Plot of Functionality, Efficiency, and Usability')

# Add legend
plt.legend()

# Show the plot
plt.show()
