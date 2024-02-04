import os
import shutil

def copy_pdfs(source_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
 
    for root, dirs, files in os.walk(source_folder):
        if '笔记' in dirs:
                dirs.remove('笔记')
        for file in files:
            if file.endswith('.pdf'):
                shutil.copy(os.path.join(root, file), target_folder)





