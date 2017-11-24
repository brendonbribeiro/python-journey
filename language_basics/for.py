emails = ["me@gmail.com", "myself@hotmail.com", "i@gmail.com"]
for email in emails:
    if "gmail" in email:
        print(email)

names = ["brendon", "larissa"]
domains = ["gmail", "hotmail"]

for name, domain in zip(names, domains):
    print(name + "@" + domain + ".com")
