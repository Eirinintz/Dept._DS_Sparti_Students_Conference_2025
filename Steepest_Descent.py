# The code implements the Steepest Descent Algorithm for finding the minimum of a function of two variables
# The user enters the initial points, parameters and the function they would like to examine
# The algorithm calculates the derivatives and slope of the function, updating the points at each step
# The process is terminated:
# 1) when one of the termination criteria is satisfied (before the maximum number of iterations is exceeded) and thus the results and graphs (in three-dimensional and two-dimensional form) showing the progress of the algorithm are displayed
# 2) when the maximum number of iterations is exceeded, informing the user that the number of iterations has been exceeded without displaying the graphs

# The libraries used to execute the algorithm
import sympy as sp # Calculation of symbolic operations (e.g. for equations, for derivatives)
import numpy as np # Performing mathematical operations
import matplotlib.pyplot as plt # Used to create graphs and visualize results

# Using the Initial_Point() function to input the initial points (x0,y0) from the user
def Initial_Point(): # The function Initial_Point()
    while True: # If the user enters a non-numeric value, the user is prompted to enter the point again, informing the user with a corresponding message
        try: # It will appear on the screen if the user enters a numeric value.
            print("Starting Points & Learning Rate:") # The message initially appears on the user's screen
            x0 = float(input("x0 is the initial point. Please enter x0: ")) # User input of point x0
            y0 = float(input("y0 is the initial point.Please enter y0: ")) # User input of point y0
            return x0, y0 # Returns x0, y0

        except ValueError: # It will appear on the screen in case the user enters an incorrect input, i.e. a non-numeric value
            print("Invalid input! Please enter valid numbers for x0 and y0.") # In this case, a corresponding message is displayed, informing the user and requesting the user to re-enter the point they typed incorrectly (using while True).

# Using the Parameters() function to input a (learning rate) and the constants c1,c2,c3 that terminate the algorithm
def Parameters(): # The function Parameters()
    while True: # If the user enters a value that is not numeric, the corresponding parameter is requested again, informing the user with a corresponding message
        try: # It will appear on the screen in case the user enters a correct input (numeric value)
            a = float(input("a is learning rate. Please enter a: ")) # Input of the learning rate (how fast the method progresses towards the minimum) by the user
            print("-------------------------------------------------------------------------------------")

            # The operation of the algorithm is described in the next command (print)
            print("The Steepest Descent algorithm stops if one of the following termination criteria is met: \n"
            "1. In case the number of iterations exceeds 1000 and any of the criteria has not been met.\n"
            "2. The slope of the function at the point found is less than a constant c1 defined by the user. \n"
            " If the slope is equal to 0 at the starting point (x0,y0), then it prompts the user for a new starting point.\n"
            " 3. The distance between two consecutive points must be less than a constant c2 defined by the user. \n"
            " 4. The value of the function between two consecutive points must be less than a constant c3 defined by the user. \n")
            print("-------------------------------------------------------------------------------------")

            # Input of constants and description of the operation of the corresponding termination criteria
            print("Therefore, for the algorithm to proceed, c1, c2, c3 are required from the user:")
            c1 = float(input("1ο) What is c1 so that the criterion can be examined |∇f| ≤ c1?")) # The first criterion concerns the slope limit
            c2 = float(input("2ο) What is c2 so that the criterion can be examined |Xn - Xn-1| ≤ c2? ")) # The second criterion concerns the limit for the distance between two consecutive points
            c3 = float(input("3ο) What is c3 so that the criterion can be examined |f(Xn) - f(Xn-1)| ≤ c3? ")) # The third criterion concerns the limit for the difference between the values ​​of the function at successive points
            return a, c1, c2, c3 # Returns a, c1, c2, c3

        except ValueError: # It will appear on the screen in case the user enters an incorrect input, i.e. a non-numeric input
            print("Invalid input! Please enter valid numbers.") # In this case, a corresponding message is displayed, informing the user and requesting the user to re-enter the parameter that was typed incorrectly (use of while True)

# Using the f() function so that the user can enter the desired function f(x,y), which will be minimized in the form of symbolic expressions
# Thus, it returns the function in a form that can be processed algebraically by sympy
def f(): # The function f()
    while True: # If the user enters anything other than an equation, the function is requested again, informing the user with a corresponding message
        try: # It will appear on the screen when the user gives a valid function (e.g. 5*x + 4*y)
            print("-------------------------------------------------------------------------------------")
            expr_str = input("Please enter the function in x and y form (e.g., x**2 + y**4): ") # User input of the function of two variables
            expr = sp.sympify(expr_str) # Converting a string to an algebraic expression
            return expr # Returns the algebraic expression

        except sp.SympifyError: # It will appear on the screen in case the user enters an invalid function (e.g. 5x + 4y)
            print("Invalid input! Please enter a valid function.") # In this case, a corresponding message appears, informing the user and requesting the input of a valid function again
            
