text = input("Enter the string: ")
sep = input("Enter the separator: ")
maxsplit = input("Enter the maximum number of splits (leave blank for all): ")

maxsplit = int(maxsplit) if maxsplit else -1

parts = []
splits_done = 0

while maxsplit != 0:
    pos = text.rfind(sep)
    if pos == -1:
        break

    parts.append(text[pos + len(sep):])
    text = text[:pos]

    splits_done += 1
    if maxsplit > 0 and splits_done >= maxsplit:
        break

parts.append(text)
parts.reverse()

print(f"Splitted text: {parts}")