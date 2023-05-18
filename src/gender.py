def gender(jmeno):
    if jmeno:
        if isinstance(jmeno, str):
            jmeno = jmeno.split("(")[0].strip()
            if jmeno[-1:] == "á":
                gender = "žena"
            elif jmeno[-3:] == "ova":
                gender = "žena"
            elif "/ž/" in jmeno:
                gender = "žena"
            elif "Vica" in jmeno:
                gender = "žena"
            elif "Chantal" in jmeno:
                gender = "žena"
            elif "Lilian" in jmeno:
                gender = "žena"
            elif "Nataša" in jmeno:
                gender = "žena"
            elif "Beata" in jmeno:
                gender = "žena"
            elif "Suzanne" in jmeno:
                gender = "žena"
            else:
                gender = "muž"
        else:
            gender = None
    else:
        gender = None
    return gender
