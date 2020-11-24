import os


# Data Files renaming for easier understanding
def rename_files(notags_folder, newtags_folder):
    print("Start renaming!")
    for count, filename in enumerate(os.listdir(notags_folder)):
        dst = "nt" + str(count) + ".jpg"
        src = notags_folder + '\\' + filename
        dst = notags_folder + '\\' + dst
        # rename all the files
        os.rename(src, dst)

    for count, filename in enumerate(os.listdir(newtags_folder)):
        dst = "t" + str(count) + ".jpg"
        src = newtags_folder + '\\' + filename
        dst = newtags_folder + '\\' + dst
        # rename all the files
        os.rename(src, dst)
    print("Renaming files completed!")


if __name__ == "__main__":
    notags_folder = r"C:\Users\User\Desktop\ML\Notags"
    newtags_folder = r"C:\Users\User\Desktop\ML\Newtags"
    rename_files(notags_folder, newtags_folder)
