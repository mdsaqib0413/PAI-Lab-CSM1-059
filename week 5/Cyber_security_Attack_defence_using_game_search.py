attacks = ["Phishing", "Malware"]
defenses = ["Firewall", "Antivirus"]

scores = {
("Phishing","Firewall"):1,
("Phishing","Antivirus"):-1,
("Malware","Firewall"):-1,
("Malware","Antivirus"):1
}

def minimax(depth, defender):
    if depth == 0:
        return 0
    if defender:
        best = -100
        for d in defenses:
            for a in attacks:
                val = scores[(a,d)] + minimax(depth-1, False)
                best = max(best, val)
        return best
    else:
        best = 100
        for a in attacks:
            for d in defenses:
                val = scores[(a,d)] + minimax(depth-1, True)
                best = min(best, val)
        return best

print("Optimal Security Outcome Score:", minimax(2, True))
