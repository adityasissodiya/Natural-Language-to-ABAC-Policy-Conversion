### **1. Project Goal and Concept**
The objective is to **convert natural language access control policies** (e.g., "The driver can update the car's software when the vehicle is stationary") into **executable XACML (eXtensible Access Control Markup Language) ABAC (Attribute-Based Access Control) policies**. The challenge is ensuring that natural language policies are correctly interpreted, translated, and executed as formal policies.

### **2. Domain Context: Connected Car Ecosystem**
We are focusing on access control policies within a **connected car ecosystem**. This involves subjects (e.g., drivers, passengers), actions (e.g., update, control), resources (e.g., vehicle data, software), and conditions (e.g., car status, network connectivity).

#### **Example Policy:**
*"Only the driver can update the vehicle software when parked and connected to a secure network."*

### **3. Key Components for the Solution**

#### **Natural Language Taxonomy:**
To translate natural language into executable policies, we must first define a clear **taxonomy** that structures natural language elements:
- **Subjects**: Who is requesting access (e.g., Driver, Mechanic).
- **Actions**: What is being performed (e.g., Update, View).
- **Resources**: What is being accessed (e.g., Software, Vehicle data).
- **Conditions**: Contextual rules (e.g., Time, Location, Speed, Connectivity).

#### **NLP Component:**
An NLP tool is required to extract these components from natural language policies. This allows for structured extraction of subjects, actions, resources, and conditions. 

**Key Steps:**
1. **Text parsing and tokenization** to break down natural language into meaningful chunks.
2. **Named Entity Recognition (NER)** for identifying roles, actions, and conditions.
3. **Grammar definition** to ensure policies are expressed in a structured way (e.g., Subject → Action → Resource → Condition).

**Libraries:** SpaCy, NLTK, or Hugging Face Transformers for parsing and extracting these elements.

#### **Policy Representation:**
Once the taxonomy is extracted, we need to map it into **formal policies**:
- **XACML structure**: XACML policies consist of `<Subject>`, `<Action>`, `<Resource>`, and `<Environment>`. The parsed natural language policies are mapped into these XML-based policy elements.

### **4. Tools & Libraries**

#### **Vakt SDK**:
We’ve identified **Vakt**, a Python-based ABAC SDK that allows you to define access control policies programmatically. It uses attributes for defining policies and inquiries to check if a request adheres to the defined policies.

- **Policy Creation**: Policies are created using attributes such as action, resource, subject, and context.
- **Inquiry Mechanism**: Inquiries represent access requests, which Vakt evaluates against stored policies.
- **Storage**: Policies can be stored in memory or more advanced backends (e.g., MongoDB), making it scalable for real-world applications.

**Example with Vakt SDK:**
```python
from vakt import Policy, ALLOW_ACCESS
from vakt.rules import Eq, CIDR

policy = Policy(
    1,
    actions=[Eq('update')],
    resources=[{'type': 'software'}],
    subjects=[{'role': 'driver'}],
    context={'location': CIDR('192.168.1.0/24')}
)
```

### **5. Example Flow (End-to-End Process)**
#### **Step 1: Natural Language Input**
A policy in natural language: *“The driver can control the vehicle only when it is stationary and connected to a secure network.”*

#### **Step 2: NLP Parsing**
Using an NLP library, we extract:
- **Subject**: Driver
- **Action**: Control
- **Resource**: Vehicle
- **Condition**: Stationary and connected to a secure network.

#### **Step 3: Policy Mapping**
The extracted components are then mapped into an **XACML policy**:
```xml
<Policy>
  <Target>
    <Subjects>
      <Subject>Driver</Subject>
    </Subjects>
    <Resources>
      <Resource>Vehicle</Resource>
    </Resources>
    <Actions>
      <Action>Control</Action>
    </Actions>
    <Environments>
      <Environment>Vehicle is stationary</Environment>
      <Environment>Connected to secure network</Environment>
    </Environments>
  </Target>
  <Rule Effect="Permit">
    <Condition>
      <Apply FunctionId="vehicleIsStationary"/>
      <Apply FunctionId="networkIsSecure"/>
    </Condition>
  </Rule>
</Policy>
```

#### **Step 4: Execution Using Vakt**
Using the Vakt SDK, we could implement this rule and test whether specific inquiries (e.g., "Driver wants to control the vehicle while parked") are allowed.

```python
from vakt import Inquiry

inquiry = Inquiry(
    subject={'role': 'driver'},
    action='control',
    resource='vehicle',
    context={'location': 'stationary', 'network': 'secure'}
)

if guard.is_allowed(inquiry):
    print("Access Granted")
else:
    print("Access Denied")
```

### **6. Challenges & Next Steps**
- **Grammar Creation**: You need to create a structured grammar that standardizes how policies are written, making NLP parsing easier.
- **Mapping Rules**: Ensure all extracted components from the NLP system map correctly into XACML and Vakt policies.
- **Edge Cases**: Handling complex conditions and nested policies (e.g., *"The driver can control the vehicle if the passenger has not overridden the settings."*).

### **Next Steps:**
1. **Choose an NLP library** (SpaCy, NLTK, or Hugging Face) for entity extraction.
2. **Define the grammar** for the natural language policies to ensure consistency in structure.
3. **Implement policy mapping** from natural language to XACML using the Vakt SDK for ABAC enforcement.
4. **Test with real-world examples** from the connected car domain and refine the translation process.
