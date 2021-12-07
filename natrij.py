ch, cm, cs = [int(_) for _ in input().split(':')]
eh, em, es = [int(_) for _ in input().split(':')]
if es < cs:
	es += 60
	em -= 1
if em < cm:
	em += 60
	eh -= 1
if eh < ch:
	eh += 24
if eh-ch or em-cm or es-cs:
	print('%02d:%02d:%02d' % (eh-ch, em-cm, es-cs))
else:
	print('24:00:00')
