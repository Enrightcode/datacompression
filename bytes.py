def encodeFile (filename, newfilename):
  with open (filename) as f:
    data = encodeString(f.read())
  output = bytearray()
  for item in data:
    #characterbyte
    output.extend(item[1].to_bytes(1, 'big'))
  with open(newFilename, 'wb') as binary_file:
    #Write bytes to file
    binary_file.write(output)
    
def decodeFile(filename):
    with open(filename, 'rb') as f:
      data = f.read()
      #split data into pairs
      bytePairs = [data[i:i+2] for i in range(0, len(data), 2)]
      encodedList = []
      for bytePair in bytePairs:
        encodedList.append((bytePair[:1],decode('utf-8'), int.from_bytes(bytePair[1:], 'big')))
      return decodeString(encodedList)
    
    
