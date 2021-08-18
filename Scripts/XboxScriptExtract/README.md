# Python script to extract files from the Xbox games
## (Tested with ULTRAMIX2 through UNIVERSE2)
### These scripts all do the same thing. Their only difference is what game data file they look for. 

# Instructions
0. These instructions assume you've already dumped your game and extracted the files.
1. Copy `x_data_US.bin` (for ULTRAMIX 2 or 3)  **or** `x_data_XBOX_US.bin` for ULTRAMIX 4) **or** `x_data_XENON_US.bin` (for UNIVERSE games) from the game files to a folder of your choice.
2. Copy the appropriate script from this GitHub over to the same folder.
3. Create a new file with a `.csv` extension in the same folder, and title it `ExtractInfo.csv`.
4. Create a folder named `ExtractData` in the same folder.
5. From the game files, Open `x_data_US.hbn` **or** `x_data_XENON_US.hbn` (depending on game) in Excel or a similar program.
6. Add two new columns between column A and column B
7. Put the formula `=BASE(D4;16)` in the new, blank `B4` cell
8. Click the square in the lower right corner of the cell, and drag across to column D to copy the formula across.
9. With the formulas in `B4` and `C4` selected, click the box in the lower-right corner of `C4`, and drag to the last filled row of the document.
	* The document may have more rows without content. Copying the formula into these rows has no use, since there's nothing in the rows for the formulas to work off of.
10. Open the CSV file created in step 3 in a text editor (preferably Notepad++ or similar).
11. From the rows containing the files you would like to extract, copy the cells from columns A-C. 
12. Paste the cells into `ExtractInfo.csv` within the text editor used in Step 10.
13. Replace any TAB spaces with commas if needed.
	* For Notepad++, select one of the TAB spaces and hit CTRL+F. That will bring up the Find/Replace dialog with the TAB already in the "Find what:" box.
14. Add a line at the top of the document, and put the text `fnameext,offset,length` in that line.
15. Open up a command prompt to the folder (typing in `cmd` in the address bar at the top is a quick way to do this).
16. Type in the full name of the script for the appropriate game and press Enter.

### If everything was done correctly, congratulations! Your files are now extracted!
### Make sure to move the files out of the folder before extracting from another game!

## Troubleshooting
* If the files aren't created, check to make sure everything is named correctly.
* If the files aren't readable or otherwise don't contain the right content, check the CSV file to make sure that the information in there is correct.

## Any questions or issues should be reported under "Issues" at the top of this repository.