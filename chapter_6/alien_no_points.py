alien_0={'color':'green', 'speed':'slow'}
#print(alien_0['points'])

non_existent_value=alien_0.get('points', 'Points value is not assigned.')
#non_existent_value=alien_0.get('points', )
print(non_existent_value)
