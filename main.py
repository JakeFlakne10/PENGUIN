#                0                1                                   2                                    3                                   4                                   5                              6                                         7                                          8
penguin = ["invalid","King Penguin:\n", "Emperor Penguin:\n", "Chinstrap Penguin:\n", "Gentoo Pengui:n\n\n", "Little Penguin:\n\n", "African Penguin:\n", "Southern Rockhopper:\n", "Macaroni Penguin:\n"]
#               0                                      1      2 3 4 5 6 7 8
habitat = ["invalid","Habitat:\nSubantarctic islands.\n", "Habitat:\n", "Habitat:\n", "Habitat:\n", "Habitat:\n", "Habitat:\n", "Habitat:\n", "Habitat:\n"]
#          0                                          1 2 3 4 5 6 7 8
diet = ["invalid", "Diet:\nSmall Fish, Squid, and Krill", "Diet:\n", "Diet:\n", "Diet:\n", "Diet:\n", "Diet:\n", "Diet:\n", "Diet:\n"]
# 1 2 3 4 5 6 7 8
appearance = ["invalid","", "", "", "", "", "", "", ""]
# 1 2 3 4 5 6 7 8
conservation = ["invalid","", "", "", "", "", "", "", ""]
# 1 2 3 4 5 6 7 8
status = ["invalid","", "", "", "", "", "", "", ""]

# choose path/penguin
p =  input("[INPUT NUM. 1-8]pick a penguin to learn about.\n1.king\n2.emperor\n3.chinstrap\n4.gentoo\n5.little\n6.african\n7.southern rockhopper\n8.macaroni\n")

#print info based off path
print(p)
print(penguin[int(p)])
print(habitat[int(p)])
print(diet[int(p)])
print(appearance[int(p)])
print(status[int(p)])

# if statements: {0}
# elif statements: {0}
# else statements: {0}
# lines: 25 - 11(comments) = {14}