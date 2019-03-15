class Entity(object):

    def __init__(self, my_class):
        # my_class has to be a class !
        self.id = my_class.id
        self.timestamp = my_class.timestamp
        self.event_type = my_class.event_type
        self.user_id = my_class.user_id


if __name__ == '__main__':
    my_class = ???
    entity = my_class.set...???

    assert entity.id == '298ffdc9-11a1-4ccd-b6ff-fcf4dffb7bd5'
    assert entity.timestamp == '2019-03-15T16:12:01'
    assert entity.event_type == 1
    assert entity.user_id == 'USER023'

    print('Well done !')        
   