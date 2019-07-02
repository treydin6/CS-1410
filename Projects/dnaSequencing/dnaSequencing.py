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
    return target[-overlap:] == candidate[:overlap] 

def findLargestOverlap(target, candidate):
    largest = 0
    if target == candidate and len(target) > 0:
        return len(target)
    elif len(target) == len(candidate) and len(target) > 0:
        for i in range(len(target)):
            x = target[len(target) - i:]
            y = candidate[:i]
            if x == y:
                largest = i
        return largest
    else:
        return -1

def findBestCandidate(target, candidates):
    can = ''
    largest = 0
    for candidate in candidates:
        new = findLargestOverlap(target, candidate)
        if new > largest:
            largest = new
            can = candidate
    return can, largest

def joinTwoStrands(target, candidate, overlap):
	if len(candidate) == 0:
		return target
	else:
		return target + candidate[overlap:]

def main():
    tar = input('Target strand filename: ')
    validate = fileToList(tar)
    target = returnFirstString(validate)
    can = input('Candidate strands filename: ')
    candidate = fileToList(can)
    candidate, overlap = findBestCandidate(target, candidate)
    final = joinTwoStrands(target, candidate, overlap)
    print(final)


if __name__=='__main__':
    main()







