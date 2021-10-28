# The Maddest Madlib

The Maddest Madlib is a Python terminal project whose primary purpose is to boost users' moods and provide various experiences.

Secondarily, it may help users to practice English grammar.

Users can quickly learn the rules of the game and type any words according to the provided instructions. In the end, they will receive a story that includes words from the user's input which are modified according to the English grammatical rules as much as it is possible.





## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!