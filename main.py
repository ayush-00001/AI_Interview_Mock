"""
Development Server Entrypoint.
This simply imports the Flask app from our new Vercel architecture (api/index.py)
and runs it locally.
"""

import os
from api.index import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Local Development Server on http://127.0.0.1:{port}")
    app.run(debug=True, port=port)