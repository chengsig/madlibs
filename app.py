from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debeg = DebugToolbarExtension(app)

@app.route('/')
def index():
    """Return homepage. """
    return render_template('home.html', prompts=story.prompts)

@app.route('/story')
def offer_story():
    """print the story from input"""
    # place = request.args.get('place')
    # noun = request.args.get('noun')
    # verb = request.args.get('verb')
    # adjective = request.args.get('adjective')
    # plural_noun = request.args.get('plural_noun')

    # my_story = Story(
    # ["place", "noun", "verb", "adjective", "plural_noun"],
    # """Once upon a time in a long-ago {place}, there lived a
    #    large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    # )

    # story_dictionary = {'place': place, 
    #                     'noun': noun,
    #                     'verb': verb,
    #                     'adjective': adjective,
    #                     'plural_noun': plural_noun
    #                     }

    new_story = story.generate(request.args)

    return render_template("story.html", generated_story=new_story)
