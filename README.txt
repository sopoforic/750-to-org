750-to-org, version 0.3, released 2011-06-20

750-to-org takes the monthly files you can export from 750words.com
and converts them for use with emacs org-mode.

Requirements:

750-to-org should work with either Python 2 or 3, but is written for
and tested against Python 3.2.

Usage:

python 750-to-org.py [INPUT] [OUTPUT]

If you do not provide paths to the input and output files, 750-to-org
looks in the current directory for a file called '750', and writes to
'750.org'.

750-to-org places the wordcount and minutes-to-completion of each entry
in a :PROPERTIES: drawer at the top of the entry.

750-to-org was created by Tracy Poff <tracy.poff@gmail.com>. Contact
the author with any questions, problems, or suggestions.

750-to-org is Free Software, licensed under the GNU GPL, version 3 or
later. The full license is included in the file LICENSE.txt.
