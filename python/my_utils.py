def credentials(file = "./data/login.txt"):
    """TODO: Documentation
    """
    login = open(file,"r")
    myUsername = login.readline().strip()
    myPassword = login.readline().strip()
    return(myUsername,myPassword)
