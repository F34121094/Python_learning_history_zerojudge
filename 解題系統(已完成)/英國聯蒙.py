read = int(input())
k,d,a = 0,0,0
k_continue = 0
for i in range(read):
       ans = input().strip()
       if ans == "Get_Kill":
              k += 1
              k_continue += 1
              if k_continue <=2 : print("You have slain an enemie.")
              elif k_continue == 3 : print("KILLING SPREE!")
              elif k_continue == 4 : print("RAMPAGE~")
              elif k_continue == 5 : print("UNSTOPPABLE!")
              elif k_continue == 6 : print("DOMINATING!")
              elif k_continue == 7 : print("GUALIKE!")
              elif k_continue >= 8 : print("LEGENDARY!")

       elif ans == "Get_Assist" : a+=1

       elif ans == "Die":
              d+=1
              if k_continue < 3 : print("You have been slained.")
              else :print("SHUTDOWN.")
              k_continue = 0
print(f"{k}/{d}/{a}")


