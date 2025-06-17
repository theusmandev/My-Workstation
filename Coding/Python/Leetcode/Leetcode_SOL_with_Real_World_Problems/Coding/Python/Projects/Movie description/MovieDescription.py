from tkinter import *
import imdb

# Functional part
def search():
    global titlenameLabel, yearnameLabel, directornameLabel, runtimenameLabel, genrenameLabel, ratingnameLabel, castnameLabel
    
    root1 = Toplevel()
    root1.geometry('890x600+200+50')
    root1.title('Movie Information')
    root1.config(bg='orange')

    titleLabel = Label(root1, text='Title', font=('copper black', 30, 'bold'), fg='white', bg='orange')
    titleLabel.place(x=60, y=30)

    titlenameLabel = Label(root1, text='', font=('algerian', 20, 'bold'), fg='white', bg='orange')
    titlenameLabel.place(x=300, y=30)

    directorLabel = Label(root1, text='Director', font=('copper black', 30, 'bold'), fg='white', bg='orange')
    directorLabel.place(x=60, y=100)

    directornameLabel = Label(root1, text='', font=('algerian', 20, 'bold'), fg='white', bg='orange')
    directornameLabel.place(x=300, y=100)

    yearLabel = Label(root1, text='Year', font=('copper black', 30, 'bold'), fg='white', bg='orange')
    yearLabel.place(x=60, y=170)

    yearnameLabel = Label(root1, text='', font=('algerian', 20, 'bold'), fg='white', bg='orange')
    yearnameLabel.place(x=300, y=170)

    runtimeLabel = Label(root1, text='Runtime', font=('copper black', 30, 'bold'), fg='white', bg='orange')
    runtimeLabel.place(x=60, y=240)

    runtimenameLabel = Label(root1, text='', font=('algerian', 20, 'bold'), fg='white', bg='orange')
    runtimenameLabel.place(x=300, y=240)

    genreLabel = Label(root1, text='Genre', font=('copper black', 30, 'bold'), fg='white', bg='orange')
    genreLabel.place(x=60, y=310)

    genrenameLabel = Label(root1, text='', font=('algerian', 20, 'bold'), fg='white', bg='orange')
    genrenameLabel.place(x=300, y=310)

    ratingLabel = Label(root1, text='Rating', font=('copper black', 30, 'bold'), fg='white', bg='orange')
    ratingLabel.place(x=60, y=380)

    ratingnameLabel = Label(root1, text='', font=('algerian', 20, 'bold'), fg='white', bg='orange')
    ratingnameLabel.place(x=300, y=380)

    castLabel = Label(root1, text='Cast', font=('copper black', 30, 'bold'), fg='white', bg='orange')
    castLabel.place(x=60, y=450)

    castnameLabel = Label(root1, text='', font=('algerian', 20, 'bold'), fg='white', bg='orange')
    castnameLabel.place(x=300, y=450)

    # Fetch movie information
    imdbobject = imdb.IMDb()
    movie_name = movieEntry.get().strip()
    movies = imdbobject.search_movie(movie_name)

    if movies:
        index = movies[0].getID()
        movie = imdbobject.get_movie(index)

        # Update labels with movie information
        title = movie.get('title', 'N/A')
        year = movie.get('year', 'N/A')
        director = ', '.join([person['name'] for person in movie.get('directors', [])]) if movie.get('directors') else 'N/A'
        runtime = str(movie.get('runtime', ['N/A'])[0]) + ' min'
        genre = ', '.join(movie.get('genres', 'N/A'))
        rating = str(movie.get('rating', 'N/A'))
        cast = ', '.join([person['name'] for person in movie.get('cast', [])[:5]])  # Show top 5 cast members

        # Update labels with the fetched information
        titlenameLabel.config(text=title)
        yearnameLabel.config(text=year)
        directornameLabel.config(text=director)
        runtimenameLabel.config(text=runtime)
        genrenameLabel.config(text=genre)
        ratingnameLabel.config(text=rating)
        castnameLabel.config(text=cast)
    else:
        titlenameLabel.config(text="No movie found")
        yearnameLabel.config(text="")
        directornameLabel.config(text="")
        runtimenameLabel.config(text="")
        genrenameLabel.config(text="")
        ratingnameLabel.config(text="")
        castnameLabel.config(text="")

    root1.mainloop()

# Main window
root = Tk()
root.geometry('1057x650+100+30')
root.title('Movie Description')
root.resizable(False, False)

bgpic = PhotoImage(file=r"D:\Python\Projects\Movie description\pic.png")
bgLabel = Label(root, image=bgpic)
bgLabel.place(x=0, y=0)

movieLabel = Label(root, text='Movie Name:', font=('algerian', 30, 'bold'), bg='#DEDCDD')
movieLabel.place(x=200, y=570)

movieEntry = Entry(root, font=('FELTX TITLING', 20, 'bold'), bd=5, relief=GROOVE, justify=CENTER)
movieEntry.place(x=490, y=575)
movieEntry.focus_set()

moviesearchButton = Button(root, text='Search', font=('FELIX TITLTNG', 20, 'bold'), bd=5, relief=GROOVE, command=search)
moviesearchButton.place(x=880, y=565)

root.mainloop()
