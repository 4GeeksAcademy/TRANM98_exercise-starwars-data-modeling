import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(String(20), unique=True, primary_key=True)
    email = Column(String(30), unique=True, nullable=False)
    password_hash = Column(String(20), nullable=False)
    name = Column(String(20), nullable=False)
    favorites = relationship("Favorite", back_populates="user")

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    charcter_name = Column(String(250, nullable=False))
    species = Column(String(100))
    gender = Column(String(50))
    description = Column(String(250))
    image_url = Column(String)
    favorites = relationship("Favorite", back_populates="character")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    population = Column(Integer)
    description = Column(String)
    image_url = Column(String)
    favorites = relationship("Favorite", back_populates="planet")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
