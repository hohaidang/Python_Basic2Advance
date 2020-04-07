import sys

# try:
#     print(a)
# except NameError:
#     print("Name Error")
# except:
#     print("Error")

try:
  print(x)
except:
  print("Something went wrong")
finally:
    # Will print regardless of try is throw error or not
  print("The 'try except' is finished")
  sys.exit(1)

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()