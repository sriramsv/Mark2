import subprocess

def say(phrase):
	subprocess.call("""espeak -v mb-en1 '{0}'""".format(phrase),shell=True)
