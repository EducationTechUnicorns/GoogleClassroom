import os
import sys
file_alunos = open("alunos2021.csv", "r")
alunos2021_list = file_alunos.readlines()
file_google = open("GoogleUsers.csv", "r")
google_list = file_google.readlines()
list_diff = list(set(alunos2021_list).difference(google_list))
textfile = open("result.csv", "w")
for element in list_diff:
    textfile.write(element)
textfile.close()
