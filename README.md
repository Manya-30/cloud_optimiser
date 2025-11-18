# Cloud_optimiser

Small example project that compares cloud providers by a simple performance-per-cost score and outputs a `performance_chart.png`.

## Files
- `main.py` — Python script that computes a performance score and saves `performance_chart.png`.
- `Jenkinsfile` — Declarative Jenkins pipeline (venv-based) that creates a venv, installs `requirements.txt`, runs `main.py`, and archives the chart.
- `Jenkinsfile.docker` — Docker-based Jenkins pipeline (runs inside `python:3.11-slim`).
- `requirements.txt` — pinned dependencies used by the project.

## Run locally (Windows PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Run locally (Linux/macOS)
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Jenkins (Pipeline from SCM)
1. Create a new Jenkins job -> Pipeline.
2. Choose "Pipeline script from SCM", set Git repo to `https://github.com/Harishsagarla/Cloud_optimiser.git`, branch `main`.
3. Ensure `Script Path` is `Jenkinsfile` (capital J).
4. Ensure the agent/node you run on has Python 3.8+ installed OR use the Docker variant.

### Using the provided `Jenkinsfile` (venv-based)
- This pipeline creates a `venv` on the agent, installs `requirements.txt`, runs `main.py`, and archives `performance_chart.png`.
- Works on both Unix and Windows agents (pipeline chooses `sh` or `bat` based on isUnix()).

### Using the Docker variant (`Jenkinsfile.docker`)
- If your Jenkins master/agents allow Docker, use `Jenkinsfile.docker` as the Script Path.
- It runs the build inside the `python:3.11-slim` container so you don't need Python installed on the agent.

## Notes
- `venv/` is git-ignored.
- If you previously committed large files (like a virtualenv), consider cleaning history with `git filter-repo` or BFG if you need to shrink repository size.

If you want, I can also:
- Add a GitHub Actions workflow that mirrors the Jenkins pipeline.
- Create a small test and CI steps that run on each push.
