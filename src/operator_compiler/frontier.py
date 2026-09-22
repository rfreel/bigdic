from itertools import permutations


def _truthy(value):
    return str(value).lower() in {"1", "true", "yes"}


def rank_lexemes(rows):
    """Prioritize lexemes where additional causal measurement can resolve more structure."""
    out = []
    for row in rows:
        flags = [x for x in row.get("review_flags", "").split("|") if x]
        priority = 1.0 + 2.0 * _truthy(row.get("requires_context_binding")) + len(flags)
        item = dict(row)
        item["priority"] = priority
        out.append(item)
    return sorted(out, key=lambda r: (-r["priority"], r.get("canonical_term", "")))


def pair_frontier(operators):
    return list(permutations(dict.fromkeys(operators), 2))


def triple_frontier(operators):
    return list(permutations(dict.fromkeys(operators), 3))
