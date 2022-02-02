from praks2.ylesanne13.kasutajad2 import Kasutajad
class Admin(Kasutajad):
    privileegid =[]


    def naita_privileegid(self):
        for each in self.privileegid:
            print(each)