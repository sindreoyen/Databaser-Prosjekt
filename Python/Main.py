import DB2tasks.LocalData
import subprocess

available: list = ["C", "D", "E", "G", "H"]
runScript: str = ""
prompt = """
Hei! Vennligst velg hvilken brukerhistorie du vil kjøre:
Disse er tilgjengelige: 
"""
prompt += str(available) + "\n"

while runScript.capitalize() not in available:
    runScript = input(prompt)

### Run script
try:
    path = DB2tasks.LocalData.path + "/UserStory_" + runScript.capitalize() + ".py"
    print(path)
    subprocess.run(["python", path])
except Exception:
    print("Det har oppstått en feil. Vennligst kjør brukerhistorien direkte fra Userstories.")
