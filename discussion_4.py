import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a' or sentence[i] == 'A':
			total += 1
	return total

# Item class
# Describes an item to be sold. Each item has a name and a price.
class Item:
	# Constructor.
	def __init__(self, name, price):
		self.name = name
		self.price = price

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}".format(self.name, self.price))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price_item = self.items[0]
		for item in self.items:
			if item.price > max_price_item.price:
				return max_price_item

	# Checks if item is in item list. If it is print "Item already in warehouse"
	# If item isn't in the item list then print "Adding item" and add item to the warehouse
	def check_warehouse_for_item(self, item):
		if item in self.items:
			print("Item already in warehouse")
		else:
			print("Adding item")
			self.add_item(item)
	


# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6)
		self.item2 = Item("Cider", 5)
		self.item3 = Item("Water", 1)
		self.item4 = Item("Fanta", 2)
		self.item5 = Item("CocaCola", 3)

	## Check to see whether count_a works
	def test_count_a(self):
		# Sentence with an a
		self.assertEqual(count_a("this is bad"), 1)
		
		# With 0 a's
		self.assertEqual(count_a("this is bed"), 0)
		
		# A at beginning
		self.assertEqual(count_a("altitude map"), 2)

		# A at end
		self.assertEqual(count_a("data"), 2)
		
		# Only a's
		self.assertEqual(count_a("aaaaaaa"), 7)

		# Capital A's
		self.assertEqual(count_a("Abraham Amazing Awesome"), 6)


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		w1 = Warehouse()

		self.add_item 
		w1.add_item(self.item1)

		self.assertEqual(len(w1.items), 1)
		self.assertTrue(len(w1.items) > 0)
		self.assertEqual(w1.items[0], self.item1)


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		w2 = Warehouse()
		w2.add_item(self.item1) # max price
		w2.add_item(self.item2)
		w2.add_item(self.item3)

		self.assert_equal(w2.get_max_price(), self.item1)
		self.assert_equal(w2.get_max_price().price, 6)


	## Check to see whethercheck_warehouse_for_item works
	def test_check_warehouse_for_item(self):
		w3 = Warehouse()
		w3.add_item(self.item3)

		# Case 1: check when there the item isn't in the warehouse
		w3.check_warehouse_for_item(self.item1)
		self.assertEqual(w3.itmes, [self.item3, self.item1])
		self.assertEqual(len(w3.items), 2)

		# Case 2: Check when the item is in the warehouse already
		w3.check_warehouse_for_item(self.item1)
		self.assertEqual(w3.itmes, [self.item3, self.item1])
		self.assertEqual(len(w3.items), 2)


def main():
	i1 = Item("Bed", 10)
	print(i1.__str__())
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()