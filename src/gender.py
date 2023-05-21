def gender(jmeno):
    
    import os
    import json
    
    with open(os.path.join("data_fixes", "zeny.json"), encoding="utf-8") as zeny:
        zeny = json.loads(zeny.read())

    if jmeno:
        if isinstance(jmeno, str):
            if ("(") in jmeno:
                jmeno = jmeno.split("(")[0].strip()
            if jmeno[-1:] == "á":
                gender = "žena"
            elif jmeno[-3:] == "ova":
                gender = "žena"
            elif jmeno in zeny:
                gender = "žena"
            else:
                gender = "muž"
        else:
            gender = None
    else:
        gender = None
    return gender