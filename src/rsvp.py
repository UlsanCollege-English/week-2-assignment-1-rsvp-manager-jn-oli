import re
from collections import defaultdict

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

def dedupe_emails_case_preserve_order(emails):
    seen = set()
    result = []
    for email in emails:
        if not EMAIL_REGEX.match(email):
            continue
        folded = email.casefold()
        if folded not in seen:
            seen.add(folded)
            result.append(email)
    return result


def first_with_domain(emails, domain):
    target = domain.casefold()
    for idx, email in enumerate(emails):
        if EMAIL_REGEX.match(email):
            local, _, dom = email.partition("@")
            if dom.casefold() == target:
                return idx
    return None


def domain_counts(emails):
    counts = defaultdict(int)
    for email in emails:
        if EMAIL_REGEX.match(email):
            domain = email.split("@")[1].casefold()
            counts[domain] += 1
    # Return sorted by domain name
    return sorted(counts.items())
