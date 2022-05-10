import cgi
form = cgi.FieldStorage()
with open ('photo.png','w') as fileOutput:
    fileOutput.write(form.getValue('UploadFile'))
