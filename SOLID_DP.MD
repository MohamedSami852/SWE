1. PizzaToppings: 
   applied to dynamically add toppings to the selected pizza 

2. InventoryManager: 
   centralized inventory management that includes all components ensuresing consistentancy

Principles:

1. Single Responsibility Principle 
   `Pizza`, `InventoryManager` one singel responsability 

2. Open/Closed Principle
classes like Pizza and Cheese, Olives, Mushrooms are open for extension but closed for modification.

3. Liskov Substitution Principle
   subclasses like margheritaPizza and pepperoniPizza correctly implement the interfaces .

4. Interface Segregation Principle 
   specific interfaces like Payment ensure no unneccessary methods .

5. Dependency Inversion 
high-level modules  depend on abstractions like ayment instead of concrete implementations.

---

