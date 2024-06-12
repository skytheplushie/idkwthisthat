projects_hg_done = {"Mielebee": True, "Eisendrache": True, "Syliru": True, "Diraixos": False, "Avefir": False,
                    "Nadaler": False, "Fayrah": False, "Dysuva": False, "Paranox": False, "Falugeis": False,
                    "Desygual": False, "Hielochiim": False, "Aethereus": False}
print(projects_hg_done)
print(projects_hg_done["Mielebee"])
print(projects_hg_done["Nadaler"])
projects_hg_done.update({"Diraixos": True, "Avefir": True})
projects_hg_done["Moixaura"] = False
projects_hg_done["Uheailes"] = False
print(projects_hg_done["Aethereus"])
del projects_hg_done["Aethereus"]
print(projects_hg_done)
