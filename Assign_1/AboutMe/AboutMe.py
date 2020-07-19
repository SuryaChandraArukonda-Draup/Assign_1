from Edit.Edit import EditData
from Delete.Delete import Delete


class AboutMe(EditData, Delete):
    def __init__(self, uid, name, profession, contact, skills, DOB, description):
        self.uid = uid
        self.name = name
        self.profession = profession
        self.contact = contact
        self.skills = skills
        self.DOB = DOB
        self.description = description
