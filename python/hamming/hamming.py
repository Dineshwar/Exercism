def distance(strand_a, strand_b):
    ans = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('Both string not equal.')
    else:
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                ans += 1
    return ans
