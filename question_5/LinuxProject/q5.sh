# Display the contents of text.txt 
cat text.txt

# Append the following text to text.txt
echo "\nLet's learn Linux\n" >> text.txt

# Count Number of lines in text.txt
wc -l text.txt

# Search for the word "Love" in text.txt and display the lines containing it.
grep "Love" text.txt

# Replace "Make" with "Do".
sed 's/Make/Do/g' text.txt

# Display only the third word from each line in text.txt.
awk '{print $3}' text.txt

# Count the number of words in each line.
awk '{print NF}' text.txt
