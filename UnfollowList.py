import instaloader
import Generator

USER = "your-username"
PASSWORD = "your-password"

L = instaloader.Instaloader()

L.login(USER, PASSWORD)  

profile = instaloader.Profile.from_username(L.context, USER)

unfollowList = Generator.generateInfo(profile)