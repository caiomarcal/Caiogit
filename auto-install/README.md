# Pacote de instalação de atalhos e integrações

Este diretório contém um script (`setup.py`) e instruções para configurar integrações de IA no iPadOS 26.

## Passos para usar

1. Clone ou baixe esta pasta para o iPad (via Pythonista ou Carnets).
2. Execute `python3 setup.py` para clonar os projetos de integração e instalar dependências.
3. Configure as variáveis `OPENAI_API_KEY` e `GDRIVE_FOLDER_ID` nos respectivos projetos.
4. Importe os atalhos abaixo no app **Atalhos** (Shortcuts) do iPad e forneça sua chave da API quando solicitado.

### Atalhos (links iCloud)

- **ChatGPT Siri**: instalar via iCloud em `https://www.icloud.com/shortcuts/debc9a9029854473b515414cc7766b47`.
- **Notefy**: instalar via iCloud em `https://www.icloud.com/shortcuts/219e814900024849845fd0f7e8d36592`.
- **Share‑to‑ChatGPT**: instalar via iCloud em `https://www.icloud.com/shortcuts/25262952f34544e99b9e6678056c1168`.

Para cada atalho, ative o "Compartilhamento Privado" em Ajustes > Shortcuts e toque no link no Safari para adicionar.

### Observações

- O script `setup.py` deve ser executado em um ambiente Python com acesso a internet.
- O projeto não contém códigos de terceiros; apenas clona os repositórios originais.