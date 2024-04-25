from pydantic import BaseModel
from openai import OpenAI
import instructor
import devtools

import schema
import render

# Patch the OpenAI client
client = instructor.from_openai(OpenAI())

# Extract structured data from natural language
drawing = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=schema.Drawing,
    temperature=0.0,
    messages=[
        {"role": "user", "content": "Here is a schema."},
        {
            "role": "user",
            "content": "Draw three green 80x20 boxes side by side, labeled foo, bar etc.",
        },
    ],
)

devtools.debug(drawing)
render.draw(drawing)
