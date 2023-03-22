import Userstories

available: list = ["C", "D", "E"]
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
    exec(open("./Userstories/UserStory_" + runScript.capitalize() + ".py").read())
except Exception:
    print("Det har oppstått en feil. Vennligst kjør brukerhistorien direkte fra Userstories.")
