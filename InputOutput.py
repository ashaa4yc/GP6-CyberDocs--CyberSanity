def number(ask, low, high):
    while True: 
        question = input(ask)
        try:
            num = int(question)
            if low <= num <= high:
                return num
            else:
                print(f"Invalid input. Number must be between {low} and {high}!")
        except ValueError:
            print("Invalid input. Enter a valid number !")


def make_bar(value, max_value=100, bar_length=20):
    value = max(0, min(value, max_value))
    filled_bar = round(value / max_value * bar_length)
    empty_bar = bar_length - filled_bar
    return f"[{'#' * filled_bar}{'-' * empty_bar}] {value/max_value}"


list_component = [("Optical Scanner", "Eyes", 5, 10, "Civilian", "Low"),("Subdermal Armor", "Skin", 10, 20, "Civilian", "Mid"),("Load-Lifter Arm", "Arm", 12, 40, "Industrial", "Mid"),("Kerenzikov", "Nervous", 15, 30, "Combat", "High"),("Mantis Blades", "Arm", 18, 35, "Combat", "High"), ("Sandevistan", "Nervous", 25, 60, "Combat", "High"), ("Neural Link", "Nervous", 20, 50, "Civilian", "High"), ("Prosthetic Arm", "Arm", 8, 25, "Medical", "Low"),("Retinal Implant", "Eyes", 6, 12, "Medical", "Low"),("Small Wrist Display", "Arm", 3, 5, "Civilian", "Low"),("Night Vision Lens", "Eyes", 7, 15, "Civilian", "Low"),("Heavy Grip Hand", "Arm", 10, 30, "Industrial", "Mid")]

load = 0
status = number("Select option 1 to install, 4 to exit : ", 1, 4)

while status != 4:
    if status == 1:
        component = input("What component to install ? : ").lower().strip()
        
        for item in list_component:
            item_name = item[0].lower().strip()
            if component in item_name or item_name in component : 
                load += item[2]
                print(f"{item[0]} Installed successfully !")
                break
                
        else:
            print("Component Not Found.")
            
        status = number("Select option 1 to install, 4 to exit : ", 1, 4)
        
    else:
        print("Not Coded Yet")
        status = number("Select option 1 to install, 4 to exit : ", 1, 4)

print(f"Final workload: {load}")
