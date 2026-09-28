status = "WARNING::ENGINE_OVERHEAT::SECTOR_7"

status = status.replace("::", " | ").replace("_", " ").lower()

print(status)
