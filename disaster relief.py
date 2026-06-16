<!DOCTYPE html>
<html>
<head>
    <title>Disaster Relief Resource Planner</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f9;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }

        h1 {
            text-align: center;
            color: #2c3e50;
        }

        .section {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin-top: 8px;
            margin-bottom: 8px;
        }

        button {
            background: #007bff;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            margin-top: 5px;
        }

        button:hover {
            background: #0056b3;
        }

        #output {
            margin-top: 20px;
            padding: 15px;
            background: #eef2f7;
            border-radius: 5px;
            white-space: pre-line;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>Disaster Relief Resource Planner</h1>

    <!-- Add Resource -->
    <div class="section">
        <h3>Add Resource</h3>

        <input type="text" id="resourceName" placeholder="Resource Name">
        <input type="number" id="resourceQty" placeholder="Quantity">
        <input type="text" id="resourceUnit" placeholder="Unit">

        <button onclick="addResource()">Add Resource</button>
    </div>

    <!-- View Resources -->
    <div class="section">
        <h3>Resources</h3>
        <button onclick="viewResources()">View Resources</button>
    </div>

    <!-- Allocate Resource -->
    <div class="section">
        <h3>Allocate Resource</h3>

        <input type="text" id="areaName" placeholder="Area Name">
        <input type="text" id="allocResource" placeholder="Resource Name">
        <input type="number" id="allocQty" placeholder="Quantity">

        <button onclick="allocateResource()">Allocate Resource</button>
    </div>

    <!-- Allocation History -->
    <div class="section">
        <h3>Allocation History</h3>
        <button onclick="viewAllocations()">View History</button>
    </div>

    <!-- BFS Route Search -->
    <div class="section">
        <h3>BFS Route Search</h3>

        <input type="text" id="startLocation" placeholder="Start Location">
        <input type="text" id="goalLocation" placeholder="Goal Location">

        <button onclick="bfsRoute()">Find Route</button>
    </div>

    <!-- Decision Agent -->
    <div class="section">
        <h3>Decision Agent</h3>

        <input type="number" id="severity" placeholder="Severity Level (1-10)">

        <button onclick="decisionAgent()">Analyze</button>
    </div>

    <!-- Shortage Prediction -->
    <div class="section">
        <h3>Shortage Prediction</h3>

        <input type="number" id="disasters" placeholder="Past Disasters">
        <input type="number" id="shortages" placeholder="Resource Shortages">

        <button onclick="shortagePrediction()">Predict</button>
    </div>

    <!-- Explainable Reasoning -->
    <div class="section">
        <h3>Explainable Reasoning</h3>

        <input type="text" id="reasonArea" placeholder="Area">
        <input type="number" id="reasonSeverity" placeholder="Severity">

        <button onclick="reasoningTrace()">Generate Trace</button>
    </div>

    <div id="output">
        Output will appear here...
    </div>

</div>

<script>

let resources = {};
let allocations = [];

function showOutput(text) {
    document.getElementById("output").innerText = text;
}

function addResource() {

    let name = document.getElementById("resourceName").value;
    let qty = parseInt(document.getElementById("resourceQty").value);
    let unit = document.getElementById("resourceUnit").value;

    resources[name] = {
        quantity: qty,
        unit: unit
    };

    showOutput("Resource Added Successfully!");
}

function viewResources() {

    let output = "AVAILABLE RESOURCES\n\n";

    if (Object.keys(resources).length === 0) {
        output += "No Resources Available";
    }
    else {

        for (let name in resources) {
            output +=
                `${name} : ${resources[name].quantity} ${resources[name].unit}\n`;
        }
    }

    showOutput(output);
}

function allocateResource() {

    let area =
        document.getElementById("areaName").value;

    let resource =
        document.getElementById("allocResource").value;

    let qty =
        parseInt(document.getElementById("allocQty").value);

    if (!resources[resource]) {
        showOutput("Resource Not Found!");
        return;
    }

    let available = resources[resource].quantity;

    if (qty > available) {
        showOutput(
            "Constraint Failed!\nInsufficient Resources"
        );
        return;
    }

    resources[resource].quantity -= qty;

    allocations.push({
        area,
        resource,
        quantity: qty
    });

    showOutput("Allocation Successful!");
}

function viewAllocations() {

    let output = "ALLOCATION HISTORY\n\n";

    if (allocations.length === 0) {
        output += "No Allocations Found";
    }
    else {

        allocations.forEach(a => {
            output +=
            `Area: ${a.area} | Resource: ${a.resource} | Quantity: ${a.quantity}\n`;
        });
    }

    showOutput(output);
}

function bfsRoute() {

    let graph = {
        Warehouse: ["Chennai", "Hyderabad"],
        Chennai: ["Vijayawada"],
        Hyderabad: ["Warangal"],
        Vijayawada: [],
        Warangal: []
    };

    let start =
        document.getElementById("startLocation").value;

    let goal =
        document.getElementById("goalLocation").value;

    let visited = [];
    let queue = [[start]];

    while (queue.length > 0) {

        let path = queue.shift();
        let node = path[path.length - 1];

        if (node === goal) {
            showOutput(
                "Best Route Found:\n" +
                path.join(" ➜ ")
            );
            return;
        }

        if (!visited.includes(node)) {

            visited.push(node);

            (graph[node] || []).forEach(neighbour => {

                let newPath = [...path, neighbour];

                queue.push(newPath);
            });
        }
    }

    showOutput("No Route Found");
}

function decisionAgent() {

    let severity =
        parseInt(document.getElementById("severity").value);

    let output = "";

    if (severity >= 8) {

        output =
        "High Severity\nAction: Send Maximum Resources";

    } else if (severity >= 5) {

        output =
        "Medium Severity\nAction: Send Moderate Resources";

    } else {

        output =
        "Low Severity\nAction: Monitor Situation";
    }

    showOutput(output);
}

function shortagePrediction() {

    let disasters =
        parseInt(document.getElementById("disasters").value);

    let shortages =
        parseInt(document.getElementById("shortages").value);

    let probability = shortages / disasters;

    showOutput(
        "Probability Of Resource Shortage: " +
        probability.toFixed(2)
    );
}

function reasoningTrace() {

    let area =
        document.getElementById("reasonArea").value;

    let severity =
        parseInt(document.getElementById("reasonSeverity").value);

    let output =
        "EXPLAINABLE AI TRACE\n\n" +
        "Area: " + area + "\n" +
        "Severity: " + severity + "\n\n";

    if (severity >= 8) {

        output +=
        "Rule Applied → High Severity Rule\n" +
        "Decision → Allocate Maximum Resources";

    }
    else if (severity >= 5) {

        output +=
        "Rule Applied → Medium Severity Rule\n" +
        "Decision → Allocate Moderate Resources";

    }
    else {

        output +=
        "Rule Applied → Low Severity Rule\n" +
        "Decision → Monitor Situation";
    }

    showOutput(output);
}

</script>

</body>
</html>
