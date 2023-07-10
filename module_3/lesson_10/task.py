# import os
#
# while True:
#     current_dir = os.getcwd()
#     command = input(current_dir + "$ ").split()
#     match command[0]:
#         case "cd":
#             os.chdir(command[1])
#
# # cp file_path dir_path
# # pwd
# # cat # "print('hello')" >> text.txt
# # mkdir
# # touch
# # copy
# # ls , dir
# # rm
# # rmdir

# ================================
from pathlib import Path
from os.path  import join

# print("1/2/3")

# path_ = Path(__file__)
# print(Path.is_dir(path_))
# print(Path.exists(Path("home2")))
# print(Path.cwd())

# print(Path.is_file(Path(join(path_ , 'task.py'))))

# =================================

import os
from pathlib import Path

# l = os.listdir()
# c = 0
# for i in l:
#     if Path(i).is_file():
#         c += 1
# print(c)

print(os.path.getsize("/home/os_.py"))



"""
HOME WORK :
    max getsize file
    terminal
"""




















