from models.company_model import Company


def merge_companies(
    existing: list[Company],
    new: list[Company]
) -> list[Company]:
    """
    Merge two company lists while removing duplicates.

    Companies are uniquely identified by their `key`
    (ticker if available, otherwise input_name).
    """

    merged = {}

    for company in existing:
        merged[company.key] = company

    for company in new:
        merged[company.key] = company

    return list(merged.values())    