def clean_reference(reference: str) -> str:
    reference = (
        reference.strip().replace("%20", " ").replace(".", ":").replace("%3A", ":")
    )
    return reference
