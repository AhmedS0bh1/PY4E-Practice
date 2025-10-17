try:
    handle = open("mbox.txt")
except:
    print("File not found.")
    quit()
emails = dict()
domains = dict()
hours = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        items = line.split()
        email = items[1]
        domain = items[1].split("@")[1]
        hour = int(items[5].split(":")[0])
        emails[email] = emails.get(email,0)+1
        domains[domain] = domains.get(domain,0)+1
        hours[hour] = hours.get(hour,0)+1

hours_tuples = list(hours.items())
hours_tuples.sort(key = lambda t:t[1],reverse=True)
top_sender = max(emails.items(),key=lambda x:x[1])
top_domain = max(domains.items(),key=lambda x:x[1])
print(f"Top sender: {top_sender[0]} ({top_sender[1]} emails)\nTop domain: {top_domain[0]} ({top_domain[1]} emails)")
print("-" * 40)
print(f"Emails by hour:")
for (hour,count) in hours_tuples:
    if hour < 10:
        print(0,end="")
    print(f"{hour} - {count}")