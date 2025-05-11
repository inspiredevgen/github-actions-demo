echo "### Executing script: $0"

mkdir -p /tmp/inspiredev/
echo "### Downloading files to /tmp/inspiredev/ ###"
wget https://mathcenter.oxford.emory.edu/site/math117/probSetAllTogether/words.txt

mv words.txt password.txt
echo "### Downloading complete ###"
echo "### Starting to process the file ###"
echo "### password with the word inspire ###"
cat password.txt | grep -i inspire
echo "### File content complete ###"