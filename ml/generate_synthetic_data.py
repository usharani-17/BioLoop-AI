import pandas as pd
import random

# List of organic waste types
waste_types = [
    "Food Waste",
    "Cow Dung",
    "Poultry Waste",
    "Vegetable Waste",
    "Fruit Waste",
    "Agricultural Residue"
]

# List of locations
locations = [
    "Chennai",
    "Coimbatore",
    "Madurai",
    "Salem",
    "Trichy"
]

data = []

# Generate 500 sample records
for i in range(500):
    waste = random.choice(waste_types)
    quantity = random.randint(100, 10000)  # kg
    location = random.choice(locations)

    # Estimate CBG yield
    cbg_yield = round(quantity * random.uniform(0.04, 0.08), 2)

    # Estimate revenue
    revenue = round(cbg_yield * 65, 2)

    # Estimate slurry
    slurry = round(quantity * random.uniform(0.25, 0.45), 2)

    data.append([
        waste,
        quantity,
        location,
        cbg_yield,
        revenue,
        slurry
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Waste_Type",
        "Quantity_kg",
        "Location",
        "CBG_Yield",
        "Revenue",
        "Slurry"
    ]
)

df.to_csv("ml/data/synthetic_yield_dataset.csv", index=False)

print("Dataset created successfully!")