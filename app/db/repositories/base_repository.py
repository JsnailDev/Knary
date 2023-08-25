from peewee import *


class BaseRepository:
    # Initialize the repository with a model class
    def __init__(self, model_class: Model):
        self.model_class = model_class

    # Define a method to create a new record
    def create(self, **kwargs):
        return self.model_class.create(**kwargs)

    # Define a method to get a record by id
    def get_by_id(self, id) -> Model:
        return self.model_class.get_by_id(id)

    # Define a method to get all records
    def get_all(self):
        return self.model_class.get()

    # Define a method to update a record by id
    def update_by_id(self, id, **kwargs):
        return (
            self.model_class.update(**kwargs).where(self.model_class.id == id).execute()
        )

    # Define a method to delete a record by id
    def delete_by_id(self, id):
        return self.model_class.delete().where(self.model_class.id == id).execute()
