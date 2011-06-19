750-to-org, version 0.2, released 2011-06-19

750-to-org takes the monthly files you can export from 750words.com
and converts them for use with emacs org-mode.

Requirements:

750-to-org should work with either Python 2 or 3, but is written for
and tested against Python 3.2.

Usage:

Keep this script in the directory with the org-mode file containing
your entries (if you have one already). This file should be called
'750.org'. Place into that same directory the export file, called
'750'. Then, just execute the script. If all goes well, the new entries
will be appended to 750.org. The file will be created if it does not
exist.

750-to-org places the wordcount and minutes-to-completion of each entry
in a :PROPERTIES: drawer at the top of the entry.

750-to-org was created by Tracy Poff <tracy.poff@gmail.com>. Contact
the author with any questions, problems, or suggestions. This version
has received little testing, so problems are not unexpected.

750-to-org is Free Software, licensed under the GNU GPL, version 3 or
later. The full license is included in the file LICENSE.txt.
