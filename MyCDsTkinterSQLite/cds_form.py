import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3


# Print data from form function (method)

def enterData():

    artist = artistEntry.get()
    album = albumEntry.get()
    barcode = barcodeDateEntry.get()


    if artist and album and barcode:

        releaseDate = releaseDateEntry.get()
        originalReleaseDate = originalReleaseDateEntry.get()

        if releaseDate.isdigit() and originalReleaseDate.isdigit():

            nrOfDiscs = nrOfDiscsSpinbox.get()
            inMusicBrainz = musicbrainzCheckVar.get()
            flacArchive = flacArchiveCheckVar.get()
            flacFiles = flacFilesCheckVar.get()
            oggFiles = oggFilesCheckVar.get()
            metadataFrom = metaDataFromCombobox.get()
            filename = filenameEntry.get()
            fileLocation = fileLocationEntry.get()
            fileMedium = fileMediumCombobox.get()

# Database and table creation

            conn = sqlite3.connect('cd_database.db')

            table_create_sql =  '''
                                CREATE TABLE IF NOT EXISTS cd_data 
                                (
                                    artist TEXT,
                                    album TEXT,
                                    barcode TEXT,
                                    release_date TEXT,
                                    og_release_date TEXT,
                                    nr_discs TEXT,
                                    in_musicbrainz TEXT,
                                    flac_archive TEXT,
                                    flac_files TEXT,
                                    ogg_files TEXT,
                                    metadata_from TEXT,
                                    file_name TEXT,
                                    file_location TEXT,
                                    medium TEXT
                                )
                                '''
            conn.execute(table_create_sql)

# Insert data in table

            data_insert_sql =   '''
                                INSERT INTO cd_data
                                (
                                    artist,
                                    album,
                                    barcode,
                                    release_date,
                                    og_release_date,
                                    nr_discs,
                                    in_musicbrainz,
                                    flac_archive,
                                    flac_files,
                                    ogg_files,
                                    metadata_from,
                                    file_name,
                                    file_location,
                                    medium
                                )
                                VALUES
                                (
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?
                                )
                                '''
            data_insert_tuple = (artist, album, barcode, releaseDate, originalReleaseDate, nrOfDiscs, inMusicBrainz, 
                                 flacArchive, flacFiles, oggFiles, metadataFrom, filename, fileLocation, fileMedium)
            cursor = conn.cursor()
            cursor.execute(data_insert_sql,data_insert_tuple)
            conn.commit()
            conn.close

# Print data

            print("Artist: ", artist)
            print("Album: ", album)
            print("Barcode: ", barcode)
            print("Release Date: ",releaseDate)
            print("Original Release Date: ", originalReleaseDate)
            print("Barcode: ", barcode)
            print("Number Of Discs: ", nrOfDiscs)
            print("In MusicBrainz?: ", inMusicBrainz)
            print("FLAC Arcvhive? ", flacArchive)
            print("FLAC Files?: ", flacFiles)
            print("oggFiles?: ", oggFiles)
            print("Metadata From: ", metadataFrom)
            print("Filename: ", filename)
            print("File Location: ", fileLocation)
            print("Medium: ", fileMedium)
        
        else:
            tkinter.messagebox.showwarning(title= "Error", message="Release Date and Original Release Date must be numbers." )
    else:
            tkinter.messagebox.showwarning(title= "Error", message="Artist, Album and Barcode are required." )


# Window

window = tkinter.Tk()
window.title("CD Status Form")

frame = tkinter.Frame(window)
frame.pack()


# Saving CD info

cdInfoFrame =tkinter.LabelFrame(frame, text="CD Information")
cdInfoFrame.grid(row=0, columnspan=2, sticky="news", padx=20, pady=20)

artistLabel = tkinter.Label(cdInfoFrame, text="Artist")
artistLabel.grid(row=0, column=0)
artistEntry = tkinter.Entry(cdInfoFrame, width=67)
artistEntry.grid(row=1, column=0)


albumLabel = tkinter.Label(cdInfoFrame, text="Album")
albumLabel.grid(row=3, column=0)
albumEntry = tkinter.Entry(cdInfoFrame, width=67)
albumEntry.grid(row=4, column=0)

for widget in cdInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=4, sticky="w")

# Saving CD Details

cdDetailsFrame =tkinter.LabelFrame(frame, text="CD Details")
cdDetailsFrame.grid(row=1, column=0, sticky="news", padx=20, pady=0)

