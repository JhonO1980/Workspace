import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3


# Print data from form function (method)

def enterData():
    try:

            artist = artistEntry.get()
            album = albumEntry.get()
            barcode = barcodeDateEntry.get()


            if artist and album and barcode:

                albumYear = albumYearEntry.get()
                releaseYear = releaseYearEntry.get()

                if albumYear.isdigit() and releaseYear.isdigit():

                    release = releaseEntry.get()
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

                    conn = sqlite3.connect('cd_database.db', timeout=2)

                    table_create_sql =  '''
                                        CREATE TABLE IF NOT EXISTS cd_data 
                                        (
                                            artist              VARCHAR(255) NOT NULL,
                                            album               VARCHAR(255) NOT NULL,
                                            barcode             VARCHAR(255) NOT NULL,
                                            release             VARCHAR(255) NOT NULL,
                                            album_year          INTEGER(4),
                                            release_year        INTEGER(4),
                                            nr_discs            INTEGER(3),
                                            in_musicbrainz      VARCHAR(1),
                                            flac_archive        VARCHAR(1),
                                            flac_files          VARCHAR(1),
                                            ogg_files           VARCHAR(1),
                                            metadata_from       VARCHAR(255),
                                            file_name           VARCHAR(255),
                                            file_location       VARCHAR(255),
                                            medium              VARCHAR(255),
                                            UNIQUE (artist, album, barcode)
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
                                            release,
                                            album_year,
                                            release_year,
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
                                            ?,
                                            ?
                                        )
                                        '''
                    data_insert_tuple = (artist, album, barcode, release, albumYear, releaseYear, nrOfDiscs, inMusicBrainz, 
                                        flacArchive, flacFiles, oggFiles, metadataFrom, filename, fileLocation, fileMedium)
                    cursor = conn.cursor()
                    cursor.execute(data_insert_sql,data_insert_tuple)

        # Print data

                    print("Artist: ", artist)
                    print("Album: ", album)
                    print("Barcode: ", barcode)
                    print ("Release: ", release)
                    print("Album Year: ",albumYear)
                    print("Release Year: ", releaseYear)
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
                    tkinter.messagebox.showwarning(title= "Error", message="Album Year and Release Year must be numbers." )
            else:
                    tkinter.messagebox.showwarning(title= "Error", message="Artist, Album and Barcode are required." )

    except sqlite3.Error as error:
                tkinter.messagebox.showwarning(title= "Error", message= error )

    finally:
        conn.commit()
        conn.close

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


releaseLabel = tkinter.Label(cdInfoFrame, text="Release")
releaseLabel.grid(row=5, column=0)
releaseEntry = tkinter.Entry(cdInfoFrame, width=67)
releaseEntry.grid(row=6, column=0)


for widget in cdInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=4, sticky="w")

# Saving CD Details

cdDetailsFrame =tkinter.LabelFrame(frame, text="CD Details")
cdDetailsFrame.grid(row=1, column=0, sticky="news", padx=20, pady=0)

albumYearLabel = tkinter.Label(cdDetailsFrame, text="Album Year")
albumYearLabel.grid(row=0, column=0)
albumYearEntry = tkinter.Entry(cdDetailsFrame)
albumYearEntry.grid(row=1, column=0)


releaseYearLabel = tkinter.Label(cdDetailsFrame, text="Release Year")
releaseYearLabel.grid(row=0, column=1)
releaseYearEntry = tkinter.Entry(cdDetailsFrame)
releaseYearEntry.grid(row=1, column=1)

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
