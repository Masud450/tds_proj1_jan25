'''from fastapi import FastAPI, HTTPException
from tasksB import *

app = FastAPI()

@app.post("/run")
async def run_task(task: str, params: dict = {}):
    try:
        if "fetch data" in task:
            result = fetch_data_from_api(params["url"], params["save_path"])
        elif "clone repo" in task:
            result = clone_and_commit(params["repo_url"], params["commit_message"])
        elif "run SQL" in task:
            result = run_sql_query(params["db_path"], params["query"], params["output_path"])
        elif "scrape website" in task:
            result = scrape_website(params["url"], params["save_path"])
        elif "resize image" in task:
            result = compress_or_resize_image(params["input_path"], params["output_path"], params["width"], params["height"])
        elif "transcribe audio" in task:
            result = transcribe_audio(params["audio_path"], params["output_path"])
        elif "convert Markdown" in task:
            result = convert_md_to_html(params["md_path"], params["html_path"])
        elif "filter CSV" in task:
            result = filter_csv(params["csv_path"], params["column"], params["value"])
        else:
            raise HTTPException(status_code=400, detail="Unknown task")
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))'''
        
from fastapi import FastAPI, HTTPException, Query
import requests
import os

app = FastAPI()

# Helper function to validate path
def validate_path(file_path):
    if not file_path.startswith("/data/"):
        raise ValueError("Access to paths outside /data/ is restricted.")

@app.post("/run")
async def run_task(task: str = Query(...), url: str = Query(None), save_path: str = Query(None)):
    if "fetch data" in task.lower():
        if not url or not save_path:
            raise HTTPException(status_code=400, detail="Missing required parameters: 'url' and 'save_path'")
        try:
            # Make sure the URL is valid
            if not (url.startswith("http://") or url.startswith("https://")):
                raise HTTPException(status_code=400, detail="Invalid URL. Must start with 'http://' or 'https://'.")

            # Validate save path
            validate_path(save_path)

            # Fetch data from URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad HTTP responses

            # Save the fetched data
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "w") as file:
                file.write(response.text)

            return {"status": "success", "message": f"Data fetched from {url} and saved to {save_path}"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")

