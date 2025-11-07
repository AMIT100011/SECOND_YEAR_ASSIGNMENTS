emails = ["test@gmail.com", "hello123", "abc.org", "world@yahoo.com"]

# (a) Use filter() + lambda to get valid emails
valid_emails = list(filter(lambda e: "@" in e and (e.endswith(".com") or e.endswith(".org")), emails))

# (b) Extract domain names using list comprehension
domains = [email.split("@")[1].split(".")[0] for email in valid_emails]

# (c) Create dictionary for domain frequency
freq = {}
for d in domains:
    if d in freq:
        freq[d] += 1
    else:
        freq[d] = 1

# Output
print("Valid Emails:", valid_emails)
print("Domains:", domains)
print("Domain Frequency:", freq)
