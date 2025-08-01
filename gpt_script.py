import os
import openai


def main():
    """Exemplo simples de chamada ao GPT via OpenAI API."""
    # Certifique-se de definir a variável de ambiente OPENAI_API_KEY nos Secrets do GitHub
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = "Hello, GPT!"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
