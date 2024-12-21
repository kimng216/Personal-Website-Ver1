# Personal-Website-Ver1

## Overview

This is the initial version of my personal website, designed to showcase my professional profile, skills, and contact information. The website includes clickable links to my LinkedIn, GitHub, LeetCode, resume, and email, with each section styled for a modern user experience.

## Features
**Clickable Images:** Each section (e.g., LinkedIn, GitHub, etc.) is presented as a clickable box that redirects to the respective links.

**Responsive Design:** The layout adjusts to different screen sizes using CSS flexbox properties.

**Interactive Hover Effects** Hovering over each box changes its background color and adds a shadow for a subtle interactive effect.

**Custom Image Styling:** Each box includes an icon/image styled specifically for this website.

## File Structure
project-folder/
├── app.py         
├── templates/
│   └── index.html     
├── static/ 
    ├── css/ 
        ├── styles.css  
        ├── cpp.png  
        ├── css.png  
        ├── csulb.png 
        ├── email-logo.png  
        ├── github-logo.png 
        ├── github.css  
        ├── haskell.png  
        ├── html.png  
        ├── leetcode-logo.png 
        ├── leetcode.png    
        ├── linkedin-logo.png 
        ├── linkedin.png 
        ├── person.jpg 
        ├── python.png 
        ├── r.png      
        ├── resume.png 
        └── sql.png   

## Prerequisites
- Python 3.8+
- Flask * *(if running the website locally)* *

## Installation and Usage
**Clone the repository:** 
git clone https://github.com/kimng216/Personal-Website-Ver1.git
cd Personal-Website-Ver1

**If using Flask, install the required dependencies:** 
pip install flask
**Run the Flask server:** 
python app.py
**Open the website in your browser:**
Local: http://127.0.0.1:5000
**Customization:**
Update the links in the index.html file to point to your personal profiles and resources:
<a href="https://www.linkedin.com/in/kimnguyencs/" target="_blank">
Replace the placeholder images in the static folder with your own icons.

## License
This project is open-source and available under the MIT License.
