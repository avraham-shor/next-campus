class UnderAge(ValueError):
    def __init__(self,_age):
        self._age = _age

    def __str__(self):
        return f"""Sorry! your age is only {self._age} years old
                and is less than 18,
            In {18-self._age} years time you can reach a birthday
        """














def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


send_invitation("avraham",20)
send_invitation("moshe",17)
