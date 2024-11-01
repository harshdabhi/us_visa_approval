import os
from pathlib import Path

project_name = "usa_visa_approval"


list_of_files = [
    

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",

    f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/predict_pipeline.py",

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
 

    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logger.py",

    f"{project_name}/notebook/__init__.py",
    f"{project_name}/notebook/notebook.ipynb",



    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "demo.py",
    "config/config.yaml",
    "config/schema.yaml"


 
     ]

for files in list_of_files:
    file_path = Path(files)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass

    else:
        print(f"{file_name} already exists")