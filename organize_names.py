modules = "navigation|life_support|cargo_bay|engine_control"

modules = modules.split("|")

modules = ", ".join(modules).replace("_", " ").title()


print(modules)
