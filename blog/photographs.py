"""
    This is a program to convert from instagram pics to photography page
    Into HTML stuff for generating photography.html
    WINDOWS ONLY
    To run on unix systems, replace 'pip' with 'pip3'
    Uses https://github.com/rarcega/instagram-scraper for scraping instagram
"""

import argparse
import os
from random import shuffle

# Downloads all posts made by user and stores them in folder 'username'
def download(username):
    try:
        os.system('instagram-scraper {}'.format(username))
    except:
        os.system('pip install instagram-scraper')
        os.system('instagram-scraper {}'.format(username))

# Function to get all images (jpg) stored in a folder (username == path)
def get_files(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))

    shuffle(files)
    return files

# Function to generate HTML for each picture
def post(file):
    html = '''<article class="brick entry format-standard animate-this">
        <div class="entry-thumb">
            <img src="{}">                   
        </div>
    </article> 
    <!-- end article -->
    '''.format(file)

    return html
    
def main(username):
    download(username)
    files = get_files(username)

    html = '\n'.join(open('templates/header_photos.txt', 'r').readlines())

    print("Generating HTML")
    for i in files:
        html += post(i)

    html += '\n'.join(open('templates/footer.txt', 'r').readlines())

    fh = open("photography.html", 'w')
    fh.write(html)
    fh.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates HTML for photographs page')
    parser.add_argument('username', help='Username to generate HTML for', default='the_real_naimish')
    args = parser.parse_args()
    main(args.username)
    print("Completed.")