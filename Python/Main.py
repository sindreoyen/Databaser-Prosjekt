import DB2tasks.LocalData
import subprocess

available: list = ["C", "D", "E", "G", "H"]
runScript: str = ""
prompt = """
Hei! Vennligst velg hvilken brukerhistorie du vil kjøre:
Disse er tilgjengelige: 
C - Togruter innom stasjon (Ukedag)
D - Søk blant togruter mellom start og sluttstasjon, basert og sortert på dato og tid
E - Registrere bruker
G - Finn og kjøpe ledige billetter
H - Se din billetthistorikk
"""

while runScript.capitalize() not in available:
    runScript = input(prompt)

### Run script
try:
    path = DB2tasks.LocalData.path + "/UserStory_" + runScript.capitalize() + ".py"
    print(path)
    subprocess.run(["python", path])
except Exception:
    print("Det har oppstått en feil. Vennligst kjør brukerhistorien direkte fra '/DB2Tasks'.")
