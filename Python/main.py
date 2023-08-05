import datetime
import FormatValues as FV

# Load default values from OSICDef.dat
f = open('OSICDef.dat', 'r')
NEXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_COVERAGE = float(f.readline())
GLASS_COST = float(f.readline())
LOANER_CAR_COST = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()

# Function to calculate extra costs based on user input
def calculate_extra_costs(options, num_cars):
    extra_liability_cost = 130.0 if 'Y' in options else 0
    glass_coverage_cost = 86.0 if 'Y' in options else 0
    loaner_car_cost = 58.0 if 'Y' in options else 0
    return (extra_liability_cost + glass_coverage_cost + loaner_car_cost) * num_cars

# Function to calculate the total insurance premium
def calculate_insurance_premium(basic_premium, num_cars):
    return basic_premium + ((num_cars - 1) * (basic_premium * ADD_CAR_DISCOUNT))

# Function to format the date as "yyyy-mm-dd"
def format_date(date):
    return date.strftime("%Y-%m-%d")

# Main program loop
policy_records = []
total_policies = 0
total_premiums = 0

with open('NewPolicies.dat', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line.strip():  # Skip empty lines
            policy_data = line.strip().split(', ')
            NEXT_POLICY_NUM = int(policy_data[0])
            InvDate = datetime.datetime.strptime(policy_data[1], "%Y-%m-%d")
            CustFirstName = policy_data[2]
            CustLastName = policy_data[3]
            StAdd = policy_data[4]
            City = policy_data[5]
            Province = policy_data[6]
            PostalCode = policy_data[7]
            PhoneNum = policy_data[8]
            NumCarInsured = int(policy_data[9])
            ExtraLiability = policy_data[10]
            GlassCoverage = policy_data[11]
            LoanerCar = policy_data[12]
            PayMethod = policy_data[13]
            InsurancePremium = float(policy_data[14][1:])

            ExtraCosts = calculate_extra_costs([ExtraLiability, GlassCoverage, LoanerCar], NumCarInsured)
            TotalInsurancePremium = InsurancePremium + ExtraCosts

            # Update the total policies count and total premiums
            total_policies += 1
            total_premiums += TotalInsurancePremium

            # Append the policy information to the policy_records list
            policy_records.append((NEXT_POLICY_NUM, CustFirstName + " " + CustLastName, format_date(InvDate),
                                   FV.FDollar2(InsurancePremium), FV.FDollar2(ExtraCosts), FV.FDollar2(TotalInsurancePremium)))

# Print the policy listing report
print("\nONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF {format_date(datetime.datetime.now())}")
print("POLICY   CUSTOMER             TOTAL      TOTAL   MONTHLY")
print("NUMBER   NAME                PREMIUM      HST    PAYMENT")
print("=" * 65)
for policy_record in policy_records:
    print(f"{policy_record[0]:<8d} {policy_record[1]:<22s} {policy_record[2]:<10s} {policy_record[3]:<10s} {policy_record[4]:<10s}")
print("=" * 65)
print(f"Total policies: {total_policies:<7d} {FV.FDollar2(total_premiums):<10s}")

# Write the current values back to the defaults file.
with open('OSICDef.dat', 'w') as f:
    f.write(f"{NEXT_POLICY_NUM}\n")
    f.write(f"{BASIC_PREMIUM}\n")
    f.write(f"{ADD_CAR_DISCOUNT}\n")
    f.write(f"{EXTRA_LIABILITY_COVERAGE}\n")
    f.write(f"{GLASS_COST}\n")
    f.write(f"{LOANER_CAR_COST}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESSING_FEE}\n")
    f.close()