releaseDateLabel = tkinter.Label(cdDetailsFrame, text="Release Date")
releaseDateLabel.grid(row=0, column=0)
releaseDateEntry = tkinter.Entry(cdDetailsFrame)
releaseDateEntry.grid(row=1, column=0)


originalReleaseDateLabel = tkinter.Label(cdDetailsFrame, text="Original Release Date")
originalReleaseDateLabel.grid(row=0, column=1)
originalReleaseDateEntry = tkinter.Entry(cdDetailsFrame)
originalReleaseDateEntry.grid(row=1, column=1)

barcodeLabel = tkinter.Label(cdDetailsFrame, text="Barcode")
barcodeLabel.grid(row=0, column=2)
barcodeDateEntry = tkinter.Entry(cdDetailsFrame)
barcodeDateEntry.grid(row=1, column=2)


nrOfDiscsVar = tkinter.Variable(value=1)  # initial value
nrOfDiscsLabel =tkinter.Label(cdDetailsFrame, text="Number Of Discs")
nrOfDiscsLabel.grid(row=2,column=0)
nrOfDiscsSpinbox = ttk.Spinbox(cdDetailsFrame, from_= 1, to="infinity", textvariable= nrOfDiscsVar)
nrOfDiscsSpinbox.grid(row=3, column=0)


for widget in cdDetailsFrame.winfo_children():
    widget.grid_configure(padx=10, pady=4, sticky="w")

# Saving CD Status

cdStatusFrame = tkinter.LabelFrame (frame, text="CD Status")
cdStatusFrame.grid(row=2,column=0, sticky="news", padx=20, pady=20)


musicbrainzCheckVar = tkinter.StringVar(value="N")
musicbrainzCheck = tkinter.Checkbutton(cdStatusFrame, text="In MusicBrainz?", variable=musicbrainzCheckVar, onvalue="Y", offvalue="N")
musicbrainzCheck.grid(row=0, column=0)


flacArchiveCheckVar = tkinter.StringVar(value="N")
flacArchiveCheck = tkinter.Checkbutton(cdStatusFrame, text="FLAC Archive?", variable=flacArchiveCheckVar, onvalue="Y", offvalue="N")
flacArchiveCheck.grid(row=0, column=1)


flacFilesCheckVar = tkinter.StringVar(value="N")
flacFilesCheck = tkinter.Checkbutton(cdStatusFrame, text="FLAC Files?", variable=flacFilesCheckVar, onvalue="Y", offvalue="N")
flacFilesCheck.grid(row=0, column=2)


oggFilesCheckVar = tkinter.StringVar(value="N")
oggFilesCheck = tkinter.Checkbutton(cdStatusFrame, text="Ogg Files?", variable=oggFilesCheckVar, onvalue="Y", offvalue="N")
oggFilesCheck.grid(row=0, column=4)


metaDataFromLabel =tkinter.Label(cdStatusFrame, text="Metadata From:")
metaDataFromLabel.grid(row=1,column=0)
metaDataFromCombobox = ttk.Combobox(cdStatusFrame, values=["MusicBrainz", "Discogs"])
metaDataFromCombobox.grid(row=2, column=0)

for widget in cdStatusFrame.winfo_children():
    widget.grid_configure(padx=10, pady=4, sticky="w")

# Saving Files

filesFrame =tkinter.LabelFrame(frame, text="Files")
filesFrame.grid(row=3, columnspan=2, sticky="news", padx=20, pady=0)

filenameLabel = tkinter.Label(filesFrame, text="Filename")
filenameLabel.grid(row=0, column=0)
filenameEntry = tkinter.Entry(filesFrame, width=67)
filenameEntry.grid(row=1, column=0)

fileLocationLabel = tkinter.Label(filesFrame, text="File Location")
fileLocationLabel.grid(row=2, column=0)
fileLocationEntry = tkinter.Entry(filesFrame, width=40)
fileLocationEntry.grid(row=3, column=0)

fileMediumLabel =tkinter.Label(filesFrame, text="Medium")
fileMediumLabel.grid(row=4,column=0)
fileMediumCombobox = ttk.Combobox(filesFrame, values=["Blu-ray", "CD-R","DVD-R","NAS","HDD"])
fileMediumCombobox.grid(row=5, column=0)

for widget in filesFrame.winfo_children():
    widget.grid_configure(padx=10, pady=4, sticky="w")

# Enter Data Button

button = tkinter.Button(frame, text="Enter data", command= enterData)
button.grid(row=4, column=0, pady=10)


window.mainloop()
