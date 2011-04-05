#!/usr/bin/bash
url=$1 # url from to download the files
docname=$2 # name of the pdfs that repeat without the number
doctype=$3 # type of document
pdfcount=$4 # number of pdfs/chapters

# Usage printout
if [[ $# -ne 4 ]]; then
	echo "Usage"
	echo "====="
	echo "wget-all <url> <docname> <doctype> <doccount>"
	echo "url - the url of the page from where the docs are to be downloaded"
	echo "docname - the name of the doc without the chapter/sequence number"
	echo "doctype - the extension. (case sensitive)"
	echo "pdfcount - number of documents or end of sequence number"	
fi


counter=1
while [[ $counter -le $pdfcount ]]; do
	wget "$url/$docname$counter.$doctype"
	counter=$(( $counter + 1 ))
done
