import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *

screen = Tk()

screen['bg'] = 'yellow'
screen.resizable( width = False, height = False )
screen.geometry( '440x270' )
screen.title( 'Spam to mail' )


def send_mail( event ):
	L = login.get()
	P = password.get()
	U = url.get()
	To = toaddr.get()
	T = topic.get()
	M = mess.get()
	N = number.get()

	for value in range( int( N ) ):
		msg = MIMEMultipart()

		msg[ 'Subject' ] = T
		msg[ 'From' ] = L
		body = M
		msg.attach( MIMEText( body, 'plain' ) )

		server = root.SMTP_SSL( U, 465 )
		server.login( L, P )
		server.sendmail( L, To, msg.as_string() )
		server.quit()

		value += 1
		result [ 'text' ] = 'x' + str( value )


Tlogin = Label( text = 'Login:', font = 'Consolas', background='yellow'  )
login = Entry( screen, font = 'Consolas' )

Tpassword = Label( text = 'Password:', font = 'Consolas', background='yellow'  )
password = Entry( screen, font = 'Consolas' )

Turl = Label( text = 'smtp:', font = 'Consolas', background='yellow' )
url = Entry( screen, font = 'Consolas' )

Ttoaddr = Label( text = 'To whom:', font = 'Consolas', background='yellow' )
toaddr = Entry( screen, font = 'Consolas' )

Ttopic = Label( text = 'Theme:', font = 'Consolas', background='yellow'  )
topic = Entry( screen, font = 'Consolas' )

Tmess = Label( text = 'Message:', font = 'Consolas', background='yellow'  )
mess = Entry( screen, font = 'Consolas' )

Tnumber = Label( text = 'Message count:', font = 'Consolas', background='yellow'  )
number = Entry( screen, font = 'Consolas' )

enter = Button( text = 'Start flooding', font = 'Consolas', width = 18 , background='yellow' )

result = Label( text = 'Flooded:', font = 'Consolas' , background='yellow' )


Tlogin.grid( row = 0, column = 0, sticky = W, padx = 1, pady = 1 )
login.grid( row = 0, column = 1, padx = 1, pady = 1 )

Tpassword.grid( row = 1, column = 0, sticky = W, padx = 1, pady = 1 )
password.grid( row = 1, column = 1, padx = 1, pady = 1 )

Turl.grid( row = 2, column = 0, sticky = W, padx = 1, pady = 1 )
url.grid( row = 2, column = 1, padx = 1, pady = 1 )

Ttoaddr.grid( row = 3, column = 0, sticky = W, padx = 1, pady = 1 )
toaddr.grid( row = 3, column = 1, padx = 1, pady = 1 )

Ttopic.grid( row = 4, column = 0, sticky = W, padx = 1, pady = 1 )
topic.grid( row = 4, column = 1, padx = 1, pady = 1 )

Tmess.grid( row = 5, column = 0, sticky = W, padx = 1, pady = 1 )
mess.grid( row = 5, column = 1, padx = 1, pady = 1 )

Tnumber.grid( row = 6, column = 0, sticky = W, padx = 1, pady = 1 )
number.grid( row = 6, column = 1, padx = 1, pady = 1 )

enter.grid( row = 7, column = 0, padx = 1, pady = 1 )

result.grid( row = 7, column = 1, padx = 1, pady = 1 )


enter.bind( '<Button-1>', send_mail )


screen.mainloop()