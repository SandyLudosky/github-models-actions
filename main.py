
from dotenv import load_dotenv

from openai import OpenAI # type: ignore
from colorama import Fore
import base64

from rich.console import Console # type: ignore
from rich.pretty import pprint
 
load_dotenv()


client = OpenAI()   
console = Console()
console.rule("[bold green]Running Eval for User Request Categorization[/bold green]")



response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn."
)

pprint(response)

response = client.responses.create(
    model="gpt-5",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation"}],
)

# Save the image to a file
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]
    
if image_data:
    image_base64 = image_data[0]
    with open("otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))