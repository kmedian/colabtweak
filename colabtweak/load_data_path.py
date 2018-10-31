
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials


# Colab Boilerplate to download data from G Drive
def load_data_path(folder_id, colab_path='/root/data/', local_path='../data/'):
    """Boilerplate to download data from Google Drive into Colab
    notebook or to point to local data folder

    Behavior:
    ---------
    1. Identify if Notebook is running in Colab
    2. If Yes, then
        a. do Google OAuth login (requires user interaction)
        b. create a data folder in Colab (colab_path)
        c. Search for all CSV files in Google Drive folder
        d. Copy all CSV files from G Drive into colab_path folder
        e. Return the colab_path variable
    3. If No, then
        a. Return the local_path variable

    Example 1:
    ----------
        !pip install colabtweak
        from colabtweak import load_data_path
        folder_id = "kasdhkfhjkashfjadskjfjsalk"
        data_path = load_data_path(folder_id)

        import pandas as pd
        df = pd.read_csv(data_path + "train.csv")
        df.head()

    Example 2:
    ----------
        !pip install colabtweak
        from colabtweak import load_data_path
        folder_id = "kasdhkfhjkashfjadskjfjsalk"
        colab_path = "/root/somecustomfolderincolab/"
        local_path = "../localsiblingprojectfolder/
        data_path = load_data_path(
            folder_id, colab_path=colab_path, local_path=local_path)

    """

    if os.getcwd() == '/content':  # Not a very clever way to identify Colab
        print("Notebook is running in Colab")

        if folder_id is None:
            print((
                "Folder ID is missing.\n"
                "Click on the Google Drive folder and check your URL\n"
                "'https://drive.google.com/drive/u/0/folders/<folder_id>'"))

        # Login
        auth.authenticate_user()
        gauth = GoogleAuth()
        gauth.credentials = GoogleCredentials.get_application_default()
        drive = GoogleDrive(gauth)

        # create "~/data" folder within the Colab image
        download_path = os.path.expanduser(colab_path)
        try:
            os.makedirs(download_path)
        except FileExistsError:
            pass

        # Extract the FileIDs from the Google Drive directory
        querystr = "title contains '.csv' and '" + folder_id + "' in parents"
        listed = drive.ListFile({'q': querystr}).GetList()

        # Copy all files
        for file in listed:
            print('{} {}'.format(file['id'], file['title']))
            output_file = os.path.join(download_path, file['title'])
            temp_file = drive.CreateFile({'id': file['id']})
            temp_file.GetContentFile(output_file)

        # Set directory path
        return colab_path

    else:
        print("Notebook is running in Jupyter")
        return local_path
