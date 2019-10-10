# -*- coding: utf-8 -*-
import re
def sen(d):
	if "..." in d: d = d.replace("...","/neos//neos//neos/")
	d=re.sub("([.!?])"+"[\\\\]","/neos/\\\\",d)
	d=re.sub("[!]"+"[!]"+"[!]","/neos2//neos2//neos2//eos/",d)
	d=re.sub("[!]"+"[,]","/neos2/,",d)
	d=re.sub("[?]"+"[,]","/neos3/,",d)
	d=re.sub("[\"]"+"[!]"+"[.]","/neos2/\".",d)
	d=re.sub("[\"]"+"[?]"+"[.]","/neos3/\".",d)
	d=re.sub("(Jan|Feb|Mar|Apr|Aug|Sep|Oct|Nov|Dec|Mr|Mrs|Ms|Dr|St|Prof|Lt|Tech|Sc|Com|Rs|Ltd|Hi|LTD|Inc|INC|www|No|Co|Mt|Ref|Corp|Sci| no| vs| etc| rs| ex)[.]"+"[\s]"+"([a-z0-9])","\\1/neos/ \\2",d)
	d=re.sub("[.]"+"([A-Z])","/neos/\\1",d)
	d=re.sub("([aApP])"+"[.]"+"([mM])"+".","\\1/neos/\\2/neos/",d)
	d=re.sub("([^a-zA-Z'])"+"([a-zA-Z])"+"[.]","\\1\\2/neos/",d)
	d=re.sub("([^a-zA-Z])"+"[.]"+"([0-9])","\\1/neos/\\2",d)
	d=re.sub("(^\s)"+"[.]"+"(^\s)"+"[.](com|net|in|gov|ac|org)"+" ","\\1/neos/\\2/neos/\\3 ",d)
	d=re.sub("[.](com|net|in|gov|ac|org)","/neos/\\1",d)
	d=re.sub(" e\.g\."," e/neos/g/neos/",d)
	d=re.sub(" i\.e\."," i/neos/e/neos/",d)
	d=re.sub("([a-zA-Z])"+"(/neos/)"+"([a-zA-Z])"+"[.]","\\1\\2\\3/neos/",d)
	d=re.sub("([.]|[!]|[?])"+"\"","\"\\1/eos/",d)
	d=re.sub("([.]|[!]|[?])","\\1/eos/",d)
	d=re.sub("/neos/",".",d)
	d=re.sub("/neos2/","!",d)
	d=re.sub("/neos3/","?",d)
	d=d.split("/eos/")

	l=[]
	for i in range(len(d)):
		d[i]=d[i].strip()
		if not d[i]:
			continue
		d[i]=re.sub("([\"”])"+"([.]|[!]|[?])","\\2\\1",d[i])
		l.append(d[i])
	return l