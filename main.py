import os
import dotenv
from colorama import Fore, Style

from openai import OpenAI

dotenv.load_dotenv()


# Get GitHub token from environment variable
github_token = os.getenv("GIT_TOKEN")
if not github_token:
    raise ValueError(
        "GIT_TOKEN environment variable is not set. "
        "Please set it with: export GIT_TOKEN'your_token_here'"
    )

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=github_token,
    default_query={
        "api-version": "2024-08-01-preview",
    },
)

messages = [{
    "role": "system",
    "content": (
        "You are a specialist in translating from French to English. Provide the English translation for the given word along with examples of its usage in English. Adhere to any specific instructions provided, if applicable."
    ),
}]

def main():
    print(Style.BRIGHT + "//==============*****Assistant IA/Traducteur*****===============//" + Style.RESET_ALL)
    print(Fore.CYAN +  "\n-Taper votre question\n–Taper 'quit' pour sortir.\n" + Style.RESET_ALL)
     
    while True:
        user_input = input("Vous: ")

        if user_input.lower() in ("quit", "exit", "q"):
            print(Style.BRIGHT + Fore.CYAN + "Assistant: À bientôt 👋" + Style.RESET_ALL)
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                messages=messages,
                model="gpt-4o-mini", 
                temperature=1.0,
            )
            # console.print(response)
            print(Style.BRIGHT + Fore.GREEN + response.choices[0].message.content + Style.RESET_ALL)
     
        except Exception as e:
            print(e)
            continue
    
if __name__ == "__main__":
    main()