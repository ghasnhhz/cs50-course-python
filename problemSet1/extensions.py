fileType = input("File name: ")

if ".gif" in fileType:
  print("image/gif")
elif ".jpg" in fileType or "jpeg" in fileType:
  print("image/jpeg")
elif ".png" in fileType:
  print("image/png") 
elif ".pdf" in fileType:
  print("application/pdf")
elif ".txt" in fileType:
  print("text/plain")
elif ".zip" in fileType:
  print("application/zip")
else: 
  print("application/octet-stream")