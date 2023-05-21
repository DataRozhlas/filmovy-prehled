def gender(jmeno, zeny, nelide):
    
    gend = None

    if jmeno:
        if isinstance(jmeno, str):
            if jmeno in nelide:
                pass
            if ("(") in jmeno:
                jmeno = jmeno.split("(")[0].strip()
            if jmeno[-1:] == "á":
                gend = "žena"
            elif jmeno[-3:] == "ova":
                gend = "žena"
            elif jmeno in zeny:
                gend = "žena"
            else:
                gend = "muž"
        else:
            gend = None

    return gend