import pandas as pd

guests = [
    # Helo Extrangeiros
     (["Rita", "Fábio"], "15 de Agosto de 2026"),
    (["Emilly"], "August 15, 2026"),
    (["Letícia", "Wilye"], "15 de Agosto de 2026/August 15, 2026"),
    (["Sarah", "Pedro"], "15 de Agosto de 2026"),
    (["Mariana"], "15 de Agosto de 2026"),
    (["Beatriz Dias"], "15 de Agosto de 2026"),
    (["Beatriz", "Ricardo"], "15 de Agosto de 2026"),
    (["Silke"], "August 15, 2026"),
    (["BIF"], "August 15, 2026"),
    (["Silvia", "José"], "15 de Agosto de 2026"),
    (["Marina", "Jhon"], "15 de Agosto de 2026/August 15, 2026"),
]

base_url = "https://casamento-hl.github.io/HeloLuis/Convites/"

rows = []

for names, date in guests:
    filename = "".join(name.replace(" ", "") for name in names)
    link = f"{base_url}{filename}.html"

    rows.append({
        "Guests": ", ".join(names),
        "Date": date,
        "Link": link
    })

# Create DataFrame
df = pd.DataFrame(rows)

# Save to Excel
df.to_excel("guest_links.xlsx", index=False)

print("Excel file saved as guest_links.xlsx")