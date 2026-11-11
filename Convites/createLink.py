import pandas as pd

guests = [
    # Helo
    (["Rita", "Fábio"], "15 de Agosto de 2026"),
    #(["Emilly"], "August 15, 2026"),
    (["Letícia", "Wilye"], "15 de Agosto de 2026/August 15, 2026"),
    (["Sarah", "Pedro"], "15 de Agosto de 2026"),
    (["Mariana"], "15 de Agosto de 2026"),
    (["Beatriz Dias"], "15 de Agosto de 2026"),
    (["Beatriz", "Ricardo"], "15 de Agosto de 2026"),
    #(["Silke"], "August 15, 2026"),
    (["BIF"], "15 de Agosto de 2026"),
    (["Silvia", "José"], "15 de Agosto de 2026"),
    (["Marina", "Jhon"], "15 de Agosto de 2026/August 15, 2026"),
  #Luis

  # Heloisa
    (["Júlia", "Christian"], "20 de Dezembro de 2026"),
    (["Rosângela", "Tomaz"], "20 de Dezembro de 2026"),
    (["Padrinho", "Madrinha"], "20 de Dezembro de 2026"),
    (["Patrícia", "Lucas"], "20 de Dezembro de 2026"),
    (["Gisele"], "20 de Dezembro de 2026"),
    (["Henrique", "Valdeci"], "20 de Dezembro de 2026"),
    (["Joseane", "Júnior"], "20 de Dezembro de 2026"),
    (["Márcia", "Júnior", "Lara"], "20 de Dezembro de 2026"),
    (["Marco", "Vanessa", "Letícia"], "20 de Dezembro de 2026"),
    (["Renye", "Cyndi"], "20 de Dezembro de 2026"),
    (["Tatiany"], "20 de Dezembro de 2026"),
    (["Fernando", "Felipe"], "20 de Dezembro de 2026"),
    (["Letícia", "Alexandre","Laura"], "20 de Dezembro de 2026"),
    (["Suélen", "Ronaldo","Elisa","Benjamin"], "20 de Dezembro de 2026"),
    (["Leonardo", "Patrícia", "Antonio", "Larissa"], "20 de Dezembro de 2026"),
    (["Fabiane", "Neimar","Caetano"], "20 de Dezembro de 2026"),
    (["Bruno", "Anne"], "20 de Dezembro de 2026"),
    (["Isabel", "Roberto", "Lívia"], "20 de Dezembro de 2026"),
    (["Arthur", "Karina","Júlia"], "20 de Dezembro de 2026"),
    (["Vitor"], "20 de Dezembro de 2026"),
    (["Luciana", "Evair","Gabriela"], "20 de Dezembro de 2026"),


  # Luis
  (["Fernando", "Gisele"], "20 de Dezembro de 2026"),
  (["Eloisa", "Eleazar"], "20 de Dezembro de 2026"),
  (["Teresa", "Fernando"], "20 de Dezembro de 2026"),
  (["Fabio", "Mônica"], "20 de Dezembro de 2026"),
  (["Flavio", "Márcia"], "20 de Dezembro de 2026"),
  (["Adriana", "Nelson"], "20 de Dezembro de 2026"),
  (["Eduardo", "Vanderlei"], "20 de Dezembro de 2026"),
  (["Maria Helena", "Fabio"], "20 de Dezembro de 2026"),
  (["João", "Marian"], "20 de Dezembro de 2026"),
  (["Fernanda", "Nikolas", "Olívia"], "20 de Dezembro de 2026"),
  (["Regina", "Gustavo"], "20 de Dezembro de 2026"),
  (["Beatriz", "Guilherme"], "20 de Dezembro de 2026"),
  (["Karina", "Marcos", "Mateus"], "20 de Dezembro de 2026"),
  (["Sthela", "João Goulart"], "20 de Dezembro de 2026"),
  (["Marcia"], "20 de Dezembro de 2026"),
  (["Nelson", "Dalva"], "20 de Dezembro de 2026"),
  
]

base_url = "http://casamentoheloluis.com/Convites/"

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
