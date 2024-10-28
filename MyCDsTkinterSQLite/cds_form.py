import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3


# Print Data from Form Function (Method)

def enterData():
    artist = artistEntry.get()
    print("Artist: ", artist)

    album = albumEntry.get()
    print("Album: ", album)

    releaseDate = releaseDateEntry.get()
    print("Release Date: ",releaseDate)

    originalReleaseDate = originalReleaseDateEntry.get()
    print("Original Release Date: ", originalReleaseDate)

    barcode = barcodeDateEntry.get()
    print("Barcode: ", barcode)

    nrOfDiscs = nrOfDiscsSpinbox.get()
    print("Number Of Discs: ", nrOfDiscs)

    inMusicBrainz = musicbrainzCheckVar.get()
    print("In MusicBrainz?: ", inMusicBrainz)

    flacArchive = flacArchiveCheckVar.get()
    print("FLAC Arcvhive? ", flacArchive)

    flacFiles = flacFilesCheckVar.get()
    print("FLAC Files?: ", flacFiles)

    oggFiles = oggFilesCheckVar.get()
    print("oggFiles?: ", oggFiles)

    metadataFrom = metaDataFromCombobox.get()
    print("Metadata From: ", metadataFrom)

    filename = filenameEntry.get()
    print("Filename: ", filename)

    fileLocation = fileLocationEntry.get()
    print("File Location: ", fileLocation)

    fileMedium = fileMediumCombobox.get()
    print("Medium: ", fileMedium)


# Enter Data Function

'''
def enter_data():
    terms_accepted = terms_check_var.get()
    if terms_accepted=="Accepted":

        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Course info
            resgistration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("Registration status: ", resgistration_status)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
        else:
            tkinter.messagebox.showwarning(title= "Error", message="First name and last name are required." )
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms." )

'''

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
