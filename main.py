#                0                1                                   2                                    3                                   4                                   5                              6                                         7                                          8
penguin["invalid","King Penguin:\n\n", "Emperor Penguin\n\n", "Chinstrap Penguin\n\n", "Gentoo Penguin\n\n", "Little Penguin\n\n", "African Penguin\n\n", "Southern Rockhopper\n\n", "Macaroni Penguin\n\n"]
#               0                                      1      2 3 4 5 6 7 8
habitat["invalid","Habitat:\nSubantarctic islands.\n", "Habitat:\n", "Habitat:\n", "Habitat:\n", "Habitat:\n", "Habitat:\n", "Habitat:\n", "Habitat:\n"]
#          0                                          1 2 3 4 5 6 7 8
diet["invalid", "Diet:\nSmall Fish, Squid, and Krill", "Diet:\n", "Diet:\n", "Diet:\n", "Diet:\n", "Diet:\n", "Diet:\n", "Diet:\n"]
# 1 2 3 4 5 6 7 8
appearance["invalid","", "", "", "", "", "", "", ""]
# 1 2 3 4 5 6 7 8
conservation["invalid","", "", "", "", "", "", "", ""]
# 1 2 3 4 5 6 7 8
status["invalid","", "", "", "", "", "", "", ""]

# choose path/penguin
p =  ("[INPUT NUM. 1-8]pick a penguin to learn about.\n1.king\n2.emperor\n3.chinstrap\n4.gentoo\n5.little\n6.african\n7.southern rockhopper\n 8.macaroni ")

#print info based off path
print(int(penguin[p]))
print(int(habitat[p]))
print(int(diet[p]))
print(int(appearence[p]))
print(int(status[p]))

# if statements: {0}
# elif statements: {0}
# else statements: {0}
# lines: 25 - 11(comments) = {14}