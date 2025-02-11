# Extract Pressbook Info

## Clone this repository

Click the green "Code" button on the homepage, download as ZIP, and save the .zip folder

Then, extract all contents into a folder you want to keep these files

## Downloading the Book:

Export your Pressbook as html
- Log in to Pressbooks, choose the Pressbook to export
- Go to the "Export" tab
- Check "XHTML" in the "Other Formats" column and click "Export your Book"

Rename the download as `book.html`

Ensure `book.html` is located in the same folder as .py files from Step 1

## Running the Program:

Copy the path of the folder you just created to your clipboard
- Trick: Using your File Explorer, click the folder path on the top to copy it as text

Open Command Prompt (Windows) or Terminal (Mac)
	
In the command prompt, navigate to the folder with `book.html` and .py files from Step 1
- Enter the following command to navigate to your folder: `cd "path\to\folder"`
- Example: `cd "C:\Users\yourname\Desktop\VCU\Extract_PB_Info"`

Run the programs
- Enter the following command to extract hyperlinks: `python extractLinks.py`
- Enter the following command to extract alt text: `python extractAlt.py`
- Enter the following command to extract embedded content: `python extractEmbeds.py`

These commands create .csv files with the corresponding information. Open them to view your Pressbook contents!

