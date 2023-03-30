def greet4(first_name= "John", last_name="Doe"):
    """
    
    :param first_name: first name of the persone, default=John
    :param last_name: last name, default=Doe
    :return: name
    """
    print(f"Hi {first_name} {last_name}")

greet4("Lucas", "Baptiste")
greet4()
greet4("James")
greet4(last_name="Baptiste", first_name="Lucas")