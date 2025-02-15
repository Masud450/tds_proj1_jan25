from fastapi import FastAPI, HTTPException
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
        raise HTTPException(status_code=500, detail=str(e))
