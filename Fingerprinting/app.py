from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

HEADERS_TO_CHECK = (
    "User-Agent",
    "Accept-Language",
    "Accept",
    "Accept-Encoding",
    "Referer",
    "Sec-Fetch-Site",
    "Sec-Fetch-Mode",
    "Sec-CH-UA",
)


@app.get("/")
def home():
    print("\n========== NEW VISIT ==========", flush=True)
    print("IP address:", request.remote_addr, flush=True)
    print("HTTP method:", request.method, flush=True)
    for name in HEADERS_TO_CHECK:
        print(f"{name}: {request.headers.get(name, '(not sent)')}", flush=True)
    print("===============================\n", flush=True)
    return render_template("index.html")


@app.post("/collect")
def collect():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="Send a JSON object"), 400

    print("\n========== COLLECT ==========", flush=True)
    for name, value in data.items():
        print(f"{name}: {value}", flush=True)
    print("=============================\n", flush=True)
    return jsonify(status="received")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
