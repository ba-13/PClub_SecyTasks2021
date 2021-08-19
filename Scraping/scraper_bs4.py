from bs4 import BeautifulSoup
import csv
import time

url = "https://hello.iitk.ac.in/esc201a21/#/home"
print("Please paste Course HomePage HTML Code in \"./input.html\" and then move furthur:")
for i in range(3):
    print(".", end='')
    time.sleep(1)
input("Done?(y/n) ")
if input == 'y' or input == 'Y':
    print("Update and re-run.")
    exit()
print("")
n = int(input("Enter the Number of Latest Lectures you need to Analyze: "))
move = input(f"Want to Modify URL from \"{url[:-6]}\"?(y/n): ")
if move == "y" or move == "Y":
    url = input(
        "Paste the Course Home Page URL (e.g.\"https://hello.iitk.ac.in/esc201a21/#/home\"): ")
print("Remember that wrong input leads to wrong output :P")

with open("./input.html", 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")

allLectureNames = [i.contents[0].strip()
                   for i in soup.select(".lectureInfoBoxText")]
if len(allLectureNames)-n < 0:
    print("You really want more Lectures?")
    exit()

requiredLectures = [(len(allLectureNames)-n+i, allLectureNames[len(allLectureNames)-n+i])
                    for i in range(n)]


def duration(i):
    return soup.select(".lectureInfoBoxText")[i].find_next_sibling("div").contents[2].contents[0]


def link(i):
    # url[:-6] to remove "#/home" from pasted URL
    return url[:-6] + soup.select(".lectureInfoBoxText")[i].parent.parent.attrs["href"]


def weekNumber(i):
    return soup.select(".lectureInfoBoxText")[i].parent.parent.parent.parent.parent.parent.parent.parent.contents[1].contents[3].contents[0].strip()


print("....writing to \"scrapeLectureDetails.csv\"")

with open("scrapeLectureDetails.csv", "w") as f:
    writer = csv.writer(f)
    for i, name in requiredLectures:
        writer.writerow([i+1, duration(i), weekNumber(i), name, link(i)])

print("....Done!")
