import facebook

token = 'EAANWR6mw9AUBANAkg99yGiZCnYRzeZCBuFpR5s3VW8LeZAZCW05MmBffSmNsd3ZArE9P4BOY6TtjrzJdeDWi0V0WFSFBDXx4mkPvRM78AnWRZA0Qt92mdI9YlAnLxSzeWatdcw10l7SfQmorQXWnYjCg81DSKX2bbumF7ByYkJZA8XLNr3VWT4pyTfCuM8xWbPV86BIeyIgZBwZDZD'

graph = facebook.GraphAPI(token)
#profile = graph.get_object("me/friends")
#friends = graph.get_connections("me", "friends")

#friend_list = [friend['name'] for friend in friends['data']]

#print (friends['data'])

friends = graph.get_object("me/friends")
for friend in friends['data']:
    print("{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id']))
'''
graph = facebook.GraphAPI(token)
friends = graph.get_object("me/friends")
for friend in friends['data']:
    print ("{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id']))
'''