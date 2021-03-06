# Copyright 2011 Tracy Poff <tracy.poff@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import re
import os
import sys

def main(infile="750", outfile="750.org"):
    try:
        with open(infile, 'rb') as f:
            text = f.read().decode('utf_8')
    except IOError:
        print("Couldn't read input file! Please check if you have the right path.", file=sys.stderr)
        return

    entries = text.split("##### ENTRY ##### ")
    del entries[0]

    num_words_regex = "num_words:(\d+),"
    num_minutes_regex = "num_minutes:(\d+\.\d+)\n"

    # After the next line, the members of entries are tuples containing
    # the entry's date, the number of words, the number of minutes it
    # took to write, and the entry text, in that order. That is:
    # (DATE, WORDS, MINUTES, TEXT)
    entries = [(datetime.datetime.strptime(entry[0:10], "%Y-%m-%d"),
                int(re.search(num_words_regex, entry).group(1)),
                float(re.search(num_minutes_regex, entry).group(1)),
                entry[entry.find("\n") + 1:])
               for entry in entries]

    orgtext = ""
    # Include the year heading if it's January, or if we're creating the
    # file for the first time.
    if entries[0][0].month is 1 or not os.path.exists("750.org"):
        orgtext += "* " + str(entries[0][0].year) + "\n"
    orgtext += "** " + entries[0][0].strftime("%Y-%m %B") + "\n"
    for entry in entries:
        orgtext += "*** " + entry[0].strftime("%Y-%m-%d %A") + "\n"
        orgtext += ":PROPERTIES:\n"
        orgtext += ":WORD_COUNT: " + str(entry[1]) + "\n"
        orgtext += ":MINUTES: " + str(entry[2]) + "\n"
        orgtext += ":END:\n"
        orgtext += entry[3]

    try:
        with open(outfile, "ab") as f:
            f.write(orgtext.encode("utf_8"))
    except IOError:
        print("Couldn't write to " + outfile + "!", file=sys.stderr)
        return

    print("Added entries for " + entries[0][0].strftime("%B") + " to " + outfile + ".")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main()
