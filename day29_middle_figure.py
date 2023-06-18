def middle_figure(s1,s2):
    s3 = s1 + s2
    if len(s3) % 2 != 0:
        index = int(len(s3)/2)
        return s3[index]
    return 'no middle figure'

print(middle_figure('make love','not wars'))