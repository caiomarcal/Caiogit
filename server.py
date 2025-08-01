import os, requests
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER, REPO = "caiomarcal", "Caiogit"
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}", "Accept": "application/vnd.github+json"}

@app.route("/workflows", methods=["GET"])
def list_workflows():
    r = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows", headers=HEADERS)
    return jsonify(r.json()), r.status_code

@app.route("/workflows/<int:wf_id>/dispatch", methods=["POST"])
def trigger_workflow(wf_id):
    ref = (request.json or {}).get("ref", "main")
    r = requests.post(
        f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{wf_id}/dispatches",
        headers=HEADERS, json={"ref": ref})
    return ("", r.status_code)

@app.route("/ai-plugin.json")
def plugin_manifest():
    return send_from_directory('.', 'ai-plugin.json', mimetype='application/json')

@app.route("/openapi.yaml")
def openapi_spec():
    return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333)
