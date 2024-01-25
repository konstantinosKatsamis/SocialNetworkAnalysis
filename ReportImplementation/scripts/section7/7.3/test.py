import matplotlib.pyplot as plt

def truncate_to_two_decimals(number):
    number_str = str(number)
    decimal_index = number_str.find('.')
    if decimal_index != -1:
        return float(number_str[:decimal_index + 3])
    else:
        return number

def create_table_b(ta):
    counts_dict = {}

    for value in ta:
        # Truncate the number to two decimal places
        truncated_value = truncate_to_two_decimals(value)

        # Exclude 0 values
        if truncated_value != 0:
            if truncated_value in counts_dict:
                counts_dict[truncated_value] += 1
            else:
                counts_dict[truncated_value] = 1

    tb = [[key, value] for key, value in counts_dict.items()]
    return tb

# Read numbers from a text file
with open('ma.txt', 'r') as file:
    lines = file.readlines()

# Convert lines to a list of floating-point numbers
ta = [float(line.strip()) for line in lines]

# Create table b
tb = create_table_b(ta)


# Extract x and y values for plotting
x_values = [row[0] for row in tb]
y_values = [row[1] for row in tb]

# Manually set y-axis and x-axis values
desired_yticks = [1, 2, 3, 4, 5, 6, 7, 8]  # Add more values as needed
desired_xticks = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]#x_values  # Use unique truncated values for x-axis
plt.yticks(desired_yticks)
plt.xticks(desired_xticks)


# Create a bar chart
plt.bar(x_values, y_values, width=0.009) # width of bars
plt.xlabel('Grouped closeness centrality values')
plt.ylabel('Counter')
plt.title('Closeness Centrality')

plt.show()
