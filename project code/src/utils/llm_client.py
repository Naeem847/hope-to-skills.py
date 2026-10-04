import os
from google import genai
from google.genai import types
from dotenv import load_dotenv,find_dotenv
# load enviroment variables from .env file
load_dotenv(find_dotenv())
from fastapi import APIRouter, UploadFile, HTTPException
def get_llm_response(context: str, query: str) -> str:
    """
    send a user query and contect to google genai and return the assistant's response.
    Args:
        context (str): background information delimited by triple backticks.
        query (str): The user's question to be answered based on the context.
    
    Returns:
        str: the assistant generated text response.
        Raises: 
        ValueError: If the context or query is empty.or if the GEMINAI_API_KEY environment variable is not set.
    """
    api_key = os.environ.get("GEMINAI_API_KEY")
    if not api_key:
        raise ValueError("GEMINAI_API_KEY environment variable is not set."
                         "please set it to your google genai api key.(get key from https://aistudio.google.com/)")
    # initialize the genAI client with the API key
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash"  # specify the model to use
    contents=[
        types.Cntent(
            role="user",
            parts=[types.part.from_text(text=query)],
        ),
    ]
    generate_content_config=types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(
                text=("you are a helpful assistant that answers questions based on the provided context delimited by triple backticks.\n\n"
        "you will be given a context and a user query your task is to generate an answer based on the context:\n\n"
        "relevent to the query based on the cntext provided. if the context does not contain the answer, respond with 'I don't know.\n\n"
        "information to answer the query, you should indicate that youdo not have enough information to answer the query.\n\n"
        "to provide a complete answer\n\n"
        "if the context is empty you should responce with a message indacating\n\n"
        "enough information to answer the query\n\n"
        "you should always responce in a fiendly snd heplful manner,you should not make up answers if the context does not contain the answer to the query.\n\n"
        "personal openions or information in your responses\n\n"
        "you should not provide any personal opinions or information in your responses\n\n:"f"Context:\n```{context}```"
           )
        ),
    ],

    )
    # stream and accumulate the response
    response_text=""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.type == types.ComputeTokensResponse.ChunkType.RESPONSE:

            response_text += chunk.text

    return response_text