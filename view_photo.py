from PIL import ImageTk, Image
import tkinter as tk


def show_photo():
    # Open the image file
    image = Image.open(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\screenshots\CADELINA\CADELINA_1.jpg")

    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)

    # Create a new window
    window = tk.Toplevel()

    # Display the photo in a label widget
    label = tk.Label(window, image=photo)
    label.pack()

    # Set the photo as an attribute of the window to prevent it from being garbage collected
    window.photo = photo

    # Bind a callback function to the label's click event
    label.bind("<Button-1>", lambda event: view_photo(window.photo))


def view_photo(photo):
    # Create a new window to view the photo
    view_window = tk.Toplevel()

    # Display the photo in a label widget
    label = tk.Label(view_window, image=photo)
    label.pack()

    # Start the Tkinter event loop for the view window
    view_window.mainloop()


# Create the main window
root = tk.Tk()

# Create a button to trigger the photo display
button = tk.Button(root, text="View Photo", command=show_photo)
button.pack()

# Start the Tkinter event loop
root.mainloop()
