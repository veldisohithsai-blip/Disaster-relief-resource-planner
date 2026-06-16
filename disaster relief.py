class DisasterReliefPlanner:

    def __init__(self):
        self.resources = {}
        self.allocations = []

    # CO1 - State Space Representation
    def add_resource(self):
        name = input("Enter Resource Name: ")
        quantity = int(input("Enter Quantity: "))
        unit = input("Enter Unit: ")

        self.resources[name] = {
            "quantity": quantity,
            "unit": unit
        }

        print("Resource Added Successfully!")

    def view_resources(self):
        print("\nAVAILABLE RESOURCES")
        print("-----------------------")

        if not self.resources:
            print("No Resources Available")
            return

        for name, details in self.resources.items():
            print(
                f"{name} : {details['quantity']} {details['unit']}"
            )

    # CO3 - CSP Resource Allocation
    def allocate_resource(self):

        area = input("Enter Area Name: ")
        resource = input("Enter Resource Name: ")

        if resource not in self.resources:
            print("Resource Not Found!")
            return

        qty = int(input("Enter Quantity To Allocate: "))

        available = self.resources[resource]["quantity"]

        if qty > available:
            print("Constraint Failed!")
            print("Insufficient Resources")
            return

        self.resources[resource]["quantity"] -= qty

        self.allocations.append({
            "area": area,
            "resource": resource,
            "quantity": qty
        })

        print("Allocation Successful!")

    def view_allocations(self):

        print("\nALLOCATION HISTORY")
        print("----------------------")

        if not self.allocations:
            print("No Allocations Found")
            return

        for a in self.allocations:
            print(
                f"Area: {a['area']} | "
                f"Resource: {a['resource']} | "
                f"Quantity: {a['quantity']}"
            )

    # CO2 - BFS Search
    def bfs_route(self):

        graph = {
            "Warehouse": ["Chennai", "Hyderabad"],
            "Chennai": ["Vijayawada"],
            "Hyderabad": ["Warangal"],
            "Vijayawada": [],
            "Warangal": []
            
        }

        start = input("Enter Start Location: ")
        goal = input("Enter Goal Location: ")

        visited = set()
        queue = [[start]]

        while queue:

            path = queue.pop(0)

            node = path[-1]

            if node == goal:
                print("Best Route Found:")
                print(" -> ".join(path))
                return

            if node not in visited:

                visited.add(node)

                for neighbour in graph.get(node, []):

                    new_path = list(path)

                    new_path.append(neighbour)

                    queue.append(new_path)

        print("No Route Found")

    # CO4 - Intelligent Agent
    def decision_agent(self):

        severity = int(
            input("Enter Severity Level (1-10): ")
        )

        print("\nDecision Agent Output")

        if severity >= 8:
            print("High Severity")
            print("Action: Send Maximum Resources")

        elif severity >= 5:
            print("Medium Severity")
            print("Action: Send Moderate Resources")

        else:
            print("Low Severity")
            print("Action: Monitor Situation")

    # CO5 - Bayesian Prediction
    def shortage_prediction(self):

        disasters = int(
            input("Total Past Disasters: ")
        )

        shortages = int(
            input("Number Of Resource Shortages: ")
        )

        probability = shortages / disasters

        print(
            "\nProbability Of Resource Shortage:",
            round(probability, 2)
        )

    # CO6 - Explainable Reasoning
    def reasoning_trace(self):

        area = input("Enter Area: ")
        severity = int(
            input("Enter Severity Level: ")
        )

        print("\nEXPLAINABLE AI TRACE")
        print("----------------------")

        print("Area:", area)
        print("Severity:", severity)

        if severity >= 8:

            print(
                "Rule Applied -> High Severity Rule"
            )

            print(
                "Decision -> Allocate Maximum Resources"
            )

        elif severity >= 5:

            print(
                "Rule Applied -> Medium Severity Rule"
            )

            print(
                "Decision -> Allocate Moderate Resources"
            )

        else:

            print(
                "Rule Applied -> Low Severity Rule"
            )

            print(
                "Decision -> Monitor Situation"
            )


def main():

    planner = DisasterReliefPlanner()

    while True:

        print("\n===================================")
        print(" DISASTER RELIEF RESOURCE PLANNER ")
        print("===================================")

        print("1. Add Resource")
        print("2. View Resources")
        print("3. Allocate Resource")
        print("4. View Allocation History")
        print("5. BFS Route Search")
        print("6. Decision Agent")
        print("7. Shortage Prediction")
        print("8. Explainable Reasoning")
        print("9. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            planner.add_resource()

        elif choice == "2":
            planner.view_resources()

        elif choice == "3":
            planner.allocate_resource()

        elif choice == "4":
            planner.view_allocations()

        elif choice == "5":
            planner.bfs_route()

        elif choice == "6":
            planner.decision_agent()

        elif choice == "7":
            planner.shortage_prediction()

        elif choice == "8":
            planner.reasoning_trace()

        elif choice == "9":
            print(
                "\nThank You For Using Disaster Relief Resource Planner"
            )
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
