import datetime
import re
import os

def main():
    try:
        with open('750', 'rb') as f:
            text = f.read().decode('utf_8')
    except IOError:
        print("Couldn't read file!")
        return

    entries = text.split("##### ENTRY ##### ")
    del entries[0]

    num_words_regex = "num_words:(\d+),"
    num_minutes_regex = "num_minutes:(\d+\.\d+)\n"

    # After the next line, the members of entries are tuples containing
    # the entry's date, the number of words, the number of minutes it
    # took to write, and the entry text, in that order. That is:
    # (DATE, WORDS, MINUTES, TEXT)
    entries = [(datetime.date(int(entry[0:4]), int(entry[5:7]), int(entry[8:10])), int(re.search(num_words_regex, entry).group(1)), float(re.search(num_minutes_regex, entry).group(1)), entry[entry.find("\n") + 1:]) for entry in entries]

    orgtext = ""
    # Include the year heading if it's January, or if we're creating the
    # file for the first time.
    if entries[0][0].month is 1 or not os.path.exists("750.org"):
        orgtext += "* " + str(entries[0][0].year) + "\n"
    orgtext += "** " + entries[0][0].strftime("%Y-%m %B") + "\n"
    for entry in entries:
        orgtext += "*** " + entry[0].isoformat() + " " + entry[0].strftime("%A") + "\n"
        orgtext += ":PROPERTIES:\n"
        orgtext += ":WORD_COUNT: " + str(entry[1]) + "\n"
        orgtext += ":MINUTES: " + str(entry[2]) + "\n"
        orgtext += ":END:\n"
        orgtext += entry[3]

    try:
        with open("750.org", "ab") as f:
            f.write(orgtext.encode("utf_8"))
    except IOError:
        print("Couldn't write to 750.org!")
        return

if __name__ == "__main__":
    main()