# Implementation of the steepest_descent algorithm for minimizing a function of two variables
def steepest_descent(f_num, x0, y0, a, c1, c2, c3, derivative_x, derivative_y): # f_num: The function to minimize - converting the symbolic function to arithmetic using lambdify from sympy
    tries = 0 # tries: It represents the number of iterations of the algorithm, that is, how many times the algorithm will repeat the process for the function entered by the user
    MAX_TRIES = 1000 # MAX_TRIES: The maximum number of iterations. If the algorithm does not converge before reaching this number, then it will terminate
    points = [] # points: List that stores the points visited by the algorithm until it reaches the final point or MAX_TRIES
    x, y = sp.symbols('x y') # sp: From the library sympy
    # symbols: A function of the sympy library, used to create symbolic variables, where these variables are not numbers but symbols used in equations
    # x, y: symbols returns two symbolic variables which it assigns to x, y
    # Thus, it has two variables which can be used in derivation, solving equations, etc

    x_path = [x0] # x_path: List that stores the value of x during the algorithm, so that it can be visualized
    y_path = [y0] # y_path: List that stores the value of y during the course of the algorithm, so that it can be visualized
    z_path = [f_num(x0, y0)] # z_path: List that stores the value of f(x, y) during the course of the algorithm, so that it can be visualized

    slope_x = derivative_x.subs({x: x0, y: y0}).evalf() # The derivative value at the point (x0, y0) is calculated, the result is converted to a numerical value and stored in the variable slope_x
    # derivative_x: The partial derivative of the function with respect to the variable x
    # .subs({x: x0, y: y0}): Method used to replace variables x, y with the values ​​x0, y0 respectively
    # .evalf(): Method that converts the symbolic expression into a numeric value and returns it
    
    slope_y = derivative_y.subs({x: x0, y: y0}).evalf() # In the same way here

    grad_norm = sp.sqrt(slope_x**2 + slope_y**2) # The degree measure is calculated, which shows how quickly the function changes at the point we are examining
    # grad_norm: Calculating the norm of the gradient vector (gradient norm)
    # If it is zero, it means that the function is already at a local minimum or maximum.
    # sp.sqrt: Calculating the square root of the sum of the squares of the derivatives

    slope_x_expr = derivative_x # The value of the partial derivative with respect to x is assigned to the variable slope_x_expr
    slope_y_expr = derivative_y # The value of the partial derivative with respect to y is assigned to the variable slope_y_expr
    slope_x = slope_x_expr.subs({x: x0, y: y0}).evalf() # Replacing x,y by x0,y0 & calculating the numerical value of the partial derivative with respect to x at the point (x0, y0)
    slope_y = slope_y_expr.subs({x: x0, y: y0}).evalf() # Substituting x,y by x0,y0 & calculating the numerical value of the partial derivative with respect to y at the point (x0, y0)
    print("The partial derivative with respect to x:", slope_x_expr) # Display the partial derivative with respect to x
    print("The partial derivative with respect to y:", slope_y_expr) # Display the partial derivative with respect to y

    # In case the slope is 0, we ask the user to give new x0 and y0
    while grad_norm == 0:
        print("The slope at point (x0, y0) is 0. Please enter a new starting point.")
        x0, y0 = Initial_Point() # The user gives the new points again

        # We recalculate the derivatives and the slope at the new point
        slope_x = derivative_x.subs({x: x0, y: y0}).evalf()
        slope_y = derivative_y.subs({x: x0, y: y0}).evalf()
        grad_norm = sp.sqrt(slope_x**2 + slope_y**2)

    # As the algorithm repeats the process and terminates after 1000 iterations
    while tries <= MAX_TRIES:
        # Calculating derivatives and gradients
        slope_x = derivative_x.subs({x: x0, y: y0}).evalf()
        slope_y = derivative_y.subs({x: x0, y: y0}).evalf()
        grad_norm = sp.sqrt(slope_x**2 + slope_y**2)

        # Adding the point with coordinates (x0,y0) to the points list using the append method
        points.append((x0, y0))

        # TERMINATION CRITERIA
        # Criterion 1 -> Check if the slope is less than the constant c1:
        # If it is, the process is stopped and the result is recorded in the criterion
        # If not, it checks if there are at least two points in the points list. If there are, it calculates the distance of the last and penultimate point, based on the Euclidean distance formula.
        if grad_norm < c1: # grad_norm: the value of the slope. If the value of the slope is less than the constant c1 defined above, then the algorithm proceeds to the next instructions after the 1st criterion is satisfied
            criterion = "1st criterion: The slope is small." # If the above condition is true, then the variable criterion is assigned the value "1st criterion: The slope is small.", which recognizes that the 1st criterion has been satisfied
            break # If the above is true, then the loop execution stops and the process is completed

        elif len(points) > 1: # If the first criterion is not satisfied, the case is considered where the slope value is greater than the constant c1
            prev_x, prev_y = points[-2] # points[-2]: Refers to the second-to-last element of the points list
            # Therefore, the command "prev_x, prev_y = points[-2]" assigns the coordinates of the penultimate point in the list to the variables prev_x, prev_y
            distance = sp.sqrt((x0 - prev_x)**2 + (y0 - prev_y)**2).evalf() # (x0 - prev_x)**2 + (y0 - prev_y)**2: Calculating the square of the distance between two points in two-dimensional space
            # .evalf(): Calculates the numerical value of the result, converting the symbolic expression to a decimal number and storing it in the distance variable


            # Criterion 2 -> Check if the distance between the current and the penultimate point is less than the constant c2:
            # If it is, the process is stopped and the result is recorded in the criterion
            # If it is not, the values ​​of the function at the penultimate and current points are calculated and stored in the variables f_prev and f_current respectively, in order to complete the optimization process and find the minimum point.
            if distance < c2: # distance: The distance shows us how far apart the two points are in two-dimensional space (it has been calculated above)
            # When the distance between two consecutive points is less than the value of the constant c2 entered by the user, then the condition is true and the points are very close to each other
                criterion = "2nd criterion: The distance between two consecutive points is small." # The value "2nd criterion: The distance between two consecutive points is small." is assigned to the variable criterion
                break  # If the above is true, then the loop execution stops and the process is completed

            f_prev = f_num(prev_x, prev_y) # The value of the function f_num is calculated at the penultimate point (prev_x, prev_y), which is the previous point from (x0, y0)
            # The value of the function at the penultimate point is stored in the variable f_prev
            f_current = f_num(x0, y0) # The value of the function f_num is calculated at the current point (x0, y0)
            # The value of the function at the current point is stored in the variable f_current


            # Criterion 3 -> Convergence of the difference of function values. Checks whether the absolute difference between the values ​​of a function at two consecutive points is less than the constant c3:
            # If it is, then the function has converged and the convergence criterion is recorded
            if abs(f_current - f_prev) < c3: # abs(): Absolute value function
            # Here, the absolute difference between the values ​​of the function at two consecutive points is calculated
            # If this difference is less than the constant c3, then it does not change much from one point to another
            # This means that the optimization process is approaching the desired result
                criterion = "3rd criterion: The convergence of the function is small." # If the above condition is true, then the value "3rd criterion: The convergence of the function is small.", is assigned to the variable criterion
                break # If the above is true, then the loop execution stops and the process is completed
                # The process is stopped because there are no significant changes in the function values
            # This means that the process is complete since the function values ​​no longer change significantly
            # Thus, the function approaches the minimum point

        # Update variables x0 and y0. The values ​​are updated based on the slope and learning rate (as demonstrated in the following operations)
        x0 = x0 - a * slope_x
        y0 = y0 - a * slope_y

        x_path.append(x0) # Append the current value of x, i.e. each time x0, to the list x_path, so that this list contains all the points x visited by the algorithm throughout the process
        # So, the list displays the points that x has passed as it approaches the optimum
        y_path.append(y0) # Append the current value of y, i.e. each time y0, to the y_path list, so that this list contains all the y points visited by the algorithm throughout the process
        # So, the list displays the points that y has passed as it approaches the optimum
        z_path.append(f_num(x0, y0)) # Append the function values ​​to each (current) point (x0, y0) in the z_path list
        # In this way, we know how the value of the function changes as we approach the optimum during the iterations of the algorithm.

        # Go to the next cycle of repeating the process to check the next points
        tries += 1

    # If the algorithm fails to converge to an optimal point within the specified number of iterations, then there is a failure
    if tries > MAX_TRIES: # If the process of finding the minimum exceeds 1000 iterations...
        criterion = f"Search failed: maximum retries ({MAX_TRIES})." # ...informs the user about the reason the algorithm failed to find the optimum
        return x0, y0, None, criterion, False, x_path, y_path, z_path, tries # Return the specified points, parameters, criterion and number of iterations

    # If the execution is successful, then the following is returned:
    # The final values ​​of the parameters, the final value of the function, a success message & success status (True), the path of the values ​​x, y, f(x,y) and the total number of iterations
    return x0, y0, f_num(x0, y0), criterion, True, x_path, y_path, z_path, tries

