# Recursive sudoku  

## The main goal

At first this project was just meant to be a shallow dive into recursive algorithms.  
But I have procrastinated on this project for too long, so it was kinda forgotten for a long time.  
Fast forward a few months — I decided to learn **React** and then after learning basics, a brilliant thought appeared — to create a **React** SPA that would basically consist of two functions:
- get a new sudoku puzzle
- solve the puzzle

## Deeper into the rabbit hole

But by that time I had made a little bit of progress in recursively solving sudoku using python and I would have no fun redoing it in JavaScript. So another thought appeared — to create a basic server that would be able to get new puzzles, recieve puzzles from client, solve recieved puzzles and then return them back to the client.

Django seemed like a bit of an overkill for such a simple task, so I used **Flask**, as it  is much more suitable for smaller and simpler projects.

## Hosting

My friend asked me if they could check out my project themselves without having to download and install a ton of stuff. So I had some fun (not really) putting the app on heroku.

It is available [here](https://recursive-sudoku.herokuapp.com/)