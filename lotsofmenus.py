from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import  Base, Category, Item
 
engine = create_engine('sqlite:///categorywithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Menu for UrbanBurger
category1 = Category(name = "Urban Burger")

session.add(category1)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", category = category1)

session.add(item1)
session.commit()

item2 = Item(name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", category = category1)

session.add(item2)
session.commit()

item3 = Item(name = "Chocolate Cake", description = "fresh baked and served with ice cream", category = category1)

session.add(item3)
session.commit()

item4 = Item(name = "Sirloin Burger", description = "Made with grade A beef", category = category1)

session.add(item4)
session.commit()

item5 = Item(name = "Root Beer", description = "16oz of refreshing goodness", category = category1)

session.add(item5)
session.commit()

item6 = Item(name = "Iced Tea", description = "with Lemon", category = category1)

session.add(item6)
session.commit()

item7 = Item(name = "Grilled Cheese Sandwich", description = "On texas toast with American Cheese", category = category1)

session.add(item7)
session.commit()

item8 = Item(name = "Veggie Burger", description = "Made with freshest of ingredients and home grown spices", category = category1)

session.add(item8)
session.commit()




#Menu for Super Stir Fry
category2 = Category(name = "Super Stir Fry")

session.add(category2)
session.commit()


item = Item(name = "Chicken Stir Fry", description = "with your choice of noodles vegetables and sauces",category = category2)

session.add(item)
session.commit()

item2 = Item(name = "Peking Duck", description = " a famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", category = category2)

session.add(item2)
session.commit()

item3 = Item(name = "Spicy Tuna Roll", description = "Test", category = category2)

session.add(item3)
session.commit()

print "added menu items!"

