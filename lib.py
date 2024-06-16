def clean_reference(reference: str) -> str:
    return reference.replace("%20", " ").replace(".", ":")
