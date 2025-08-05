import os
import subprocess

def clone_repo(url, dest):
    # Clona o repositório apenas se a pasta destino não existir
    if not os.path.exists(dest):
        subprocess.run(["git", "clone", url, dest], check=True)

# Repositórios de integração com Google Drive e ChatGPT
repos = {
    "gdrive-chatgpt": "https://github.com/fonckchain/gdrive-chatgpt.git",
    "chatgpt-gdrive-integration": "https://github.com/robson-koji/ChatGPT-GDrive-Integration.git",
}

for name, url in repos.items():
    clone_repo(url, name)
    # Se o projeto tiver requirements.txt, instala as dependências
    req_file = os.path.join(name, "requirements.txt")
    if os.path.exists(req_file):
        subprocess.run(["pip", "install", "-r", req_file], check=True)

print("Repos clonados e dependências instaladas. Configure OPENAI_API_KEY e GDRIVE_FOLDER_ID conforme os READMEs dos projetos.")