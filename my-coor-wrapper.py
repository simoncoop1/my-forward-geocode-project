import os    

cmd = """./giqtrans --CGI='SourceSRID=27700&TargetSRID=4937&PreferredDatum=13&Geometry={"type":"Point","coordinates":[586500,245739,0]}'"""


#call = os.system("cat syscall_list.txt | grep f89e7000 | awk '{print $2}'")
call = os.system(cmd)
print(call)
