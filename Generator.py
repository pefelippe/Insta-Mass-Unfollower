with open('whitelist.txt', 'r') as w:
    whitelist = w.read().splitlines()
    
def createArquive(lista, name):
    archiveName = str(name) + '.txt'
    
    arquivo = open (archiveName, "w+")
    
    for line in lista:
        if (line.username not in whitelist):
            arquivo.write(line.username + '\n')
        else:
            print(f"Ignored: {line.username}")
        
def generateInfo(profile):
    userFollowers = profile.get_followers()

    userFollowees = profile.get_followees()

    unfollowList = list(set(userFollowees) - set(userFollowers))
    
    createArquive(unfollowList, 'unfollowList')
    


