def fileToList(filename):
	lines = []
	try:
		fin = open(filename, 'r')
	except:
		return []
	for line in fin:
		lines.append(line.strip())
	fin.close()	
	return lines


def returnFirstString(strings):
	try:
		return strings[0]
	except:
		return ''


def strandsAreNotEmpty(strand1, strand2):
	if len(strand1) > 0 and len(strand2) > 0:
		return True


def strandsAreEqualLengths(strand1, strand2):
	if len(strand1) == len(strand2):
		return True


def candidateOverlapsTarget(target, candidate, overlap):
    

def findLargestOverlap(target, candidate):
	#if strandsAreNotEmpty(target, candidate) and strandsAreEqualLength(target, candidate):
	#	largest = 0
	#	for i in range(len(target)):
	#		
	#else:
	#	return -1	
	pass

def findBestCandidate(target, candidate):
	pass


def joinTwoStrands(target, candidate, overlap):
	if len(candidate) == 0:
		return target
	else:
		return target + candidate[overlap:]

#def main():

