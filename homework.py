class User():
  first_name = ""
  last_name = ""
  email_address = ""
  phone_number = ""
  allergies = ""
  food_diet = ""

  def get_full_name(self):
    return "{} {}".format(self.first_name, self.last_name)


class fullMenu():
  mealItems = []
  date = ""
  filter = ""


class Meal():
  title = ""
  portion_size = ""
  details = ""
  ingredients = ""


class Price():
  price = ""
  quantity = ""
  totalAmount = ""


class Order(Meal, Price):
  orderId = ""
  orderedMeal = Meal.name
  quantity = Meal.serving_size
  short_description = ""
  isPacked = False
  additional_needs = ""
  price = Price.totalPrice


user = User()  # instantiate the user class
user.first_name = "Tim"
user.last_name = "Afrane"
user.phone_number = "+2331234456774"
user.email_address = "tim@hooge.capital"
user.allergies = "pinapples"
