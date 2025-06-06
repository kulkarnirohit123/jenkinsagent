# jenkins_agent.py
import requests
from datetime import datetime
from llama_cpp import Llama

# === CONFIGURATION ===
JENKINS_URL = "http://localhost:8080"
JENKINS_USER = "admin"
JENKINS_API_TOKEN = "your_api_token_here"
MODEL_PATH = "./models/llama-2-7b.ggml.q4_0.bin"
LOG_FILE = "./logs/build_summary.log"
TEAMS_WEBHOOK_URL = "https://outlook.office.com/webhook/..."  

# === FETCH BUILDS FROM JENKINS ===
def fetch_jenkins_builds():
    url = f"{JENKINS_URL}/api/json?tree=jobs[name,builds[number,result,timestamp]]"
    try:
        response = requests.get(url, auth=(JENKINS_USER, JENKINS_API_TOKEN))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

# === RUN LOCAL LLM ===
def summarize_builds(data):
    llm = Llama(model_path=MODEL_PATH)
    prompt = """
    You are an AI DevOps assistant. Given Jenkins build data, summarize how many builds succeeded, failed, or are in progress.

    Data:
    {}""".format(str(data)[:5000])  # truncate if too large

    result = llm(prompt, max_tokens=512, echo=False)
    return result["choices"][0]["text"]

# === LOG TO FILE ===
def log_summary(summary):
    with open(LOG_FILE, "a") as f:
        f.write("\n=== {} ===\n".format(datetime.now().isoformat()))
        f.write(summary + "\n")

# === SEND TO TEAMS ===
def send_to_teams(message: str):
    payload = {
        "text": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(TEAMS_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to send message to Teams: {e}")



# === MAIN FLOW ===
def main():
    builds_data = fetch_jenkins_builds()
    if "error" in builds_data:
        log_summary("[ERROR] Failed to fetch Jenkins data: " + builds_data["error"])
        return

    summary = summarize_builds(builds_data)
    log_summary(summary)
    send_to_teams(summary)

if __name__ == "__main__":
    main()
