"""places blueprint"""
from flask import Blueprint, render_template

places = Blueprint('places', __name__)


@places.route('/place1', methods=['GET'])
def place1():
    """place1 route"""
    return render_template('place1.html')


@places.route('/place2', methods=['GET'])
def place2():
    """place2 route"""
    return render_template('place2.html')




@places.route('/place4', methods=['GET'])
def place4():
    """place4 route""" 
    return render_template('place4.html')



