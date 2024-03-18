# COMMAND ----------

dbutils.widgets.text(name="ensemble_file_path", defaultValue="", label="ENSEMBLE json-file Path")

# COMMAND ----------

ensemble_file_path = dbutils.widgets.get("ensemble_file_path")

# COMMAND ----------

import json

ensemble_file_path_file_api = ensemble_file_path.replace('dbfs:', '/dbfs')

with open(ensemble_file_path_file_api) as file:
    data = json.load(file)

# COMMAND ----------

print(data)
