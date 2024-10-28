import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3

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

cd_info_frame =tkinter.LabelFrame(frame, text="CD Information")
cd_info_frame.grid(row=0, columnspan=2, sticky="news", padx=20, pady=20)

artist_label = tkinter.Label(cd_info_frame, text="Artist")
artist_label.grid(row=0, column=0)
artist_entry = tkinter.Entry(cd_info_frame, width=67)
artist_entry.grid(row=1, column=0)


album_label = tkinter.Label(cd_info_frame, text="Album")
album_label.grid(row=3, column=0)
album_entry = tkinter.Entry(cd_info_frame, width=67)
album_entry.grid(row=4, column=0)

for widget in cd_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=4, sticky="w")

# Saving CD Details

cd_details_frame =tkinter.LabelFrame(frame, text="CD Details")
cd_details_frame.grid(row=1, column=0, sticky="news", padx=20, pady=0)

release_date_label = tkinter.Label(cd_details_frame, text="Release Date")
release_date_label.grid(row=0, column=0)
release_date_entry = tkinter.Entry(cd_details_frame)
release_date_entry.grid(row=1, column=0)


original_release_date_label = tkinter.Label(cd_details_frame, text="Original Release Date")
original_release_date_label.grid(row=0, column=1)
original_release_date_entry = tkinter.Entry(cd_details_frame)
original_release_date_entry.grid(row=1, column=1)

barcode_label = tkinter.Label(cd_details_frame, text="Barcode")
barcode_label.grid(row=0, column=2)
barcode_date_entry = tkinter.Entry(cd_details_frame)
barcode_date_entry.grid(row=1, column=2)


nrOfDiscsVar = tkinter.Variable(value=1)  # initial value
nrOfDiscsLabel =tkinter.Label(cd_details_frame, text="Number Of Discs")
nrOfDiscsLabel.grid(row=2,column=0)
nrOfDiscsSpinbox = ttk.Spinbox(cd_details_frame, from_= 1, to="infinity", textvariable= nrOfDiscsVar)
nrOfDiscsSpinbox.grid(row=3, column=0)


for widget in cd_details_frame.winfo_children():
    widget.grid_configure(padx=10, pady=4, sticky="w")

# Saving CD Status

cd_status_frame = tkinter.LabelFrame (frame, text="CD Status")
cd_status_frame.grid(row=2,column=0, sticky="news", padx=20, pady=20)


musicbrainz_check_var = tkinter.StringVar(value="N")
musicbrainz_check = tkinter.Checkbutton(cd_status_frame, text="In MusicBrainz?", variable=musicbrainz_check_var, onvalue="Y", offvalue="N")
musicbrainz_check.grid(row=0, column=0)


flac_archive_check_var = tkinter.StringVar(value="N")
flac_archive_check = tkinter.Checkbutton(cd_status_frame, text="FLAC Archive?", variable=flac_archive_check_var, onvalue="Y", offvalue="N")
flac_archive_check.grid(row=0, column=1)


flac_files_check_var = tkinter.StringVar(value="N")
flac_files_check = tkinter.Checkbutton(cd_status_frame, text="FLAC Files?", variable=flac_files_check_var, onvalue="Y", offvalue="N")
flac_files_check.grid(row=0, column=2)


ogg_files_check_var = tkinter.StringVar(value="N")
ogg_files_check = tkinter.Checkbutton(cd_status_frame, text="In Ogg Files?", variable=ogg_files_check_var, onvalue="Y", offvalue="N")
ogg_files_check.grid(row=0, column=4)


metaDataFromLabel =tkinter.Label(cd_status_frame, text="Metadata From:")
metaDataFromLabel.grid(row=1,column=0)
metaDataFromCombobox = ttk.Combobox(cd_status_frame, values=["MusicBrainz", "Discogs"])
metaDataFromCombobox.grid(row=2, column=0)

for widget in cd_status_frame.winfo_children():
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

button = tkinter.Button(frame, text="Enter data")
button.grid(row=4, column=0, pady=10)


window.mainloop()
