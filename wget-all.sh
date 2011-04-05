#!/usr/bin/bash
url=$1 # url from to download the files
docname=$2 # name of the pdfs that repeat without the number
doctype=$3 # type of document
pdfcount=$4 # number of pdfs/chapters
counter=1
while [[ $counter -le $pdfcount ]]; do
	wget "$url/$docname$counter.$doctype"
	counter=$(( $counter + 1 ))
done
