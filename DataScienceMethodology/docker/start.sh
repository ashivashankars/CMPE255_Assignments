#!/usr/bin/env bash
set -e
# Default to serving the CRISP-DM API; adjust as needed.
uvicorn crispdm_homecredit.src.serve:app --host 0.0.0.0 --port 8000
