# Read from the file file.txt and output the tenth line to stdout.

# awk ' NR==10 {print NR ":" $0}' file.txt | cut -d : -f 2
# cat --number file.txt | grep 10 -m 1 | cut -f 2
# sad -n "10p" file.txt
awk ' NR==10 {print $0}' file.txt | cut -f 2
