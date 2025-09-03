def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if weight > 0 and weight <= 500:
                return weight
            else:
                print("Please enter a valid weight between 0 and 500 kg!")
        except ValueError:
            print("Please enter a valid number for weight!")

def get_height():
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height > 0 and height <= 3.0:
                return height
            else:
                print("Please enter a valid height between 0 and 3.0 meters!")
        except ValueError:
            print("Please enter a valid number for height!")

def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_health_advice(category):
    advice = {
        "Underweight": "Consider consulting a healthcare provider for guidance on healthy weight gain.",
        "Normal weight": "Great! Maintain your current lifestyle with balanced diet and regular exercise.",
        "Overweight": "Consider adopting a healthier diet and increasing physical activity.",
        "Obese": "It's recommended to consult a healthcare provider for a weight management plan."
    }
    return advice.get(category, "Consult a healthcare provider for personalized advice.")

def display_results(weight, height, bmi, category):
    print("\n" + "="*60)
    print("                    BMI CALCULATION RESULT")
    print("="*60)
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi}")
    print(f"Category: {category}")
    print("-"*60)
    advice = get_health_advice(category)
    print("Health Advice:")
    print(advice)
    print("="*60)

def show_bmi_chart():
    print("\n" + "="*40)
    print("           BMI REFERENCE CHART")
    print("="*40)
    print("Underweight    : BMI < 18.5")
    print("Normal weight  : BMI 18.5 - 24.9")
    print("Overweight     : BMI 25.0 - 29.9")
    print("Obese          : BMI >= 30.0")
    print("="*40)

def main():
    print("="*60)
    print("              WELCOME TO BMI CALCULATOR")
    print("="*60)
    print("Body Mass Index (BMI) is a measure of body fat based on height and weight")
    
    while True:
        try:
            print("\nChoose an option:")
            print("1. Calculate BMI")
            print("2. View BMI Chart")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == '1':
                weight = get_weight()
                height = get_height()
                
                bmi = calculate_bmi(weight, height)
                category = get_bmi_category(bmi)
                
                display_results(weight, height, bmi, category)
                
            elif choice == '2':
                show_bmi_chart()
                
            elif choice == '3':
                print("\nThank you for using BMI Calculator!")
                print("Stay healthy and take care!")
                break
                
            else:
                print("Invalid choice! Please select 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again!")

if __name__ == "__main__":
    main()