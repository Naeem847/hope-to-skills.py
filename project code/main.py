from fastapi import FastAPI
from src.routers import data_handler
from fastapi.responses import HTMLResponse

app=FastAPI(
    title="CAG Project API Chatwith your PDF.",
    description="API for uploading PDFs, quering content via LLM,and managing data.",
    version="0.1.0",
)
app.include_router(
    data_handler.router,
    prefix="api/v1",
    tags=["Data Handling and Chat With PDF."],
)
@app.get("/",response_class=HTMLResponse,tags=["root"])
def read_root():
    """
    provide a simple HTML wellcome page with a link to the Swagger(OpenAPI) docs.
    """
    html_content="""
    <!DOCTYPE html>
    <html>
    <head>
    <title>CAG Project API</title>
    <style>
     body{font-family:Arial,sans-serif;padding:2rem;background:#f9f9f9l}
     .container{max-width:600px;margin:auto;background:#fff;padding:2rem;border: 1px solid #ddd;}
     h1{color:#333;}
     a{color:#007acc;text-decoration:none;}
     a:hover{text-decoration:none:under-line;}
     }
    </style>
    </head>
    <body>
    <div class="container">
    <h1>Wellcome to the Cag project API</h1>
    <p>view the automatically generated API documentation here:</p>
    <p><a href="/docs" target="_blank">Swagger UI(OpenAPI docs)</a></p>
    </div>
      </body>
      </html>
"""
    return HTMLResponse(content=html_content,status_code=200)

if __name__=="__main__":
 import uvicorn
# run the Fastapi APP using uvicorn
