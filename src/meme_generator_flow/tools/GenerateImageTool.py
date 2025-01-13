from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from openai import OpenAI
import os #requests

class GenerateImageInput(BaseModel):
    """Input schema for GenerateImageInput."""

    imageprompt: str = Field(..., description="Prompt to generate image.")


class GenerateImageTool(BaseTool):
    name: str = "Generate Image"
    description: str = (
        "Generates an image that encapsulates the provided meme concept."
    )
    args_schema: Type[BaseModel] = GenerateImageInput

    def _run(self, imageprompt: str) -> str:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.images.generate(
            model="dall-e-3",
            prompt=imageprompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        # words = chapter_content_and_character_details.split()[:5] 
        # safe_words = [re.sub(r'[^a-zA-Z0-9_]', '', word) for word in words]  
        # filename = "_".join(safe_words).lower() + ".png"
        # filename = "memeimage"+".png"
        # filepath = os.path.join(os.getcwd(), filename)

        # # Download the image from the URL
        # image_response = requests.get(image_url)
        # if image_response.status_code == 200:
        #     with open(filepath, 'wb') as file:
        #         file.write(image_response.content)
        # else:
        #     print("Failed to download the image.")
        #     return ""

        return image_url
