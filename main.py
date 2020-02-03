""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import Book, BookStore
from menu import Menu
import ui

store = BookStore()

def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    menu.add_option('2', 'Search For Book', search_book)
    menu.add_option('3', 'Show Unread Books', show_unread_books)
    menu.add_option('4', 'Show Read Books', show_read_books)
    menu.add_option('5', 'Show All Books', show_all_books)
    menu.add_option('6', 'Change Book Read Status', change_read)
    menu.add_option('7', 'Delete Book', delete_book)
    menu.add_option('Q', 'Quit', quit_program)

    return menu

def delete_book():
    new_delete = ui.get_book_id()
    book = store.get_book_by_id(new_delete)
    if not book:
        ui.message('Book not in lib')
    else: 
        book.delete()




def add_book():
    new_book = ui.get_book_info()
    try:
        new_book.save()
    except:  
        '''
        The catch is triggered if the user enters book and author information that is already in the database.
        '''
        print('\nYou have already entered this book and author.\n')
    

def show_read_books():
    read_books = store.get_books_by_read_value(True)
    ui.show_books(read_books)


def show_unread_books():
    unread_books = store.get_books_by_read_value(False)
    ui.show_books(unread_books)


def show_all_books():
    books = store.get_all_books()
    ui.show_books(books)

def search_book():
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
    matches = store.book_search(search_term)
    ui.show_books(matches)



def change_read():

    book_id = ui.get_book_id()
    book = store.get_book_by_id(book_id)  

    new_read = ui.get_read_value()     
    book.read = new_read
    new_print = book.print_change()
    print (new_print)
    book.save()
    

    #If the book value is none the error message is printed
    if book == None:  
        print('\nError: The book id is not in the database\n')
    else:
        new_read = ui.get_read_value()     
        book.read = new_read 
        book.save()


def quit_program():
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()
