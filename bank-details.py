from pathlib import Path
import shutil

# Pasta onde estão os arquivos HTML
folder = Path(".")

# Procura todos os arquivos bank-details*.html
for file in folder.glob("bank-details*.html"):

    # Ignora arquivos que já terminam com -en.html
    if file.stem.endswith("-en"):
        continue

    # Novo nome com -en antes do .html
    new_name = file.with_name(f"{file.stem}-en{file.suffix}")

    # Copia o arquivo
    shutil.copy(file, new_name)

    print(f"Copiado: {file.name} -> {new_name.name}")

print("Concluído!")