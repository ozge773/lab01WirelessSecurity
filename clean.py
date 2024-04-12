import statistics
import math

# Define the path to your GNSS log file
file_path = '/Users/ozgef1/WirelessSecDataCleaning/stationMoving.csv'  # Replace with your actual file path

# Initialize a list to hold the Cn0DbHz values
cn0DbHz_values = []
latitude_values = []

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
        
                
        # Process only lines that start with "Status"
        if line.startswith('Fix'):
            parts1 = line.strip().split(',')
            # Extract the Cn0DbHz value based on its position and convert to float
            latitude = float(parts1[2])
            latitude_values.append(latitude)
# Calculate variance and standard deviation
variance_cn0DbHz = statistics.variance(cn0DbHz_values)
std_deviation_cn0DbHz = statistics.stdev(cn0DbHz_values)



variance_latitude = statistics.variance(latitude_values)
std_deviation_latitude = statistics.stdev(latitude_values)

# Calculate RMS for cn0DbHz
rms_cn0DbHz = math.sqrt(sum(x**2 for x in cn0DbHz_values) / len(cn0DbHz_values))

# Calculate RMS for latitude
rms_latitude = math.sqrt(sum(x**2 for x in latitude_values) / len(latitude_values))


print(f'Variance for the parameter cn0DbHz : {variance_cn0DbHz}')
print(f'Standard Deviation for the parameter cn0DbHz: {std_deviation_cn0DbHz}')
print(f'RMS for the parameter cn0DbHz: {rms_cn0DbHz}\n')

print(f'Variance for the parameter latitude: {variance_latitude}')
print(f'Standard Deviation for the parameter latittude: {std_deviation_latitude}')
print(f'RMS for the parameter latitude: {rms_latitude}')