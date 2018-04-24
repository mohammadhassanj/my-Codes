from lxml import etree
from requests import get
import sys
import os

url_for_get_id = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&field=title&term=\"{}\""
url_for_get_title = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={}&retmode=XML"

def xml_id_or_title_extractor(page):

   """extract the ids from page and return that as string"""

   content = etree.fromstring(page)
   root = content.getroottree()
   result = [item.text for item in root.xpath(xpath)]
   if len(result)<1:
       return "Not Found!!"
   return ",".join(result)

def write_to_file(_list):

    result = open("title_pubmedid_result.txt","a")

    for title in _list:
        try:
            title = title.strip()
            page = get(URL.format(title)).content
            _id = xml_id_or_title_extractor(page)
            result.write(_id + "\t" + title + "\n")
            print (title,"===>","OK")
        except:
            print("An Exception occurred!! on \n <{}>".format(title))
            result.write("ERROR" + "\t" + title + "\n")
    result.close()

def run(title_list):

    if len(sys.argv) > 2:
        path = os.getcwd()
        file_path = path+"/"+sys.argv[2]
        try:
            read_file = [item.strip() for item in open(file_path).readlines()]
            write_to_file(read_file)
        except FileNotFoundError:
            print ("your file is not exsists or input file not in same directory")
        except:
            print ("there is a problem with your input file")
    else:
        write_to_file(title_list)


if __name__ == "__main__":

    print ("the script is running\n")
    print ("this is a script to convert article paper to pubmedid and vice versa")
    print ("*"*20)

    if len(sys.argv)<2:
        print ("\nyour arguments are not enough !!\n \n Use this format : for example \n\n< python pubmedid_to_title.py -t2id your_file.txt> for reading from file\n\n\
        or \n\n< python pubmedid_to_title.py -t2id> for reading from a list")
        sys.exit()
    elif sys.argv[1] == "-t2id":
        URL = url_for_get_id
        xpath = "//Id"
        _id_or_title_list = ["Differentially Expressed miRNAs in Hepatocellular Carcinoma Target Genes in the Genetic Information Processing and Metabolism Pathways.",
        "miR-429 inhibits migration and invasion of breast cancer cells in vitro."]

    elif sys.argv[1] == "-id2t":
        URL = url_for_get_title
        xpath = "//ArticleTitle"
        _id_or_title_list = ["18456660","19196975"]
    else:
        print ("use -id2t for convert id to title or -t2id for convert title to id as first argument!! ")
        sys.exit()
    # suppose you have a list of paper's title, for example two titles or two id ==> _id_or_title_list list
    # you can edit it ...

    # if you wnat to read from a file, your file name come after it, be careful the script and file directory must be in same directory
    # also each line should be just one title
    # for example type this:
    # python title_to_pubmedid.py -t2id your_file.txt
    # first argument must be -t2id for convert titles to ides and -id2t for reverse search
    #SO YOU HAVE TWO CHICE: 1:READ FROM FILE 2:EDIT THE ABOVE LIST :D
    run(_id_or_title_list)
