# Cable Insulation Resistance Calculator
# Calculates insulation resistance using:
# R = rho * L / A

print("========================================")
print("   CABLE INSULATION RESISTANCE CALCULATOR")
print("========================================")

# Input values
resistivity = float(input("Enter insulation resistivity (ohm-meter): "))
length = float(input("Enter cable length (m): "))
area = float(input("Enter cross-sectional area (m^2): "))

# Calculate insulation resistance
resistance = resistivity * length / area

# Display result
print("\n------------- RESULT ----------------")
print(f"Cable Length              : {length:.2f} m")
print(f"Cross-sectional Area      : {area:.6e} m^2")
print(f"Insulation Resistivity    : {resistivity:.2e} ohm-m")
print(f"Insulation Resistance     : {resistance:.2f} ohms")
print("-------------------------------------")
