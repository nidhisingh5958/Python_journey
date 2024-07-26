def capitalize_sentence():
             f1 = open("test.txt", 'r')
             f2 = open("file1.txt", 'w')
             while 1:
                          line = f1.readline()
                          if not line:
                                       break
                          line = line.rstrip()
                          lineLength = len(line)
                          str=' '
                          str=str+ line[0].upper()
                          i=1
                          while i< lineLength:
                                       if line[i] == ".":
                                                    srt = str + line[i]
                                                    i = i +1

                                                    if i>= lineLength:
                                                                 break
                                                    str = str+ line[i].upper()
                                       else:
                                                    str = str+ line[i]
                                       i=i+1
                          f2.write(str)
             else:
                          print("Source file does not exist")
             f1.close()
             f2.close()

capitalize_sentence()
