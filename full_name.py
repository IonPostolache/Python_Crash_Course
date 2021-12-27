"""
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
"""

first_name="ada"
last_name="lovelace"
#print(f"{first_name} {last_name}")
full_name=f"{first_name.title()} {last_name.title()}"
print(full_name)
print(f"Hello, {full_name}!")

message=f"Fello, {full_name.title()}!"
print(message)

print("Languages \nPython\n\tC\n\tJavascript")

favourite_language='python'
print(f"{favourite_language}added")
favourite_language='python '
print(f"{favourite_language} added")
favourite_language=favourite_language.rstrip()
print(f"{favourite_language}added")

favourite_language=' python '
print(f"{favourite_language}added")
favourite_language=favourite_language.lstrip()
print(f"{favourite_language}added")
