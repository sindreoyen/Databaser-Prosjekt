import DB2tasks.LocalData
import subprocess

available: list = ["C", "D", "E", "G", "H"]
runScript: str = ""
prompt = """
Velkommen! Vennligst velg en brukerhistorie fra alternativene nedenfor:
- C: Finn togruter som passerer en bestemt stasjon på en ukedag
- D: Søk etter togruter mellom start- og sluttstasjoner, sortert etter dato og tid
- E: Registrer deg som bruker
- G: Finn og kjøp tilgjengelige billetter
- H: Se din billetthistorikk
Vennligst skriv bokstaven som tilsvarer ønsket brukerhistorie.
"""

while runScript.capitalize() not in available:
    runScript = input(prompt)

### Run script
try:
    path = DB2tasks.LocalData.path + DB2tasks.LocalData.sep + "UserStory_" + runScript.capitalize() + ".py"
    print(path)
    subprocess.run(["python", path])
except Exception:
    print("Det har oppstått en feil. Vennligst kjør brukerhistorien direkte fra '/DB2Tasks/UserStory_" + runScript.capitalize() +"'")
