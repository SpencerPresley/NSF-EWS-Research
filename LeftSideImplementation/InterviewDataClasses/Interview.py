from dataclasses import dataclass

# mitigates in-file errors where InterviewFeatures is not defined
# while avoiding circular imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .InterviewFeatures import InterviewFeatures

@dataclass
class Interview:
    # for database storage
    interview_id: str
    
    # for ui display
    interview_title: str
    interview_document: str
    interview_features: 'InterviewFeatures'
    
    # string to be inputted into method to lookup vector for
    # interview in db
    vector_lookup_id: str
    
    def __init__(self, *, interview_id, interview_document, interview_title, interview_features: 'InterviewFeatures'):
        self.interview_id = interview_id
        self.interview_document = interview_document
        self.interview_title = interview_title
        self.interview_features = interview_features
        self.vector_lookup_id = self.set_vector(interview_id)
    
    @staticmethod
    def set_vector(interview_id):
        # upload to blob storage
        # vectorize the interview data
        # set vector for the interview data
        vector_lookup_id = f"lookup(interview_id: {interview_id})"
        return vector_lookup_id
    
    def get_vector(self):
        # using vector_lookup_id, get the vector from storage and return it
        return f"vector({self.vector_lookup_id})"