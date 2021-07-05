from sys import maxsize


class Contact:
    def __init__(self,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 home=None,
                 mobile=None,
                 work=None,
                 fax=None,
                 email=None,
                 homepage=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 address2=None,
                 phone2=None,
                 notes=None,
                 id=None
                 ):
        self.notes = notes
        self.phone2 = phone2
        self.address2 = address2
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.homepage = homepage
        self.email = email
        self.fax = fax
        self.work = work
        self.mobile = mobile
        self.home = home
        self.address = address
        self.company = company
        self.title = title
        self.nickname = nickname
        self.lastname = lastname
        self.middlename = middlename
        self.firstname = firstname
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (
                       self.id is None
                       or other.id is None
                       or self.id == other.id) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
