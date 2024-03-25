import subprocess
import urllib.parse
import shlex

query = input("Question: ")

encodedquery = urllib.parse.quote(query)
command = f"curl -X 'GET' 'http://127.0.0.1:8000/lamini?question={encodedquery}' -H 'accept: application/json'"

args = shlex.split(command)
process = subprocess.Popen(
    args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
stdout, stderr = process.communicate()
print(stdout)
