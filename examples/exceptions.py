def parse_email(email):
    username, domain = email.split("@")
    if "." not in domain:
        raise ValueError(f"invalid domain: {domain}")
    return username, domain


addresses = [
    "anna.smith@example.com",
    "jane@smith@example.com",
    "john.oliver@test.com",
    "jamie.oliver@test",
    "mike.addamsatest.com",
]

for address in addresses:
    try:
        user, dom = parse_email(address)
    except ValueError as ex:
        print(f"Invalid address: {address} ({ex})")
    except SystemError:
        print("SystemError occurred!")
    else:
        print(user, dom)
    finally:
        print("Executes every time\n")
