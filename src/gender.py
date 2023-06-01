def gender(jmeno, zeny, nelide):
    gend = None

    zkratky = [" ml.", " nejml.", " st.", " nejst.", "PhD."]

    if jmeno:
        if isinstance(jmeno, str):
            if ("(") in jmeno:
                jmeno = jmeno.split("(")[0].strip()
            for z in zkratky:
                if z in jmeno:
                    jmeno = jmeno.split(z)[0].strip()
            if jmeno in nelide:
                pass
            elif "effects" in jmeno.lower():
                pass
            elif ".cz" in jmeno.lower():
                pass
            elif "®" in jmeno.lower():
                pass
            elif "televiz" in jmeno.lower():
                pass
            elif "agentura" in jmeno.lower():
                pass
            elif jmeno[-1:] == "á":
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
