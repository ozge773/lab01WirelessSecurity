import statistics

# Define the path to your GNSS log file
file_path = '/Users/ozgef1/WirelessSecDataCleaning/data.txt'  # Replace with your actual file path

# Initialize a list to hold the Cn0DbHz values
cn0DbHz_values = []

# Open the file and start processing
with open(file_path, 'r') as file:
    for line in file:
        # Skip comment lines
        if line.startswith('#'):
            continue
        
        # Process only lines that start with "Status"
        if line.startswith('Status'):
            parts = line.strip().split(',')
            # Extract the Cn0DbHz value based on its position and convert to float
            cn0DbHz = float(parts[7])
            cn0DbHz_values.append(cn0DbHz)

# Calculate variance and standard deviation
variance = statistics.variance(cn0DbHz_values)
std_deviation = statistics.stdev(cn0DbHz_values)

print(f'Variance: {variance}')
print(f'Standard Deviation: {std_deviation}')
