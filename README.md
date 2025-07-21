
 Siebel Backend Task - Flask API

## Project Setup

1. Clone the Repository
git clone  https://github.com/aditikakade01/siebel-backend-task.git 
cd siebel-backend-task


2 . Create Virtual Environment
python -m venv venv
.\venv\Scripts\activate

If you are using bash (Git Bash or Mac/Linux):
source venv/bin/activate

3 . Install Requirements
pip install -r requirements.txt

## Run the Project Locally
Create .env file
Inside the project root folder, create a .env file with:

DB_URL=postgresql://neondb_owner:<your-password>@<your-neon-host>/<your-database-name>?sslmode=require&channel_binding=require

## Run the Flask App
Use:
python -m myapp.app

## App will be live at:
**[http://localhost:5000](http://localhost:5000)**


## Database
" Neon PostgreSQL " is used
 Table: `case_submission`

 To check submitted form data:
1️. Go to [Neon Console](https://console.neon.tech)
2️. Open SQL Editor
3️. Run:

```sql
SELECT * FROM case_submission;

## Tech Stack
Python 3.12
 Flask
 SQLAlchemy ORM
 Neon PostgreSQL (for database)


- Note
If VSCode shows `Import "flask_cors" could not be resolved`, add this to:
.vscode/settings.json
```json
{
    "python.analysis.extraPaths": ["./myapp"],
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingImports": "none"
    }
}



