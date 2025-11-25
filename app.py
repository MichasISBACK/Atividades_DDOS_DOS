from flask import Flask, request, jsonify
import os
import psutil

app = Flask(__name__)
allocated = []

@app.route("/t")
def test():
    p = psutil.Process(os.getpid())
    allocated_mb = request.args.get("allocate_mb", type=int)
    clear = request.args.get("clear", type=int)

    try:
        if allocated_mb:
            # Aloca memória (em bytes)
            allocated.append("X" * (allocated_mb * 1024 * 1024))
        if clear:   
            allocated.clear()
    except MemoryError:
        return jsonify(error="MemoryError"), 500

    return jsonify(
        rss_mb=p.memory_info().rss // (1024 * 1024),
        allocated_chunks=len(allocated)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
