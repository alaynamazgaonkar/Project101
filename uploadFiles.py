import dropbox, os

class TransferData:
    def __init__(self, access_token,file_from,file_to):
        self.access_token = access_token
        self.file_from = file_from
        self.file_to=file_to
        # self.local_path=local_path

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        new_path=os.path.join(local_path,file_from)
        dropbox_path=os.path.join(file_to,new_path)
    
        # f = open(file_from, 'rb')
        f = open(new_path, 'rb')
        dbx.files_upload(f.read(), dropbox_path)

# local_path="C:\Users\HP\Desktop\alayna\Python\Project101"
# file_from="text.txt"
# file_to="test/file"

local_path=input('Path for the file (local path) :- ')
file_from=input('Name of the file :- ')
file_to=input('Path for the dropbox :- ')

access_token = 'W4u4sYm7ULQAAAAAAAAAAZsa8wR5_OuIH8U3oR7FqU8NEZzTkUpTrshTnR--laX6'
transferData = TransferData(access_token,file_from,file_to)

transferData.upload_file(file_from, file_to)
print("file has been moved")