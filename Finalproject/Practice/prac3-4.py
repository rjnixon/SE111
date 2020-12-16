guest_list = ['Fred', 'Nate', 'Billy']
print(guest_list[0])
i= 0

guest_list.insert(0, "Victor")
guest_list.insert(1, "Niko")
guest_list.insert(2, "Tara")

while i < 6 :

    print('Hello, ' + guest_list[i] + '. You are invited to dinner')

    i = i + 1

busy = guest_list.pop()
print(busy ,"Has plans.")
guest_list.append('Bob')

print(guest_list.pop() ,"I do not have enough room Sorry.")
print(guest_list.pop() ,"I do not have enough room Sorry.")
print(guest_list.pop() ,"I do not have enough room Sorry.")
print(guest_list.pop() ,"I do not have enough room Sorry.")
print(guest_list)

del guest_list[0]
del guest_list[0]

print(guest_list)
  

