## para windows faz assim
# 7z e -an -air!*.rar -r -oF:\target
# https://stackoverflow.com/questions/24339419/windows-batch-script-to-recursively-extract-specific-files-using-7zip
# 7z e -an -air *.7z -r 
import os
import sys
import py7zr

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
        for subdir in subdirs:
            print('\t- subdirectory ' + subdir)

        for filename in files:
            file_path = os.path.join(root, filename)

            print('\t- file %s (full path: %s)' % (filename, file_path))
            if filename.endswith('.7z'):
                # Cria um objeto Py7zr para descompactar o arquivo
                print (f' File Name {filename}')
                print (f' File Path {file_path}')

                with py7zr.SevenZipFile(os.path.join(file_path, filename), 'r') as zip_file:
                    # Extrai todos os arquivos do arquivo 7z
                    print(filename)
                    # zip_file.extractall()