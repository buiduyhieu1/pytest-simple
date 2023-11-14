""" This is a model for support the main script. """
import uuid


# pylint: disable=locally-disabled, too-few-public-methods, too-many-arguments
class UserProfile:
    """This is model to store data from csv."""
    def __init__(self, _id: uuid, user_name: str, email: str, domain_name: str,
                 birthday: str, job_area: str, country: str):
        self._id: uuid = _id
        self.user_name = user_name
        self.email = email
        self.domain_name = domain_name
        self.birthday = birthday
        self.job_area = job_area
        self.country = country
