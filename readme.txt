
# Georgian Letter Recognition Project

This project is a graphical application for recognizing handwritten Georgian letters using neural networks. It provides an interactive interface for users to draw letters, store them as training data, and train or test a neural network model for letter recognition. The neural network is built with [PyBrain](http://pybrain.org/), and the frontend interface is developed using Tkinter.

## Features

### User Interface
The application has a simple and intuitive user interface that includes:
- **Canvas Board**: Draw Georgian letters on a canvas board using a mouse or other input device.
- **SQLite Database Integration**: Save drawn letters as training data in a local SQLite database.
- **Neural Network Functionality**:
  - **Train Data**: Train the neural network on saved letter samples.
  - **Guess Letter**: Use a pre-trained model to guess the drawn letter and display results.

### Key Functionalities
1. **Drawing and Saving Letters**: Draw any Georgian letter on the canvas and save it to the local SQLite database as training data. Each drawing can be saved and labeled for future training.
2. **Guessing the Letter**: After drawing a letter, click the “?” button to make the model guess the letter. This action activates the trained neural network, which will analyze the drawing and return a list of possible letters, each with a probability percentage. These results are plotted using Matplotlib for a clear visualization of the network’s confidence levels.
3. **Training the Neural Network**: Click the “Train Data” button to train the neural network with the data stored in the SQLite database. This button reconfigures the model based on the most recent training data, improving its accuracy over time.

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: For the graphical user interface, providing a canvas for drawing letters and control buttons.
- **SQLite**: For managing the storage of training data locally.
- **PyBrain**: For creating, training, and evaluating the neural network model.
- **Matplotlib**: For plotting and displaying the model’s guess percentages.

## Educational Purpose

This project serves as an educational tool for understanding neural networks and the backpropagation algorithm. It demonstrates how neural networks can be applied to recognize handwritten letters and provides hands-on experience with training, storing, and evaluating data for a machine learning model.
