thing = 'woodchunk'
print('{}'.format(thing))

thing = 'woodchunk'
place = 'lake'
pr = 'The {} is in the{}.'.format(thing, place)
print(pr)

pr = 'The {1} is in the{0}.'.format(thing, place)
print(pr)

pr = 'The {thing} is in the {place}'.format(thing='duck', place='bathtub')
print(pr)

d = {'thing': 'duck', 'place': 'bathub'}
pr = 'The {0[thing]} is in the{0[place]}.'.format(d)
print(pr)

thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
print('The wraith is at the window')
print('The {:10s} is at the {:10s}'.format(thing, place))
print('The {:<10s} is at the {:<10s}'.format(thing, place))
print('The {:^10s} is at the {:^10s}'.format(thing, place))
print('The {:>10s} is at the {:>10s}'.format(thing, place))
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))