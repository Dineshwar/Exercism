def distance(strand_a, strand_b):
    try:
        if strand_a and strand_b:
            if strand_a.count() == strand_b.count():
                cou = 0
                for i in strand_a.count():
                    if not strand_a[i]==strand_b[i]:
                        cou+=1
                return cou
		else:
			raise ValueError('Two strings length not equal')
    except Exception as error:
        raise ValueError('Two strings length not equal')