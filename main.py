import instaloader as il
import Generator as g

USER = "your-username"
PASSWORD = "your-password"

L = il.Instaloader()

L.login(USER, PASSWORD)  

profile = il.Profile.from_username(L.context, USER)

unfollowList = g.generateInfo(profile)