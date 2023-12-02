import re

regex = "^Game ([1-9]|[1-9][0-9]|100):( (([1-9]|[1-9][0-9]) (blue|green|red)(, |))*(;|))*"
txt = "Game 2: 7 red, 1 green, 4 blue; 13 red, 11 blue; 6 red, 2 blue; 9 blue, 9 red; 4 blue, 11 red; 15 red, 1 green, 3 blue"

search = re.search(regex, txt)

print(search.group())

splitted = re.split(": |, |; ", txt)

print(splitted)
