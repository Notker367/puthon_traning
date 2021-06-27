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

