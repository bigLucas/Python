A basic CRUD Python application.

This scripts are make with Python3 and sqlite3.

To compile, download the files, navigate to the directory where the files were saved and enter with the following line of code in bash:

#Linux:
	sudo python3 application.py

OR double-click the application.py file icon

#Win:
	python application.py 

OR double-click the application.py file icon

This CRUD application saves the data in a sqlite3 database, called clients.db, this database stays with the application.

Use pyinstaller to generate an .exe file, turning all scripts into a single file.
Just browse to the directory where the files were saved, via the command prompt and execute the following line of code:

pyinstaller --onefile --windowed --noconsole aplicacao.py