# Χρήση της κύριας συνάρτησης main(), η οποία εκτελεί όλο το πρόγραμμα. Είναι υπέυθυνη για την εκτέλεση του βασικού προγράμματος
def main(): # Η συνάρτηση main()
    x0, y0 = Initial_Point() # Ζητά από τον χρήστη τα αρχικά σημεία (x0, y0), καλώντας την συνάρτηση Initial_Point()
    a, c1, c2, c3 = Parameters() # Ζητά από τον χρήστη τον ρυθμό εκμάθησης και τις σταθερές τερματισμού κριτηρίων (a, c1, c2, c3) καλώντας την συνάρτηση Parameters()

    f_sym = f() # Καλεί την συνάρτηση f(), η οποία ορίζει την συμβολική συνάρτηση που θέλουμε να βελτιστοποιήσουμε
    x, y = sp.symbols('x y') # Δημιουργεί τις συμβολικές μεταβλητές x, y με την βιβλιοθήκη Sympy

    # Μετατροπή της συνάρτησης από συμβολική σε αριθμητική συνάρτηση που μπορεί να υπολογίζει τις τιμές των x, y
    f_num = sp.lambdify((x, y), f_sym, "numpy")

    derivative_x_sym = sp.diff(f_sym, x) # Υπολογισμός μερικής παραγώγου της συνάρτησης f(x,y) ως προς x χρησιμοποιώντας την Sympy
    derivative_y_sym = sp.diff(f_sym, y) # Υπολογισμός μερικής παραγώγου της συνάρτησης f(x,y) ως προς y χρησιμοποιώντας την Sympy

    # Αποθήκευση αποτελεσμάτων μετά την εκτέλεση του κώδικα
    min_x, min_y, min_value, criterion, show_plots, x_path, y_path, z_path, total_tries = steepest_descent(f_num, x0, y0, a, c1, c2, c3, derivative_x_sym, derivative_y_sym)

    # Στην περίπτωση που ο μέγιστος αριθμός επαναλήψεων ξεπεραστεί, τότε δεν εμφανίζονται τα γραφήματα
    if not show_plots:
        print("Ο μέγιστος αριθμός επαναλήψεων ξεπεράστηκε.") # Εμφανίζεται το συγκεκριμένο μήνυμα ενημερώνοντας τον χρήστη
        return

    # Ο αλγόριθμος θα διαβάσει τις παρακάτω εντολές, σε περίπτωση που έχω:
    print("-------------------------------------------------------------------------------------")
    print(f"Ελάχιστο σημείο: ({min_x}, {min_y}), με τιμή συνάρτησης f(x, y) = {min_value}") # 1) τις τιμές του ελάχιστου σημείου, 2) της τιμής της συνάρτησης,
    print("Κριτήριο σύγκλισης ->", criterion) # 3) το κριτήριο που ικανοποιήθηκε
    print(f"Αριθμός επαναλήψεων: {total_tries}") # 4) τον αριθμό των επαναλήψεων

    # Αν τα παραπάνω αποτελέσματα είναι έγκυρα, τότε δημιουργούνται 3D και 2D γραφήματα τα οποία απεικονίζουν την πορεία του αλγορίθμου
    x_vals = np.linspace(-1.5, 1.5, 400) # Αφορά τις 400 ενδιάμεσες τιμές από -1.5 έως 1.5 για τον άξονα x
    y_vals = np.linspace(-1.5, 1.5, 400) # Αφορά τις 400 ενδιαμεσες τιμές από -1.5 έως 1.5 για τον άξονα y
    X, Y = np.meshgrid(x_vals, y_vals) # Δημιουργία πινάκων X (περιέχει όλες τις συντεταγμένες του άξονα x) και Y (περιέχει όλες τις συντεταγμένες του άξονα y)
    Z = f_num(X, Y) # Υπολογίζεται η τιμή της συνάρτησης f_num για κάθε ζεύγος (X,Y). Άρα, το Z αντιπροσωπεύει το ύψος του γραφήματος
    fig = plt.figure(figsize=(14, 6)) # Δημιουργία σχήματος με διαστάσεις: 14 ίντσες πλάτος και 6 ίντσες ύψος
    # figsize: Μέγεθος παραθύρου ώστε το γράφημα να είναι μεγάλο

    # 3D Plot (3 διαστάσεις: X, Y, Z)
    ax1 = fig.add_subplot(121, projection='3d')
    # Δημιουργία ενός υπογράφου στον πρώτο χώρο με διάταξη 1x2 (μία γραμμή και δύο στήλες), ο οποίος να έχει τρισδιάστατη μορφή (projection='3d')

    ax1.plot_surface(X, Y, Z, alpha=0.3, cmap='viridis') # Δημιουργία επιφάνειας
    # alpha=0.3: Δημιουργία ημιδιαφανούς επιφάνειας ώστε να διακρίνονται τα στοιχεία από κάτω
    # cmap='viridis': Αφορά τα χρώματα που θα απεικονίσουν την επιφάνεια (στυλ "viridis")

    ax1.plot(x_path, y_path, z_path, 'r-', label='Steepest Descent Path') # Η συνάρτηση αυτή σχεδιάζει την πορεία του αλγορίθμου της Steepest Descent
    # x_path, y_path, z_path: Λίστες που περιέχουν τις συντεταγμένες της πορείας του αλγορίθμου
    # r-: Ορίζει το χρώμα και τον τύπο της γραμμής (r: κόκκινο, -: συνεχής)
    # label='Steepest Descent Path': Ορίζει την ετικέτα

    ax1.scatter(min_x, min_y, min_value, color='red', s=100, label='Ελάχιστο Σημείο') # Τοποθέτηση του ελαχίστου
    # min_x, min_y, min_value: Περιέχουν τις συντεταγμένες του ελαχίστου
    # color='red': Ορίζει το χρώμα του ελαχίστου
    # s=100: Μέγεθος ελαχίστου (κουκίδας)
    # label='Ελάχιστο Σημείο': Ορίζει την ετικέτα

    # Ορίζει τις ετικέτες για τους άξονες x, y, z
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$'),
    ax1.set_zlabel('$f(x, y)$')

    # Προσθήκη λεζάντας για την εμφάνιση των labels που έχουμε καθορίσει για κάθε στοιχείο
    ax1.legend()


    # 2D Contour Plot (Ισοϋψεις Καμπύλες)
    ax2 = fig.add_subplot(122)
    # Δημιουργία ενός νέου υπογράφου στον δεύτερο χώρο με διάταξη 1x2 (μία γραμμή και δύο στήλες)

    ax2.contour(X, Y, Z, levels=50, cmap='viridis') # Σχεδίαση ισοϋψών καμπυλών
    # levels=50: Ορίζει τον αριθμό των ισοϋψών καμπυλών που θα σχεδιαστούν
    # cmap='viridis': Αφορά τα χρώματα που θα απεικονίσουν τις καμπύλες (στυλ "viridis")

    ax2.plot(x_path, y_path, 'r-', label='Steepest Descent Path') # Η συνάρτηση αυτή σχεδιάζει την πορεία του αλγορίθμου της Steepest Descent
    # x_path, y_path: Λίστες που περιέχουν τις συντεταγμένες της πορείας του αλγορίθμου
    # r-: Ορίζει το χρώμα και τον τύπο της γραμμής (r: κόκκινο, -: συνεχής)
    # label='Steepest Descent Path': Ορίζει την ετικέτα

    ax2.scatter(min_x, min_y, color='red', s=100, label='Ελάχιστο Σημείο') # Τοποθέτηση του ελαχίστου
    # min_x, min_y: Περιέχουν τις συντεταγμένες του ελαχίστου
    # color='red': Ορίζει το χρώμα του ελαχίστου
    # s=100: Μέγεθος ελαχίστου (κουκίδας)
    # label='Ελάχιστο Σημείο': Ορίζει την ετικέτα

    # Ορίζει τις ετικέτες για τους άξονες x, y
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('$y$')

    # Προσθήκη λεζάντας για την εμφάνιση των labels που έχουμε καθορίσει για κάθε στοιχείο
    ax2.legend()

    # Εμφάνιση 3D και 2D γραφημάτων
    plt.show()

# Ολοκλήρωση της main

main()








